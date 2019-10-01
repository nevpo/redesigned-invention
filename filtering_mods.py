import json
import pprint
#test
######### no uniq, ench, tempest, corrupt, map, normal jewel, abyss jewel, area, flask mods ########
#with open('mods.json') as f:
#    with open('mods_filtered_no_jewel.json', 'w') as dump:
#        data = json.load(f)
#        for k in list(data):
#            if data[k]["generation_type"] in {"unique", "tempest", "enchantment", "corrupted"}:
#                del data[k]
#                continue
#            if data[k]["domain"] in {'abyss_jewel', 'atlas', 'misc', 'area', 'delve', 'crafted', 'flask'}:
#                del data[k]
#        json.dump(data, dump, indent=4)

######### no non foil mods #############
#with open('mods_filtered_no_jewel.json') as f:
#    with open('mods_filtered_foils.json', 'w') as dump:
#        foil_mods = dict()
#        data = json.load(f)
#        for k in list(data):
#            count = 0
#            for m in range(0, len(list(data[k]['spawn_weights']))):
#                if count == -1:
#                    continue 
#                elif data[k]['spawn_weights'][m]['tag'] not in {'sword_elder', 'sword_shaper'}:
#                    if data[k]['spawn_weights'][m]['tag'] in {'one_hand_weapon', 'rapier', 'sword', 'weapon'}:
#                        if data[k]['spawn_weights'][m]['weight'] == 0:
#                            count = -1
#                            continue
#                        count += 1
#            if count > 0:
#                foil_mods[k] = data[k]
#        json.dump(foil_mods, dump, indent=4)

############### checking mod types count to compare with poedb #############
with open('mods_filtered_foils.json') as f:
    data = json.load(f)
    mods = list()
    type_ = list()
    for k in list(data):
        if data[k]["type"] in type_:
            continue
        type_.append(data[k]["type"])
        mods.append(k)
    pprint.pprint(len(set(mods)))