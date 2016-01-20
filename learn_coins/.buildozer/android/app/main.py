# File name: main.py

# kivy imports

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line, Color
from kivy.properties import (ObjectProperty, BooleanProperty, NumericProperty, ListProperty)
from random import random, randint
from kivy.vector import Vector as Vec
from kivy.clock import Clock
from kivy.utils import platform

#load Kv files

Builder.load_file('layout_presets.kv')
Builder.load_file('settings_screen.kv')
Builder.load_file('start_screen.kv')
Builder.load_file('game_screen.kv')

#imported own classes

from start_screen import StartScreen
from settings_screen import SettingsScreen
from game_screen import GameScreen


#Window.size = (1440/3, 2560/3)





class ChangeScreens(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        run = ChangeScreens()
        Clock.schedule_interval(run.get_screen('GameScreen').update, 1.0/60)
        return run


if __name__ == '__main__':
    MainApp().run()