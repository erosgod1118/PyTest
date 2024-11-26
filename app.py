import requests 

def get_json(url):
    r = requests.get(url)
    return r.json()

DEFAULT_CONFIGS = {"user": "user1", "database": "db1"}

def create_connection_string(config=None):
    config = config or DEFAULT_CONFIGS
    
    return f"User Id={config['user']}; Location={config['database']};"