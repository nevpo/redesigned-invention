import json

class Item:
    def __init__(self, _base = 'foil', _type = 'normal', \
                       ilvl = 86):
        self.base = _base
        self.type = _type
        self.ilvl = ilvl
        self.suffixes = []
        self.prefixes = []
        self.mod_pool = {}
        #TODO: add poe.trade pseudo mods?
    
    def add_mod(self, _type='', _mod=''):
        if _type == 'suffix':
            self.suffixes.append(_mod)
        else:
            self.prefixes.append(_mod)

    def get_mods(self):
        _ = {}
        _['Prefix'] = self.prefixes
        _['Suffix'] = self.suffixes
        return _
    