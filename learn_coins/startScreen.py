# File name: startScreen.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.properties import (ObjectProperty, BooleanProperty, NumericProperty, ListProperty)







Window.size = (1440/3, 2560/3)
Builder.load_file('startScreen.kv')

class StartScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class GameScreen(Screen):
    pass




class ChangeScreens(ScreenManager):
    pass

class StartScreenApp(App):
    def build(self):
        return ChangeScreens()


if __name__ == '__main__':
    StartScreenApp().run()