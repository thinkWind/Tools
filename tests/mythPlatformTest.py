# coding:utf-8

import unittest
from Platform.mythPlatform import mythPlatform

class mythPlatformTest(unittest.TestCase):

    def setUp(self):
        self.mythPlat = mythPlatform()

    def testLogin(self):
        ret = self.mythPlat.login("liyunf81","ilvwmfev2012")
        self.assertTrue(ret,"执行登录失败")
        print(self.mythPlat.token)

    def testNullAccountLogin(self):
        ret = self.mythPlat.login("","liyun123")
        self.assertFalse(ret,"账号为空时，登录应该失败")

    def testGetArea(self):
        ret = self.mythPlat.getArea()

