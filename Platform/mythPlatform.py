# coding:utf-8

import requests
from .Platform import Platform

class mythPlatform(Platform):

    baseUrl = "http://api.shjmpt.com:9002/"

    def login(self, account, password):
        if(not account):
            return False
        if(not password):
            return False

        loginUrl = self.baseUrl + "pubApi/uLogin?"
        req = requests.get(loginUrl,{"uName":account,
                                         "pWord":password,
                                         "Developer":"Yc1hQ0RmBLMzxKHv4N%2f5IA%3d%3d"})
        content = req.content
        cstr = str(content, encoding="utf-8")
        if(cstr.find("False") == -1):
            userInfo = cstr.split("&")
            if(len(userInfo) > 0):
                self.token = userInfo[0]
                return True
        return False

    def getArea(self):
        reqUrl = self.baseUrl + "uGetArea?"
        req = requests.get(reqUrl)
        content = str(req.content,encoding="utf-8")
        return content.split("\n")


    def getPhoneNumber(self, args):
        reqUrl = self.baseUrl + "pubApi/GetPhone"
        args["token"] = self.token
        req = requests.get(reqUrl,args)
        content = str(req.content,encoding="utf-8")
        retList = content.split(";")
        retLen = len(retList)
        if retLen > 0:
            retList.pop()
        return retList

    def getPhoneMessage(self, itemId, phoneNum):
        reqURL = self.baseUrl + "pubApi/GMessage"
        req = requests.get(reqURL,{"token":self.token,
                                   "ItemId":itemId,
                                   "Phone":phoneNum})
        content = str(req.content,encoding="utf-8")
        return content
