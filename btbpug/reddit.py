import requests

class reddit:
    def __init__(self, token, subreddit:str, limit:int=1):
        self.r = requests.get(f"https://api.bytestobits.dev/reddit/?subreddit={subreddit}&limit={limit}", headers=token).json()

        if self.r == {"message": "Internal Server Error"}:
            raise Exception(f"Subreddit {subreddit} not found")

    def raw(self):
        return self.r

    def post(self, index:int):
        return self.r[index]

    
