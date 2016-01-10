from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import  ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.clock import Clock
import time

class ClockLayout(BoxLayout):
    time_prop = ObjectProperty()




class ClockApp(App):
    sw_started = False
    sw_seconds = 0


    def on_start(self):
        Clock.schedule_interval(self.update, 0.016)

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        self.root.ids.time.text = time.strftime('[b]%H[/b]:%M:%S')#strftime from time not in the book

        m, s = divmod(self.sw_seconds,60)
        self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %(int(m), int(s), int(s * 100 % 100)))


    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0




if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    #LabelBase.register(name='Roboto',fn_regular='Roboto-Thin.ttf',fn_bold='Roboto-Medium.ttf')
    ClockApp().run()

