# Task 17: Import the modules csv, tui and visual
# TODO: Your code here
import tui
import os.path
import csv
import utils.process

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
# TODO: Your code here

records = []
index_by_name = {}
actions = ['Load Data', 'Process Data', 'Visualise Data', 'Save Data']
funcs = ['load_data', 'process_data', 'visualise_data', 'save_data']

header = []


def load_data():
    while True:
        file_path = tui.source_data_path()
        if file_path and os.path.isfile(file_path):
            break
        print(f"{file_path} does not exist. Please enter correct name." if file_path else "File have to be CSV")
    with open(file_path) as sol_data:
        data_reader = csv.reader(sol_data)
        for ind, row in enumerate(data_reader):
            if ind:
                records.append(row)
                index_by_name[row[entity_name_index]] = ind - 1
            else:
                header.extend(row)
                entity_name_index = header.index('eName')
        # ind = 0
        # for row in data_reader:
        #     if not header:
        #         header.extend(row)
        #         entity_name_index = header.index('eName')
        #     else:
        #         records.append(row)
        #         index_by_name[row[entity_name_index]] = ind
        #         ind += 1
    tui.print_gl()

def process_data():
    tui.started("Data processing")
    if not header:
        tui.error("Please load entity data first", "👆")
        return False

    def retrieve():
        utils.process.retrieve_entity(tui, records, index_by_name)

    def details():
        utils.process.entity_details(tui, header, records, index_by_name)

    def category():
        utils.process.entities_category(tui, header, records)

    def gravity():
        utils.process.entities_gravity(tui, header, records)

    def orbit():
        utils.process.entities_orbit(tui, header, records, index_by_name)

    operation_actions = ['Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
                         'Categorise entities by gravity', 'Summarise entities by orbit']
    operation_funcs = ['retrieve', 'details', 'category',
                       'gravity', 'orbit']

    while True:
        menu_selection = tui.process_type()
        if menu_selection:
            break
    tui.started(operation_actions[menu_selection - 1])
    locals()[operation_funcs[menu_selection - 1]]()
    tui.completed(operation_actions[menu_selection - 1])

    tui.completed("Data processing")


def visualise_data():
    print('Visualise...')


def save_data():
    print('Saving...')


def run():
    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()
    while True:
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        menu_selection = tui.menu()
        if menu_selection:
            if menu_selection == 5:
                break
            else:
                tui.started(actions[menu_selection - 1])
                globals()[funcs[menu_selection - 1]]()
                tui.completed(actions[menu_selection - 1])

        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        # TODO: Your code here

    # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
    # - Use the appropriate function in the module tui to display a message to indicate that the data processing
    # operation has started.
    # - Process the data (see below).
    # - Use the appropriate function in the module tui to display a message to indicate that the data processing
    # operation has completed.
    #
    # To process the data, it is recommended that you create and call one or more separate functions that do the
    # following:
    # - Use the appropriate function in the module tui to display a menu of options for processing the data.
    # - Check what option has been selected
    #
    #   - If the user selected the option to retrieve an entity then
    #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
    #       has started.
    #       - Use the appropriate function in the module tui to retrieve the entity name
    #       - Find the record for the specified entity in records.  You should appropriately handle the case
    #       where the entity cannot be found.
    #       - Use the appropriate function in the module tui to list the entity
    #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
    #       completed.
    #
    #   - If the user selected the option to retrieve an entity's details then
    #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
    #       process has started.
    #       - Use the appropriate function in the module tui to retrieve the entity details
    #       - Find the record for the specified entity details in records.  You should appropriately handle the
    #       case where the entity cannot be found.
    #       - Use the appropriate function in the module tui to list the entity
    #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
    #       process has completed.
    #
    #   - If the user selected the option to categorise entities by their type then
    #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
    #       process has started.
    #       - Iterate through each record in records and assemble a dictionary containing a list of planets
    #       and a list of non-planets.
    #       - Use the appropriate function in the module tui to list the categories.
    #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
    #       process has completed.
    #
    #   - If the user selected the option to categorise entities by their gravity then
    #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
    #       process has started.
    #       - Use the appropriate function in the module tui to retrieve a gravity range
    #       - Iterate through each record in records and assemble a dictionary containing lists of entities
    #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
    #       - Use the appropriate function in the module tui to list the categories.
    #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
    #       process has completed.
    #
    #   - If the user selected the option to generate an orbit summary then
    #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
    #       started.
    #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
    #       - Iterate through each record in records and find entities that orbit a planet in the list of
    #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
    #       accessed as follows:
    #           name_of_dict[planet_orbited][category]
    #       where category is "small" if the mean radius of the entity is below 100 and "large" otherwise.
    #       - Use the appropriate function in the module tui to list the categories.
    #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
    #       completed.
    # TODO: Your code here

    # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
    # - Use the appropriate function in the module tui to indicate that the data visualisation operation
    # has started.
    # - Visualise the data (see below).
    # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
    # operation has completed.
    #
    # To visualise the data, it is recommended that you create and call one or more separate functions that do the
    # following:
    # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
    # - Check what option has been selected
    #
    #   - if the user selected the option to visualise the entity type then
    #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
    #       process has started.
    #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
    #       non-planets.
    #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
    #       and non-planets
    #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
    #       process has completed.
    #
    #   - if the user selected the option to visualise the entity gravity then
    #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
    #       process has started.
    #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
    #       low (below lower limit), medium and high (above upper limit) gravity categories.
    #       - Use the appropriate function in the module visual to display a bar chart for the gravities
    #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
    #       process has completed.
    #
    #   - if the user selected the option to visualise the orbit summary then
    #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
    #       process has started.
    #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
    #       - Use the appropriate function in the module visual to display subplots for the orbits
    #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
    #       process has completed.
    #
    #   - if the user selected the option to animate the planet gravities then
    #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
    #       process has started.
    #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
    #       low (below lower limit), medium and high (above upper limit) gravity categories.
    #       - Use the appropriate function in the module visual to animate the gravity.
    #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
    #       process has completed.
    # TODO: Your code here

    # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
    # - Use the appropriate function in the module tui to indicate that the save data operation has started.
    # - Save the data (see below)
    # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
    #
    # To save the data, you should demonstrate the application of OOP principles including the concepts of
    # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
    # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
    # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets
    # in alphabetical order.
    # TODO: Your code here

    # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
    # break out of the loop
    # TODO: Your code here

    # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
    # display an error message
    # TODO: Your code here


if __name__ == "__main__":
    run()
