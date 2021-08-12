#!/usr/bin/python3.9
from utils.menu import utils_menu
import re
import os

header = None


def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here
    welcome_msg = " Solar Record Management System "
    try:
        size = os.get_terminal_size().columns
    except (AttributeError, ValueError, OSError):
        size = 80
    print(welcome_msg.center(size, '-'))


def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # TODO: Your code here
    return utils_menu(error, 'Load Data', 'Process Data', 'Visualise Data', 'Save Data', 'Exit')


def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f"\n{operation} has started.")


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f"\n{operation} has completed.")


def error(error_msg, emoji="💥"):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param emoji:
    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f"\n{emoji} {error_msg}.\n")


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Your code here
    path = input("\nPlease enter the file path for a data file\nFor default file - data/sol_data.csv - press enter: ") \
        .strip() \
        .replace('\\', '/')

    if not path:
        return 'data/sol_data.csv'

    path_list = path.split(".")
    if len(path_list) >= 2 and path_list[-1].lower() == 'csv':
        return path
    else:
        error("Please enter a proper file name (including path)", "")


def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    return utils_menu(error, 'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
                      'Categorise entities by gravity', 'Summarise entities by orbit')


def entity_name(msg='Please enter the name of the entity: '):
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    # TODO: Your code here
    return input(msg).strip().capitalize()


def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    # TODO: Your code here
    name = entity_name()
    ind = []
    print("Please enter a list of integer column indexes or names:\nTo stop press Enter")
    while True:
        user_input = input("index or name: ")
        if not user_input:
            break
        if user_input.isnumeric():
            choice = int(user_input)
            to_add = choice if 0 < choice < len(header) else 0
        else:
            to_add = header.index(user_input) if user_input in header else 0
        if to_add and to_add not in ind:
            ind.append(to_add)
        else:
            error("It's already there" if ind else "Please enter a proper value", "")
    return [name, ind]


def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # TODO: Your code here
    to_print = ["{0:<10}".format(entity[i]) for i in cols] if cols else ["{:<10}".format(x) for x in entity]
    print(*to_print)


def list_entities(entities, cols=[]):
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    for entity in entities:
        list_entity(entity, cols)


def list_categories(categories):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here
    for category in categories:
        if len(categories[category]):
            print(f"\nCategory: {category}")
            list_entities(categories[category])


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    # TODO: Your code here
    print("\nPlease the lower and upper limit for a range of gravity")
    lower = input_numb("lower limit: ")
    upper = input_numb("upper limit: ")
    return (lower, upper) if lower < upper else (upper, lower)
    # while True:
    #     lower = input("lower limit: ")
    #     upper = None
    #     print(is_numb(lower))
    #     if is_numb(lower):
    #         float(lower)
    #         upper = input("upper limit: ")
    #         if is_numb(upper):
    #             float(upper)
    #     if type(upper) is float:
    #         return lower, upper
    #     error("Please enter proper values")
    # ---------------------------------
    #   try:
    #       lower = float(input("lower limit: "))
    #       upper = float(input("upper limit: "))
    #       if lower < 0 or upper < 0 or lower > upper:
    #           raise Exception()
    #       return lower, upper
    #   except:
    #       error("Please enter proper values")


def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # TODO: Your code here
    entity_names = []
    print("\nPlease enter a list of entity names (one by one or comma separated)\nTo stop press enter\n")
    while True:
        ent_name = entity_name("Enter entity name(s): ")
        if not ent_name:
            return entity_names
        entity_names.extend([x.strip().capitalize() for x in ent_name.split(",")])


def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    return utils_menu(error, 'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities')


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    return utils_menu(error, 'Export as JSON')


def is_numb(user_input):
    return user_input.isnumeric() or re.match(r'^\d*\.\d*$', user_input) is not None


def input_numb(msg=''):
    while True:
        numb = input(msg).strip()
        if is_numb(numb):
            return float(numb)
        error("Please enter proper values")


def share_header(h):
    globals()['header'] = h


def run():
    # welcome()
    # print(menu())
    # print(source_data_path())
    # print(process_type())
    # print(entity_details(['', 'gravity', 'velocity', 'radius', 'weight', 'distance']))
    # list_entity(['Earth', True, 9.8])
    # list_categories({"Hard": [['Earth', True, 9.8], ['Mars', True, 6.8]],
    #                  "Soft": [['Jupiter', True, 40.8], ['Saturn', True, 20.8]]})
    print(gravity_range())
    # print(orbits())
    # print(visualise())
    # print(save())


if __name__ == "__main__":
    run()
