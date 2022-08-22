#Creating a json file to read from so I dont spam call the api
#URL for api website https://fdc.nal.usda.gov/api-guide.html#bkmk-2


import json
import requests
API_KEY = 'iigmKe0ZBdEoC508ltRcj8bIzIXdzzWsz7bgaKpO'
UPC_CODE= '039978041531'
json_file_path = "BarcodeInfo.json"

api_url = ('https://api.nal.usda.gov/fdc/v1/foods/search?query={1}&pageSize=2&api_key={0}'.format(API_KEY,UPC_CODE))
response = requests.get(api_url)

item_info_dic = response.json()




with open(json_file_path, 'w') as f:
    f.write( json.dumps(item_info_dic) )