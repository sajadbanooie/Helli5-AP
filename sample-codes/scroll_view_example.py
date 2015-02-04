# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import *


class Safhe1(Screen):
    def __init__(self, **kwargs):
        super(Safhe1, self).__init__(**kwargs)

        self.lay1 = ScrollView()

        self.lay2 = GridLayout(cols=1, padding="20dp", spacing="10dp", size_hint_y= None)
        self.lay2.bind(minimum_height=self.lay2.setter('height'))

        self.lay1.add_widget(self.lay2)
        self.add_widget(self.lay1)

        for i in range(50):
            b = Button(text=str(i+1), size_hint_y=None, height="80dp",)
            self.lay2.add_widget(b)


sm = ScreenManager(transition=FadeTransition())
p1 = Safhe1(name="page1")
sm.add_widget(p1)

class SampleApp(App):
    def build(self):
        self.title = "Scroll View Example"
        return sm

if __name__ == '__main__':
    SampleApp().run()
