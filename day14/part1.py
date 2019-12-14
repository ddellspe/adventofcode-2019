import math
from collections import defaultdict

def get_required_inputs(output, reactions):
    output_count, output_item = output
    for (rx_output_count, rx_output), rx_inputs in reactions.items():
        if output_item == rx_output:
            multiplier = math.ceil(output_count/rx_output_count)
            return [(input_count*multiplier, input_item) for (input_count, input_item) in rx_inputs], multiplier*rx_output_count

def get_dependent_inputs(output, reactions):
    dependents = set()
    for (rx_output_count, rx_output), rx_inputs in reactions.items():
        if output == rx_output:
            for (rx_intput_count, rx_input) in rx_inputs:
                dependents.add(rx_input)
    current_dependents = set()
    while len(dependents) != len(current_dependents):
        current_dependents = dependents.copy()
        for dependent in current_dependents:
            for (rx_output_count, rx_output), rx_inputs in reactions.items():
                if dependent == rx_output:
                    for (rx_intput_count, rx_input) in rx_inputs:
                        dependents.add(rx_input)
    return dependents

def compact_list(items):
    ingredient_dict = defaultdict(lambda:0)
    for (item_count, item) in items:
        ingredient_dict[item]+=item_count
    return [(item_count, item) for item, item_count in ingredient_dict.items()]

def calculate_ore(fuel_count, reaction_map, ordered_dependents):
    ingredients, multiplier = get_required_inputs((fuel_count, 'FUEL'), reaction_map)
    while len(ingredients) > 1:
        raw_ingredients = [ingredient[1] for ingredient in ingredients]
        processed = False
        for dependent in ordered_dependents:
            for ingredient in ingredients:
                if dependent == ingredient[1]:
                    extend_ingredients, generated = get_required_inputs(ingredient, reaction_map)
                    ingredients.extend(extend_ingredients)
                    ingredients.remove(ingredient)
                    processed = True
                    break
                else:
                    continue
            if processed:
                break
        ingredients = compact_list(ingredients)
    return ingredients[0][0]


reaction_map = {}
with open('input.txt','r') as file:
    for line in file.readlines():
        [input, output] = [item.strip() for item in line.split('=>')]
        reaction_map[(int(output.split(' ')[0]), output.split(' ')[1])] = [(int(ingredient.strip().split(' ')[0]), ingredient.strip().split(' ')[1]) for ingredient in input.split(',')]

reaction_dependents = {}
for output in reaction_map.keys():
    reaction_dependents[output[1]] = get_dependent_inputs(output[1], reaction_map)

output = None
output_count = 0
for item, dependents in reaction_dependents.items():
    if len(dependents) > output_count:
        output = item
        output_count = len(dependents)
ordered_dependents = []
while len(ordered_dependents) < len(reaction_dependents.keys()):
    max = 0
    max_item = None
    for item, dependents in reaction_dependents.items():
        if item in ordered_dependents:
            continue
        if len(dependents) > max:
            max_item = item
            max = len(dependents)
    ordered_dependents.append(max_item)
ordered_dependents.remove('FUEL')
ore = calculate_ore(1, reaction_map, ordered_dependents)
print(ore)