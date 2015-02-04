# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import *


class Safhe1(Screen):
    def __init__(self, **kwargs):
        super(Safhe1, self).__init__(**kwargs)

        b = Button(size_hint = (None, None), text="go to page 2",
                   size=(100,50), pos=(200, 200), on_press=self.say_hello,
                   # background_normal="2.png", background_down="3.png"
        )
        b.name = "salam"
        self.add_widget(b)

    def say_hello(self, btn):
        print btn.name
        sm.current = "page2"


class Safhe2(Screen):
    def __init__(self, **kwargs):
        super(Safhe2, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 1, 1)
            Rectangle(size=(2000, 2000))

    def on_touch_down(self, touch):
        sm.current = "page1"


sm = ScreenManager(transition=FadeTransition())
p1 = Safhe1(name="page1")
p2 = Safhe2(name="page2")
sm.add_widget(p1)
sm.add_widget(p2)

class SampleApp(App):
    def build(self):
        self.title = "Screen Manager Example"
        return sm

if __name__ == '__main__':
    SampleApp().run()
