import json
def normalize_keys(data):
    
    if isinstance(data, dict):
        return {
            k.lower(): normalize_keys(v) for k, v in data.items()
        }
    
    elif isinstance(data, list):
        return [normalize_keys(i) for i in data]

    else:
        return data


raw_input_string = '{"CONFIG": {"SiteName": "Bangalore", "DEVICES_ONLINE": 12, "Tickets": [{"ID": 1}]}}'


cleaned_data = normalize_keys(json.loads(raw_input_string))


print(json.dumps(cleaned_data, indent=2))
    