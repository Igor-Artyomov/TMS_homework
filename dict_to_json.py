import json


d = {
    111111: ('Max', 25), 
    222222: ('Sam', 32), 
    333333: ('Jim', 28), 
    444444: ('Nick', 24), 
    555555: ('Ken', 36)
    }

with open('dict_to_json.json', 'w') as outfile:
    json.dump(d, outfile)