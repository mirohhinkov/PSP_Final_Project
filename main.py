# Task 17: Import the modules csv, tui and visual
# TODO: Your code here

import os.path
import csv

import tui
import utils.process
import visual
from utils.writer import JSON_writer

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
# TODO: Your code here

records = []
index_by_name = {}
actions = ['Load Data', 'Process Data', 'Visualise Data', 'Save Data']
funcs = ['load_data', 'process_data', 'visualise_data', 'save_data']

header = []


# returns function which wraps the original one with start and complete message
def start_complete_decorator(action):
    def decorator(f):
        def decorated_function():
            tui.started(action)
            f()
            tui.completed(action)

        return decorated_function

    return decorator


# Checks if the csv file has been loaded and populates the the objects in process module
def check_data_loaded():
    if not header:
        tui.error("Please load entity data first", "👆")
        return False

    utils.process.share_data(tui, header, records, index_by_name)  # gives access to vars in process module
    tui.share_header(header)  # gives access of header in tui
    return True


@start_complete_decorator(actions[0])
def load_data():
    while True:
        file_path = tui.source_data_path()
        if file_path and os.path.isfile(file_path):
            break
        print(f"{file_path} does not exist. Please enter correct name." if file_path else "File have to be CSV")
    with open(file_path) as sol_data:
        data_reader = csv.reader(sol_data)
        header.extend(next(data_reader))
        entity_name_index = header.index('eName')
        for ind, row in enumerate(data_reader):
            records.append(row)
            """
            index_by_name - dictionary for fast searching in records by entity name
            key - entity name
            value - index of the entity in records
            """
            index_by_name[row[entity_name_index]] = ind


@start_complete_decorator(actions[1])
def process_data():
    if not check_data_loaded():
        return False

    operation_actions = ['Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
                         'Categorise entities by gravity', 'Summarise entities by orbit']
    operation_funcs = ['retrieve', 'details', 'category',
                       'gravity', 'orbit']

    @start_complete_decorator(operation_actions[0])
    def retrieve():
        utils.process.retrieve_entity()

    @start_complete_decorator(operation_actions[1])
    def details():
        utils.process.entity_details()

    @start_complete_decorator(operation_actions[2])
    def category():
        utils.process.entities_category()

    @start_complete_decorator(operation_actions[3])
    def gravity():
        utils.process.entities_gravity()

    @start_complete_decorator(operation_actions[4])
    def orbit():
        utils.process.entities_orbit()

    while True:
        menu_selection = tui.process_type()
        if menu_selection:
            break
    locals()[operation_funcs[menu_selection - 1]]()


@start_complete_decorator(actions[2])
def visualise_data():
    if not check_data_loaded():
        return False

    operation_actions = ['Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities']
    operation_funcs = ['pie', 'bar', 'orbits', 'gravity']

    @start_complete_decorator(operation_actions[0])
    def pie():
        visual.entities_pie(utils.process.entities_category(False))

    @start_complete_decorator(operation_actions[1])
    def bar():
        visual.entities_bar(utils.process.entities_gravity(False))

    @start_complete_decorator(operation_actions[2])
    def orbits():
        visual.orbits(utils.process.entities_orbit(False))

    @start_complete_decorator(operation_actions[3])
    def gravity():
        visual.gravity_animation(utils.process.entities_gravity(False))

    while True:
        menu_selection = tui.visualise()
        if menu_selection:
            break
    locals()[operation_funcs[menu_selection - 1]]()


@start_complete_decorator(actions[3])
def save_data():
    if not check_data_loaded():
        return False
    writer = JSON_writer()
    writer.process_data().encode_data().write_data().display()


def run():
    tui.welcome()
    while True:
        menu_selection = tui.menu()
        if menu_selection:
            if menu_selection == 5:
                break
            else:
                globals()[funcs[menu_selection - 1]]()


# starting point of the app
if __name__ == "__main__":
    run()
