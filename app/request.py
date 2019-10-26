import requests

# getting api 
base_url = None


# getting quotes base url
def config_request(app):
    
    global base_url
    base_url = app.config['QUOTES_API_BASE_URL']