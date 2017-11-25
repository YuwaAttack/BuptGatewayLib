#coding:utf-8
import requests
import json
import optparse
import urllib

class LoginException(Exception):
    pass

class LoginRequest:
    def __init__(self, endpoint, **identity):
        self.info = {"endpoint":endpoint}
        self.process_identity(identity)

    def process_identity(self, identity):
        self.info["username"] = identity["username"]
        self.info["password"] = identity["password"]

    def login(self):
        ret = requests.post(url=self.info["endpoint"], headers=self.make_headers(), cookies=self.make_cookies(), data=urllib.urlencode(self.make_form()))
        if not self.check_login_result(ret.text):
            raise LoginException("[Unknown error]")

    def check_login_result(self, ret_text):
        if "You have successfully logged into our system" in ret_text:
            return True
        return False 

    def check_login(self):
        ret = requests.get(url=self.info["endpoint"])
        if "Logout" in ret.text:
            return True
        return False

    def make_headers(self):
        ret = {
            "Content-Type":"application/x-www-form-urlencoded",
            "Referer" : self.info["endpoint"],
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Connection" : "keep-alive",
            "Origin" : self.info["endpoint"],
            "Cache-Control" : "max-age=0",
            "Upgrade-Insecure-Request" : "1",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",

        }
        return ret

    def make_cookies(self):
        ret = {
            "myusername" : self.info["username"],
            "username" : self.info["username"],
            "smartdot" : self.info["password"],
        }
        return ret

    def make_form(self):
        ret = {
            "DDDDD" : self.info["username"],
            "upass" : self.info["password"],
            "0MKKey" : "",
        }
        return ret

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-e", "--endpoint", dest="endpoint", help="School login endpoint")
    parser.add_option("-u", "--username", dest="username", help="School network user number")
    parser.add_option("-p", "--password", dest="password", help="School network user password")
    options, args =  parser.parse_args()

    LR = LoginRequest(options.endpoint, username=options.username, password=options.password)
    if not LR.check_login():
        try:
            LR.login()
            print "Login success! Enjoy~"
        except Exception, e:
            print "Login error!", str(e)
    
    