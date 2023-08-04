import json
import requests

class Food:
    def __init__(self, upc, food_information_json):
        self.food_barcode = upc
        self.json_file_path = food_information_json

        self.information_get(self.food_barcode, self.json_file_path)
        self.set_carbs()
        self.set_fat()
        self.set_brand()
        self.set_protien()
        self.set_description()
        self.get_calories()  
        
        


    


    def information_get(self, upc, food_barcode): #construct with UPC code from a barcode Scanner Eventually
        API_KEY = 'iigmKe0ZBdEoC508ltRcj8bIzIXdzzWsz7bgaKpO'
        UPC_CODE= self.food_barcode
        json_file_path = self.json_file_path

        api_url = ('https://api.nal.usda.gov/fdc/v1/foods/search?query={1}&pageSize=2&api_key={0}'.format(API_KEY,UPC_CODE))
        response = requests.get(api_url)

        item_info_dic = response.json()

        with open(json_file_path, 'w') as f:
            f.write( json.dumps(item_info_dic, indent = 6))

    def get_brand(self):
        with open(self.json_file_path, 'r') as f:
            item_json = json.load(f)

        for x in item_json['foods']:        
            for y in x['foodNutrients']:
                food_name = x.get('brandName')
        
        return food_name

    def get_protien(self):
        with open(self.json_file_path, 'r') as f:
            item_json = json.load(f)

        for x in item_json['foods']:        
            for y in x['foodNutrients']:            
                if 'nutrientId' in y.keys():
                    if 1003 == y['nutrientId']:
                        protienValue = y['value']
        return protienValue 
    
    def get_fat(self):
        with open(self.json_file_path, 'r') as f:
            item_json = json.load(f)

        for x in item_json['foods']:        
            for y in x['foodNutrients']:            
                if 'nutrientId' in y.keys():
                    if 1005 == y['nutrientId']:
                        fatValue = y['value']
        return fatValue 

    def get_carbs(self):
        with open(self.json_file_path, 'r') as f:
            item_json = json.load(f)

        for x in item_json['foods']:        
            for y in x['foodNutrients']:            
                if 'nutrientId' in y.keys():
                    if 1004 == y['nutrientId']:
                        carbValue = y['value']
        return carbValue 
    
    def get_calories(self):
        self.calories = ((self.protien)*4) + ((self.carbs)*4) + ((self.fat) *9)

    def get_description(self):
        with open(self.json_file_path, 'r') as f:
            item_json = json.load(f)

        for x in item_json['foods']:        
            description = x.get('description')

        return description
    
    def set_brand(self ):
        self.brand = self.get_brand()

    def set_description(self):
        self.description = self.get_description()

    def set_protien(self):
        self.protien = self.get_protien()

    def set_fat(self):
        self.fat = self.get_fat()
    
    def set_carbs(self):
        self.carbs = self.get_carbs()


    def __str__(self) -> str:
        return self.brand + '\n'+ self.description + '\n' + str(self.carbs) + '\n' + str(self.fat) + '\n' + str(self.protien) + '\n' + str(self.calories)
    
    def get_c_brand(self):
        return self.brand
    def get_c_description(self):
        return self.description
    def get_c_protien(self):
        return self.protien
    def get_c_fat(self):
        return self.fat
    def get_c_carbs(self):
        return self.carbs
