def select_fruit(items: dict) -> dict:
    fruits = dict()
    for item, type in produce.items():
        if type == "Fruit":
            fruits[item] = "Fruit"
    return fruits

produce = {
    "apple": "Fruit",
    "carrot": "Vegetable",
    "pear": "Fruit",
    "broccoli": "Vegetable",
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }
