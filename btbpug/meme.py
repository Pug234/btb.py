import requests

class meme:
    def __init__(self):
        self.r = requests.get(f"https://api.bytestobits.dev/meme/").json()

    @property
    def title(self):
        return self.r['title']

    @property
    def link(self):
        return self.r['link']

    @property
    def image(self):
        return self.r['url']

    @property
    def subreddit(self):
        return self.r['subreddit']

    @property
    def image(self):
        return self.r['url']

    @property
    def comments(self):
        return self.r['comments']

    @property
    def score(self):
        return (self.r['upvotes'], self.r['downvotes'])

    def raw(self):
        return self.r
