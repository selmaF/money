from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.graphics import Line, Color
from kivy.properties import (ObjectProperty, BooleanProperty,NumericProperty)
from random import random


class Coin(Widget):
    counter = NumericProperty()



class Game(RelativeLayout):
    counter = NumericProperty(0)


    def generate_random_coins(self):
        for i in range(12):
            self.counter += 1
            ball = Coin()
            print self.size
            center = int(random()*self.size[0]), int(random()*self.size[1])
            print center
            ball.center = center
            ball.counter = self.counter
            self.add_widget(ball)



    def on_touch_down(self,touch):
        #if touch.x<100 and touch.y<100: why ?
            #return super(Ex46, self).on_touch_down(touch) why ?
        print touch.x, touch.y

        #for child in self.children:
           # print child.ids['id01'].text




    def on_touch_up(self,touch):
        self.counter += 1
        ball = Coin()
        ball.center = touch.pos
        ball.counter = self.counter
        print ball.counter
        print touch.x, touch.y
        self.add_widget(ball)



class CoinApp(App):
    def build(self):
        self.title = 'Widget Selection'
        game = Game()
        game.generate_random_coins()
        return game

if __name__=='__main__':
    CoinApp().run()