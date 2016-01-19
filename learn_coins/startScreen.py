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
    def printhola(self):
        print 'hola'


class GameScreen(Screen):
    settings_game_difficulty = NumericProperty
    settings_audio_sounfx = BooleanProperty
    settings_audio_music = BooleanProperty
    settings_mobile_vibration = BooleanProperty
    settings_mobile_gyro = BooleanProperty


    def on_enter(self):
        settings_game_difficulty = self.parent.get_screen('SettingsScreen').ids['sl_diff'].value
        self.ids.gameDiff.text = ('game difficulty:\n {0}'.format(settings_game_difficulty))

        settings_audio_sounfx = self.parent.get_screen('SettingsScreen').ids['soundfx'].active
        settings_audio_music = self.parent.get_screen('SettingsScreen').ids['music'].active

        self.ids.gameAudio.text = 'gameAudio:\n soundfx = {0}\n music = {1}'.format(settings_audio_sounfx, settings_audio_music)

        settings_mobile_vibration = self.parent.get_screen('SettingsScreen').ids['vibration'].active
        settings_mobile_gyro = self.parent.get_screen('SettingsScreen').ids['gyro'].active

        self.ids.gameMobile.text = 'gameMobile:\n vibration = {0}\n gyro = {1}'.format(settings_mobile_vibration, settings_mobile_gyro)



class ChangeScreens(ScreenManager):
    pass

class StartScreenApp(App):
    def build(self):
        return ChangeScreens()


if __name__ == '__main__':
    StartScreenApp().run()