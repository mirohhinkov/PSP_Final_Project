tui = header = records = index_by_name = None


def share_data(*data):
    global tui, header, records, index_by_name
    tui, header, records, index_by_name = data


def find_by_name_print(name, cols=None):
    if cols is None:
        cols = []
    if name in index_by_name:
        tui.list_entity(records[index_by_name[name]], cols)
    else:
        tui.error(f"Entity with name {name} not found!", "👽")


def retrieve_entity():
    name = tui.entity_name()
    find_by_name_print(name)


def entity_details():
    name, cols = tui.entity_details()
    # includes entity name as first field if fields exists else all fields to be printed
    cols = [0, *cols] if cols else []
    find_by_name_print(name, cols)


def entities_category(screen=True):
    ind = header.index('isPlanet')
    planets = []
    non_planet = []
    for entity in records:
        if eval(entity[ind].capitalize()):
            planets.append(entity)
        else:
            non_planet.append(entity)
    result = {"Planets": planets, "Non-planets": non_planet}
    if screen:
        tui.list_categories(result)
    return result


def entities_gravity(screen=True):
    low = []
    medium = []
    high = []
    lower, up = tui.gravity_range()
    ind_gravity = header.index('gravity')
    for entity in records:
        if float(entity[ind_gravity]) < lower:
            low.append(entity)
        elif float(entity[ind_gravity]) > up:
            high.append(entity)
        else:
            medium.append(entity)
    result = {"Low gravity": low,
              "Medium gravity": medium,
              "High gravity": high}
    if screen:
        tui.list_categories(result)
    return result


def entities_orbit(screen=True):
    ind_orbits = header.index('orbits')
    ind_radius = header.index('meanRadius')
    inputs = tui.orbits()
    # filters only planets from the input list (check if is an entity and if an entity if is a planet)
    planets = [x for x in inputs if x in index_by_name and records[index_by_name[x]][ind_orbits] == 'NA']
    # creates empty dict
    print(planets)
    orbits = {planet: {'small': [], 'large': []} for planet in planets}

    for entity in records:
        if entity[ind_orbits] in planets:  # checks if the entity orbits around one of the selected planets
            s_l = 'small' if float(entity[ind_radius]) < 100.0 else 'large'  # select the category of the entity
            orbits[entity[ind_orbits]][s_l].append(entity)
    print(orbits)
    if screen:
        for planet in planets:
            print(f"\n{planet} orbits:")
            tui.list_categories(orbits[planet])
    return orbits
