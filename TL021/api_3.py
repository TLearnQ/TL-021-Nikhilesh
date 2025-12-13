import yaml
import json

class APIResponseError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status
url = r"C:\Users\nikhi\TL021\3rd.yml"

output_file = r"C:\Users\nikhi\TL021\log3.txt"
error_file = r"C:\Users\nikhi\TL021\error_log3.txt"
summary_file = r"C:\Users\nikhi\TL021\summary3.txt"

def task1_parse_yaml(url, output_file, error_file, summary_file):
    with open(url) as file:
        data = yaml.safe_load(file)

    if not data:
        raise APIResponseError("YAML file is empty or unreadable")


    paths = data.get("paths")
    if paths is None:
        raise APIResponseError("Missing 'paths' section in OpenAPI spec")

    metadata = []

    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() in ["get", "post", "put", "delete", "patch"]:

                entry = {
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get("summary"),
                    "description": details.get("description"),
                    "operationId": details.get("operationId"),
                    "tags": details.get("tags"),
                    "responses": details.get("responses", {})
                }

                metadata.append(entry)

    if not metadata:
        raise APIResponseError("No endpoints found in the API spec")


    with open(output_file, "w") as f:
        json.dump(metadata, f, indent=2)
        

    return metadata
    with open(error_log.txt, "w") as f:
        json.dump(metadata, f, indent=2)
    return metadata
try:
    task1_parse_yaml(url, output_file, error_file, summary_file)
except APIResponseError as e:
    with open(output_file, "w") as f:
        f.write(f"Error: {e}, Status: {e.status}\n")
    print(f"Error: {e}, Status: {e.status}")
    print(f"Metadata successfully written to {output_file}")
    print(f"Error details written to {error_file}")
try:
    task1_parse_yaml(url, output_file, error_file, summary_file)
    raise APIResponseError("Simulated error for demonstration", status=500)
except APIResponseError as e:
    with open(error_file, "w") as f:
        f.write(f"Error: {e}, Status: {e.status}\n")
    print(f"Error: {e}, Status: {e.status}")