# coding:utf-8

from kivy.app import App
from PlatformView import PlatformView

class QiaoHuApp(App):
    '''
    巧虎app 对象
    '''
    def build(self):
        return PlatformView()

if __name__ == '__main__':
    QiaoHuApp().run()

