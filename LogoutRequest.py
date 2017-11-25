#coding:utf-8
import requests

class LogoutRequest:
    def __init__(self, endpoint):
        self.info = {"endpoint":endpoint}

    def logout(self):
        ret = requests.get(url= "%s/F.htm" % self.info["endpoint"])
    

