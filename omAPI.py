import time 
import requests

#version and author
ver = 0.1
author = "thekip07"

#classes with all public omAPI methods
#https://omapi.ru/web
class Public(object):

    def __init__(self):
        pass

    def version(self):
        print(ver)

    def author(self):
        print(author)

    #get status
    def status(self):

        status = requests.get("https://omapi.ru")
        if (status.status_code != 200):
            print(status.status_code)
        else:
            print(200)      

    #public method of showing the user's followers count
    def get_followers_count(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowersCount/?username={user}&token=default")
        
        json_load = response.json()

        print(json_load["result"])

    #public method of showing the user's follows count
    def get_follows_count(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowsCount/?username={user}&token=default")
        
        json_load = response.json()

        print(json_load["result"])

    #public method of getting the user's avatar
    def get_avatar(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getAvatar/?username={user}&token=default")
        json_load = response.json()

        print(json_load["result"])

    #public method of getting the user's level
    def get_level(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getLevel/?username={user}&token=default")
        json_load = response.json()

        print(json_load["result"])

    #public method of getting the user's stream hotness
    def get_stream_hotness(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamHotness/?username={user}&token=default")
        json_load = response.json()

        print(json_load["result"])

    #public method of getting the user's stream status
    def is_live(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/isLive/?username={user}&token=default")
        json_load = response.json()

        print(json_load["result"])

    #public method of getting the user's verification status
    def is_verified(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/isVerified/?username={user}&token=default")
        json_load = response.json()

        print(json_load["result"])

#classes with all private omAPI methods (need a token)
#get a token here: https://omapi.ru/api
class Private(Public, object):
    
    def __init__(self, token):
        self.auth = token
    
    #private method of getting the user's followers list
    def get_followers_list(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowersList/?username={user}&token={self.auth}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    #private method of getting the user's follows list
    def get_follows_list(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getFollowsList/?username={user}&token={self.auth}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    #private method of getting the user's omlet creator status
    def is_has_omlet_creator(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/isHasOmletCreator/?username={user}&token={self.auth}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    #private method of getting the user's omlet plus status
    def is_has_omlet_plus(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/isHasOmletPlus/?username={user}&token={self.auth}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    #private method of getting the user's stream viewers
    def get_stream_viewers(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamViewers/?username={user}&token={self.auth}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    #private method of getting the user's stream session id
    def get_stream_sessionID(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamSessionID/?username={user}&token={self.auth}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

    #private method of getting the user's stream viewers list
    def get_stream_viewers_list(self, user, stime=None):

        if (stime == None):
            pass
        else:
            time.sleep(stime)

        response = requests.get(f"https://omapi.ru/api/user/getStreamViewersList/?username={user}&token={self.auth}")
        json_load = response.json()

        try:
            print(json_load["result"])
        except:
            raise TokenError("invalid token or account nickname")

#errors
class TokenError(Exception):
    pass

class ConnectionError(Exception):
    pass