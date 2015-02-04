# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class Safhe1(Screen):
    def __init__(self, **kwargs):
        super(Safhe1, self).__init__(**kwargs)

        g1 = GridLayout(rows=10, cols=10, spacing="5dp", padding="10dp")
        for i in range(1, 11):
            for j in range(1, 11):
                b = Button(text=str(i*j), on_press=self.say_hello)
                g1.add_widget(b)

        g2 = GridLayout(rows=10, cols=3, spacing="5dp", padding="10dp", size_hint_x=.3)
        for i in range(1, 11):
            for j in range(1, 4):
                b = Button(text=str(i*j), on_press=self.say_hello)
                g2.add_widget(b)

        b = BoxLayout(orientation='horizontal', spacing="5dp", padding="10dp")
        b.add_widget(g1)
        b.add_widget(g2)
        self.add_widget(b)

    def say_hello(self, btn):
        print btn.text

sm = ScreenManager(transition=FadeTransition())
p1 = Safhe1(name="page1")
sm.add_widget(p1)

class SampleApp(App):
    def build(self):
        self.title = "Grid Layout Example"
        return sm

if __name__ == '__main__':
    SampleApp().run()
