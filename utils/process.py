def retrieve_entity(tui, records, index_by_name):
    name = tui.entity_name()
    if name in index_by_name:
        tui.list_entity(records[index_by_name[name]])
    else:
        tui.error(f"Entity with name {name} not found!", "👽")

def entity_details():
    print('entity_details')


def entities_type():
    print('retrieve_entity')


def entities_gravity():
    print('entities_gravity')


def entities_orbit():
    print('entities_orbit')
