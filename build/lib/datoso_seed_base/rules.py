from datoso_seed_enhanced.dats import EnhancedDat

rules = [
    {
        'name': 'Enhanced Dat',
        '_class': EnhancedDat,
        'seed': 'Enhanced',
        'priority': 0,
        'rules': [
            {
                'key': 'url',
                'operator': 'contains',
                'value': 'www._enhanced.org',
            },
            {
                'key': 'homepage',
                'operator': 'eq',
                'value': '_enhanced',
            },
        ],
    },
]


def get_rules():
    return rules
