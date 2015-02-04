import os
import kivy
import random
kivy.require('1.8.0')

icons = os.listdir(os.path.dirname(__file__) + '\icons')
icons.remove('Thumbs.db')
hidden = 'hidden.png'

background = 'bg.jpg'

from kivy.uix.screenmanager import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.graphics import *
from kivy.core.window import Window
from kivy.clock import Clock


class Animals(Button):
    def __init__(self, animal):
        super(Animals, self).__init__(background_normal=animal)
        self.animal = animal
        self.h = False
        self.replace = False

    def replacing(self):
        self.background_normal = hidden
        self.replace = True

    def on_release(self):
        if self.replace:
            if self.h:
                self.background_normal = hidden
                self.h = False
                self.replace = True
            if not self.h:
                self.background_normal = self.animal
                self.h = True
                self.replace = False
                self.parent.parent.choose.append(self)

    def release(self):
        self.background_normal = hidden
        self.replace = True


class screen(Screen):
    def __init__(self, **kwargs):
        super(screen, self).__init__(**kwargs)
        self.Cards = []
        self.choose = []
        with self.canvas:
            Rectangle(source=background, size=(Window.width, Window.height))
        self.Grid = GridLayout(rows=5, cols=5, spacing=10)
        self.add_widget(self.Grid)
        self.draw_map()
        self.Timer = Label(text='0', size_hint_x=None, size_hint_y=None)
        self.Missed = Label(text='0', size_hint_x=None, size_hint_y=None)
        self.z = BoxLayout(size_hint_x=None, size_hint_y=None)
        self.z.add_widget(self.Timer)
        self.z.add_widget(self.Missed)
        self.Grid.add_widget(self.z)
        Clock.schedule_interval(self.recorder2, 1)

    def draw_map(self):
        myanimals = [0] * 24
        r = [looper for looper in range(24)]
        for looper in range(12):
            rand1 = random.choice(r)
            r.remove(rand1)
            rand2 = random.choice(r)
            r.remove(rand2)
            i_rand = random.choice(icons)
            myanimals[rand1] = Animals('icons/' + i_rand)
            myanimals[rand2] = Animals('icons/' + i_rand)
        for anim in myanimals:
            self.Cards.append(anim)
            self.Grid.add_widget(anim)

    def recorder2(self, dt):
        self.Timer.text = str(int(self.Timer.text) + 1)
        if int(self.Timer.text) == 10:
            for c in self.Cards:
                c.replacing()
            Clock.unschedule(self.recorder2)
            Clock.schedule_interval(self.pointer, .1)
            self.Timer.text = '0'
            Clock.schedule_interval(self.t, 1)

    def pointer(self, dt):
        if len(self.choose) == 2:
            if not self.choose[0].animal == self.choose[1].animal:
                self.choose[0].release()
                self.choose[1].release()
                self.Missed.text = str(int(self.Missed.text) + 1)
            else:
                self.choose[0].changed = False
                self.choose[1].changed = False
            self.choose = []

    def t(self, dt):
        self.Timer.text = str(int(self.Timer.text) + 1)


Myscreen = ScreenManager()
Myscreen.add_widget(screen(name='main'))
Myscreen.current = 'main'


class MemoryApp(App):
    def build(self):
        return Myscreen


if __name__ == '__main__':
    MemoryApp().run()