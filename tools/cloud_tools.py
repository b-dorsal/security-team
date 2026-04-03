import json

def list_available_resources() -> str:
    """
    Returns a list of available cloud resource types.
    """
    print(f'Agent requests resource list')
    try:
        with open('cloud_config.json', 'r') as file:
            data = json.load(file)
        response = json.dumps(list(res for res in data.get("resources")))
        print(response)
        return response
        
    
    except FileNotFoundError:
        print("ERROR: JSON FILE NOT FOUND")
        exit(1)
        # return json.dumps({"error": "json file not found"})

def query_cloud_config(resource_type: str) -> str:
    """
    Fetches the configuration metadata for a specific cloud resource type.

    Args:
        resource_type: The type of resource to look up (e.g., 'iam_policies', 'storage_buckets').
    """
    print(f'Agent requests {resource_type}')
    try:
        with open('cloud_config.json', 'r') as file:
            data = json.load(file)
        
        resources = data.get("resources").get(resource_type)
        
        for resource in resources:
            if hasattr(resources[resource], '__setitem__'):
                resources[resource]['tcbs'] = None
        response = json.dumps(resources)
        print(response)
        return response
    
    except FileNotFoundError:
        exit(1)
        # return json.dumps({"error": "json file not found"})
