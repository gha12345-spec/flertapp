from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.base import runTouchApp
from kivy.uix.button import Button







class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")
class Myapp(App):



    def build(self):
        self.icon = 'flert 3.png'
        self.title = 'Flert!!'

        return kv

if __name__ == "__main__":
    Myapp().run()

