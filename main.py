from locust import between
from api_requester import APIRequester

class WebsiteUser(APIRequester):
    wait_time = between(2, 5)
    tasks = [APIRequester]
