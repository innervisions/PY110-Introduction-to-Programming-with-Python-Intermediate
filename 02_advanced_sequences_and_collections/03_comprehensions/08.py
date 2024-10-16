def relevant_data(produce):
    if produce['type'] == 'fruit':
        return [color.capitalize() for color in produce['colors']]
    if produce['type'] == 'vegetable':
        return produce['size'].upper()

dict1 = {
    "grape": {
        "type": "fruit",
        "colors": ["red", "green"],
        "size": "small",
    },
    "carrot": {
        "type": "vegetable",
        "colors": ["orange"],
        "size": "medium",
    },
    "apricot": {
        "type": "fruit",
        "colors": ["orange"],
        "size": "medium",
    },
    "marrow": {
        "type": "vegetable",
        "colors": ["green"],
        "size": "large",
    },
}

lst = [relevant_data(produce) for produce in dict1.values()]
print(lst)
