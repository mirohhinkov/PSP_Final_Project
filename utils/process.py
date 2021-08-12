tui = header = records = index_by_name = None


def share_data(*data):
    globals()['tui'] = data[0]
    globals()['header'] = data[1]
    globals()['records'] = data[2]
    globals()['index_by_name'] = data[3]


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
    cols = [0, *cols] if cols else []
    find_by_name_print(name, cols)


def entities_category():
    ind = header.index('isPlanet')
    planets = []
    non_planet = []
    for entity in records:
        if eval(entity[ind].capitalize()):
            planets.append(entity)
        else:
            non_planet.append(entity)
    tui.list_categories({"Planets": planets, "Non-planets": non_planet})


def entities_gravity():
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
    tui.list_categories({"Low gravity": low,
                         "Medium gravity": medium,
                         "High gravity": high})


def entities_orbit():
    ind_orbits = header.index('orbits')
    ind_radius = header.index('meanRadius')
    inputs = tui.orbits()
    planets = [x for x in inputs if x in index_by_name and records[index_by_name[x]][ind_orbits] == 'NA']
    orbits = {planet: {'small': [], 'large': []} for planet in planets}
    for entity in records:
        if entity[ind_orbits] in planets:  # checks if the entity orbits around one of the selected planets
            s_l = 'small' if float(entity[ind_radius]) < 100.0 else 'large'  # select the category of the entity
            orbits[entity[ind_orbits]][s_l].append(entity)
    for planet in planets:
        print(f"\n{planet} orbits:")
        tui.list_categories(orbits[planet])
