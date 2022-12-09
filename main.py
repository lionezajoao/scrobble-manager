import os
import dotenv
import requests
dotenv.load_dotenv()

api_key = os.environ.get('API_KEY') 
url = f'http://www.last.fm/api/auth/?api_key={api_key}'

requests.get(url)