# coding:utf-8

class Platform:
    '''
    各个解码平台的基类，包括的功能有：
    登录，
    获取区域，
    '''

    def __init__(self):
        self.token = ""

    def login(self, account, password):
        '''
        登录短信平台
        :param account: 账号 
        :param password:  密码
        :return: 返回登录后的结果
        '''
        pass

    def getArea(self):
        '''
        获取区域
        :return: 返回区域信息 比如城市名字 
        '''
        pass

    def getPhoneNumber(self, **args):
        '''
        获取手机号
        :param args: 手机号参数 
        :return: 返回列表，这里会进行处理，返回至少0个手机号。
        '''
        pass

    def getPhoneMessage(self, itemId, phoneNum):
        '''
        获取手机号信息
        :param itemId: 项目ID 
        :param phoneNum: 手机号
        :return: 不作处理，只返回平台自己的返回数据。
        '''
        pass

    def sendPhoneMessage(self,itemId,phoneNum,msg):
        '''
        向特定手机号发送消息
        :param itemId: 项目id
        :param phoneNum: 手机号
        :param msg: 消息
        :return: 返回是否成功
        '''
        pass




