from datoso_seed_enhanced.dats import EnhancedDat

actions = {
    '{dat_origin}': [
        {
            'action': 'LoadDatFile',
            '_class': EnhancedDat,
        },
        {
            'action': 'DeleteOld',
            'folder': '{dat_destination}',
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}',
        },
        {
            'action': 'SaveToDatabase',
        },
    ],
}

def get_actions():
    return actions
