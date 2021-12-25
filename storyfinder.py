import requests
from random import randint

endpoint = 'https://api.npoint.io/c58548dec79f3ab6f810/'


class Story:

    def __init__(self):

        self.story = self.story_shop()

    def story_shop(self):
        story = requests.get(url=f"{endpoint}{randint(1, 7)}").json()
        return story
