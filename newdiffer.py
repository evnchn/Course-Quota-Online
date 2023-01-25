from deepdiff import DeepDiff

import quotabeautify

import dictdiffer

import json

import ast
'''
with open("latest_state.json","r") as f:
    allcourses_dict_old = json.load(f)
    
    
with open("latest_state.json","r") as f:
    allcourses_dict = json.load(f)
    
    
allcourses_dict["ACCT1610"]["SECT"]["L1(1031)"]["Wait"] = "Unknown"

allcourses_dict["ACCT1610"]["SECT"]["L1(1031)"]["QEA"]["OPEN"]["Quota"] = 300'''


# Possible states

'''
unprocessed - OK?

attribute_added - OK
attribute_removed - OK

dictionary_item_added - OK
dictionary_item_removed - OK

set_item_added - OK
set_item_removed - OK

iterable_item_added - OK
iterable_item_removed - OK
iterable_item_moved ???????

values_changed

repetition_change

type_changes

'''

# From the docs
'''
t1 = {1: 1, 2: 2, 3: [3], 4: 4}
t2 = {1: 1, 2: 4, 3: [3, 4], 5: 5, 6: 6}
ddiff = DeepDiff(t1, t2)
pprint(ddiff, indent=4)
{   'dictionary_item_added': [root[5], root[6]],
    'dictionary_item_removed': [root[4]],
    'iterable_item_added': {'root[3][1]': 4},
    'values_changed': {'root[2]': {'new_value': 4, 'old_value': 2}}}
'''

## Helper functions

def access_dict_by_root_notation(dict_in, root_notation, parent=False):
    ### THIS IS VERY UNSAFE AND INEFFICIENT, WE GOT TO CHANGE THIS!!!
    if parent:
        root_notation = root_notation.rsplit("[",1)[0]
    return eval(root_notation, {"root":dict_in})
    
def root_notation_to_dot_notation(root_notation, parent=False):
    ### THIS IS QUITE UNSAFE AND INEFFICIENT. 
    if parent:
        root_notation = root_notation.rsplit("[",1)[0]
    return ".".join(str(ast.literal_eval(x)) for x in root_notation[:-1].replace("root[","").split("]["))

'''
old_dict = {1:[1,2,3]}
new_dict = {1:[1,2,"AAAAAA"]}
'''

def diff2(old_dict, new_dict, debug=False, CQO_special_mode=True):

    deepdiff_results = DeepDiff(old_dict, new_dict, cache_size=5000) #5000 in the docs see https://zepworks.com/deepdiff/current/optimizations.html#cache-size-label

    if debug:
        print(deepdiff_results)

    forged_dictdiffer_result = []
    forged_dictdiffer_result_dedup = []
    for deepdiff_result in deepdiff_results.items():
        result_type, result_contents = deepdiff_result


        if False:
            #Just so everything starts with elif
            pass
        elif result_type in ("attribute_added", "dictionary_item_added"):
            for result_content in result_contents:
                forged_dictdiffer_result.append(("add", root_notation_to_dot_notation(result_content), access_dict_by_root_notation(new_dict, result_content)))
        elif result_type in ("set_item_added", ):
            for result_content in result_contents:
                forged_dictdiffer_result.append(("add", root_notation_to_dot_notation(result_content), access_dict_by_root_notation(new_dict, result_content, parent=True)))
                
                
                
        elif result_type in ("attribute_removed", "dictionary_item_removed"):
            for result_content in result_contents:
                forged_dictdiffer_result.append(("remove", root_notation_to_dot_notation(result_content), access_dict_by_root_notation(old_dict, result_content)))
        elif result_type in ("set_item_removed", ):
            for result_content in result_contents:
                forged_dictdiffer_result.append(("remove", root_notation_to_dot_notation(result_content), access_dict_by_root_notation(old_dict, result_content, parent=True)))
                
        elif result_type in ("iterable_item_added", ):
            for result_path, result_value in result_contents.items():
                forged_dictdiffer_result.append(("add", root_notation_to_dot_notation(result_path), result_value))
        elif result_type in ("iterable_item_removed", ):
            for result_path, result_value in result_contents.items():
                forged_dictdiffer_result.append(("remove", root_notation_to_dot_notation(result_path), result_value))
                
        
        elif result_type in ("values_changed", "type_changes"): ## May have to separate later      
            for result_path, result_value in result_contents.items():
                location = root_notation_to_dot_notation(result_path)
                old_val, new_val = result_value["old_value"], result_value["new_value"]
                if CQO_special_mode == True:
                    is_QEA_subitem = False
                    all_unimportant_suffix = (".Enrol", ".Avail", ".Quota")
                    for unimportant_strings in all_unimportant_suffix:
                        if location.endswith(unimportant_strings):
                            # result_path = result_path.rsplit("[",1)[0] #parent
                            location = root_notation_to_dot_notation(result_path, parent=True)
                            old_val = quotabeautify.beautify(access_dict_by_root_notation(old_dict, result_path, parent=True))
                            new_val = quotabeautify.beautify(access_dict_by_root_notation(new_dict, result_path, parent=True))
                            break
                #forged_dictdiffer_result.append(("change", root_notation_to_dot_notation(result_path), (result_value["old_value"], result_value["new_value"])))
                forged_dictdiffer_result_dedup.append(("change", location, (old_val, new_val)))
        
        
        elif result_type == "unprocessed":
            if isinstance(result_contents, dict):
                # We can't be sure of the structure of the dict / list so be safe. 
                result_contents = list(result_contents.items())
            for result_content in result_contents:
                forged_dictdiffer_result.append(tuple("add", "UNPROCESSED_DD2", str(result_content)))
        
        else:
            if isinstance(result_contents, dict):
                # We can't be sure of the structure of the dict / list so be safe. 
                result_contents = list(result_contents.items())
            for result_content in result_contents:
                forged_dictdiffer_result.append(tuple("add", "UNRECOGNIZED_DD2", str(result_content)))
                
                
                
    if debug:
        print(list(dictdiffer.diff(old_dict, new_dict)))
        
        
        print(forged_dictdiffer_result)
    
    forged_dictdiffer_result_dedup = list(set(forged_dictdiffer_result_dedup))
    return forged_dictdiffer_result + forged_dictdiffer_result_dedup
    
    
if __name__ == "__main__":
    
    old_dict = {1:[1,2,3]}
    new_dict = {1:[1,2,"AAAAAA"]}
    print(diff2(old_dict, new_dict))