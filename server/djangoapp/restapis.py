# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    # Build query parameters if provided
    params = "&".join(f"{key}={value}" for key, value in kwargs.items())

    # Construct request URL conditionally
    if params:
        request_url = f"{backend_url}{endpoint}?{params}"
    else:
        request_url = f"{backend_url}{endpoint}"

    print(f"GET from {request_url}")
    try:
        # Call get method of requests library with URL
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log or print exception details
        print(f"Network exception occurred: {e}")
        return {"error": "Network exception occurred"}


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
        
# Add code for posting review
