import requests
import requests.auth

class RedditBot:
    
    def __init__(self):
        pass      

    def get_auth(self):
        client_auth = requests.auth.HTTPBasicAuth('gqw0ovWDd5ZUGQ','TFu4FzYnN4k-DPG5aZDIbpcRHY8')
        post_data = {'grant_type':'password', 'username': 'insomniacphysicist', 'password':'ibmGqaRL776H'}
        headers = {"User-Agent": "graphing-upvotes/0.1 by insomniacphysicist"}
        resp = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
        self.oauth = resp.json()["access_token"]

    def make_api_request(self, url):
        headers = {"Authorization": f"bearer {self.oauth}", "User-Agent":"graphing-upvotes/0.1 by insomniacphysicist" }
        resp = requests.get(f"https://oauth.reddit.com/api{url}", headers=headers)
        return resp.json()


    def get_self(self):
        return self.make_request("/v1/me")

    def get_sub_posts(self, sub):
        # https://www.reddit.com/r/TellMeAFact/top/.json?t=all 
