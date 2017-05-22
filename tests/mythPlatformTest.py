# coding:utf-8

import unittest
from Platform.mythPlatform import mythPlatform

class mythPlatformTest(unittest.TestCase):

    def setUp(self):
        self.mythPlat = mythPlatform()

    def testLogin(self):
        ret = self.mythPlat.login("liyunf81","ilvwmfev2012")
        self.assertTrue(ret,"执行登录失败")

    def testNullAccountLogin(self):
        ret = self.mythPlat.login("","liyun123")
        self.assertFalse(ret,"账号为空时，登录应该失败")

    def testGetArea(self):
        ret = self.mythPlat.getArea()

    def testGetPhoneNum(self):
        ret = self.mythPlat.login("liyunf81", "ilvwmfev2012")
        if ret:
            param = {"Count":1,"ItemId":38}
            ret = self.mythPlat.getPhoneNumber(param)

    def testGetPhoneMessage(self):
        ret = self.mythPlat.login("liyunf81", "ilvwmfev2012")
        if ret:
            param = {"Count": 1, "ItemId": 38}
            ret = self.mythPlat.getPhoneNumber(param)
            for phoneNumber in ret:
                retMsg = self.mythPlat.getPhoneMessage(38,phoneNumber)
                print(retMsg)

