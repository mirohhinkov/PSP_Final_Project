def utils_menu(error, *menu_items):
    for i in range(len(menu_items)):
        print(f"{i + 1}: {menu_items[i]}")
    try:
        choice = int(input("Please select an option: "))
        if choice - 1 in range(len(menu_items)):
            return choice
        raise Exception("Out of range")
    except Exception as err:
        if err.args[0] == "Out of range":
            error(f"Please, choose a number from 1 to {len(menu_items)}", "👇")
        else:
            error("Invalid option.")
