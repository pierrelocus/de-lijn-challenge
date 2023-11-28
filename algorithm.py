import copy
import pprint

space = {
    'GROOT': 16,
    'NORMAAL': 12,
    'MINI': 10
}

sizes = {
    'GROOT': 4,
    'NORMAAL': 2,
    'MINI': 1
}

inpt = {
    'stelplaats': "De Lijn Arsenaal",
    'parking': [
        {'bus': "1000", 'type': "GROOT"},
        {'bus': "1001", 'type': "GROOT"},
        {'bus': "1002", 'type': "GROOT"},
        {'bus': "2000", 'type': "NORMAAL"},
        {'bus': "2001", 'type': "NORMAAL"},
        {'bus': "2002", 'type': "NORMAAL"},
        {'bus': "2003", 'type': "NORMAAL"},
        {'bus': "2004", 'type': "NORMAAL"},
        {'bus': "2005", 'type': "NORMAAL"},
        {'bus': "3000", 'type': "MINI"},
        {'bus': "3001", 'type': "MINI"},
        {'bus': "3002", 'type': "MINI"},
        {'bus': "3003", 'type': "MINI"},
        {'bus': "3004", 'type': "MINI"},
        {'bus': "3005", 'type': "MINI"},
        {'bus': "3006", 'type': "MINI"},
        {'bus': "3007", 'type': "MINI"},
        {'bus': "3008", 'type': "MINI"},
        {'bus': "3009", 'type': "MINI"},
        {'bus': "3010", 'type': "MINI"},
        {'bus': "3011", 'type': "MINI"},
        {'bus': "3012", 'type': "MINI"},
    ],
    'garage': {
        'groot': [],
        'medium': [],
        'klein': []
    }
}


def sort_key(x):
    return {'GROOT': 0, 'NORMAAL': 1, 'MINI': 2}[x['type']], x['bus']


def assign_bus(inpt, bus):
    if bus['type'] == 'GROOT' and space['GROOT'] >= sizes['GROOT']:
        inpt['garage']['groot'].append(bus)
        space['GROOT'] -= sizes['GROOT']

    elif bus['type'] == 'NORMAAL':
        if space['GROOT'] >= sizes['NORMAAL']:
            inpt['garage']['groot'].append(bus)
            space['GROOT'] -= sizes['NORMAAL']
        elif space['NORMAAL'] >= sizes['NORMAAL']:
            inpt['garage']['medium'].append(bus)
            space['NORMAAL'] -= sizes['NORMAAL']

    elif bus['type'] == 'MINI':
        if space['GROOT'] >= sizes['MINI']:
            inpt['garage']['groot'].append(bus)
            space['GROOT'] -= sizes['MINI']
        elif space['NORMAAL'] >= sizes['MINI']:
            inpt['garage']['medium'].append(bus)
            space['NORMAAL'] -= sizes['MINI']
        elif space['MINI'] >= sizes['MINI']:
            inpt['garage']['klein'].append(bus)
            space['MINI'] -= sizes['MINI']

    return inpt


def assign_busses(inpt):
    for bus in sorted(copy.copy(inpt['parking']), key=sort_key):
        inpt = assign_bus(inpt, bus)

    return inpt


pprint.pprint(assign_busses(inpt)['garage'])
