# ex46.py

from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.graphics import Line, Color
from kivy.properties import (ObjectProperty, BooleanProperty,NumericProperty)

class Ball(Widget):
    counter = NumericProperty()

class Ex46(RelativeLayout):
    counter = NumericProperty(0)
    selected = ObjectProperty(None)
    sel = BooleanProperty(False)
    
    def on_touch_down(self,touch):
        if touch.x<100 and touch.y<100:
            return super(Ex46, self).on_touch_down(touch)
        if self.select.state == 'down':
            for child in self.children:
                if child.collide_point(*touch.pos):
                    self.selected = child
                    self.sel = True
                    with self.canvas:
                        Color(0,0,0)
                        touch.ud['line'] = Line(rectangle=(child.x-5,child.y-5,child.width+10,child.height+10), dash_length=5, dash_offset=2)
                    break

    def on_touch_move(self,touch):
        if self.select.state == 'down' and self.sel == True:
            self.canvas.remove(touch.ud['line'])
            child = self.selected
            child.center = touch.pos
            with self.canvas:
                touch.ud['line']=Line(rectangle=(child.x-5,child.y-5,child.width+10,child.height+10),width=1, dash_length=5,dash_offset=2)

    def on_touch_up(self,touch):
        if self.select.state == 'down' and self.sel == True:
            self.canvas.remove(touch.ud['line'])
            self.sel = False
        if touch.x<100 and touch.y<100:
            return super(Ex46, self).on_touch_down(touch)
        if self.draw.state == 'down':
            self.counter += 1
            ball = Ball()
            ball.center = touch.pos
            ball.counter = self.counter
            self.add_widget(ball)
       
class Ex46App(App):
    def build(self):
        self.title = 'Widget Selection'
        return Ex46()

if __name__=='__main__':
    Ex46App().run()