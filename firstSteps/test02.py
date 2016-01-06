from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter

from kivy.clock import Clock
import time


class Coin(Widget):
    pass


class CoinGame(Widget):
    pass


class Learn_CoinApp(App):
    def build(self):
        return CoinGame()


if __name__ == '__main__':
    Learn_CoinApp().run()



















__author__ = 'dev'
