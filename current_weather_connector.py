from requests import get
import csv


def flatten_response(d):
    result = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten_response(subdict).items()
                result.update({key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            result[key] = val
    return result


api_key = "5f99a6817d6b8f4677f941d31dcbbba7"

city_name = input("For which city would you like to know the current weather? \n")

city_name_param_key = "q"
api_key_key = "appid"

url = "http://api.openweathermap.org/data/2.5/weather?units=metric"

query_params = {city_name_param_key: city_name,
                api_key_key: api_key}

response = get(url, params=query_params)

response_dict = flatten_response(response.json())

with open('weather_file.csv', 'w') as file:
    w = csv.writer(file)
    w.writerows(response_dict.items())

print("Thank you, your file was created!")