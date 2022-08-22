import json




with open("BarcodeInfo.json", 'r') as f:
    item_json = json.load(f)

#retriving Macros from JSON file
for x in item_json['foods']:
    for y in x['foodNutrients']:
        if 'nutrientName' in y.keys():
            if 'Protein' in y['nutrientName']:
                protienValue =  (y['value'] * (x.get('servingSize'))/100)
                print(y['nutrientName'] + ': {0:.2f}' .format(((y['value'] * (x.get('servingSize'))/100))) + y['unitName']) 
            if 'Carbohydrate, by difference' in y['nutrientName']:
                carbValue = (y['value'] * (x.get('servingSize'))/100)
                print('Carbohydrates' + ': {0:.2f}' .format(((y['value'] * (x.get('servingSize'))/100))) + y['unitName'])
            if 'Total lipid (fat)'in y['nutrientName']:
                fatValue = (y['value'] * (x.get('servingSize'))/100)
                print('Fat' + ': {0:.2f}' .format(((y['value'] * (x.get('servingSize'))/100))) + y['unitName'])
                
#Getting calories per serving
calories = (protienValue*4) + (carbValue*4) + (fatValue *9)
print('Calories per Serving: ',end = '')
print('{0:.2f}'.format(calories))