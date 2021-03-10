import requests

class reddit:
    def __init__(self, subreddit:str, limit:int=1):

        self.r = requests.get(f"https://api.bytestobits.dev/reddit/?subreddit={subreddit}&limit={limit}").json()



        if self.r == {"message": "Internal Server Error"}:
            raise Exception(f"Subreddit {subreddit} not found")

    def raw(self):
        return self.r

    def post(self, number:int):
        return self.r[number]
