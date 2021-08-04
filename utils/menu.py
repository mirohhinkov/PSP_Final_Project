def utils_menu(error, *menu_items):
    for i in range(len(menu_items)):
        print(f"{i + 1}: {menu_items[i]}")
    choice = input("Please select an option: ")
    if choice.isnumeric() and int(choice) - 1 in range(len(menu_items)):
        return int(choice)
    else:
        error("Invalid option.")
