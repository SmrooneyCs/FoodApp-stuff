import json
import requests
import FoodClass




def main():
   
    
    food1 = FoodClass.Food('077567254344',"BarcodeInfo.json")
    food2 = FoodClass.Food('073416000148','BarcodeInfo.json')

    print(food1)
    print(food2)

main()

