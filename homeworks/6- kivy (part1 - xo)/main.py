# -*- coding: utf-8 -*-
import arabic_reshaper
import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivy.graphics import *
from kivy.app import *
from kivy.uix.actionbar import ActionButton
from kivy.uix.boxlayout import *
from kivy.clock import *
from kivy.core.window import Window
from kivy.uix.button import *
from Farsi import get
from kivy.properties import StringProperty
from kivy.uix.label import Label
Builder.load_file('main.kv')
setings = {'sound':'high'}
global setings
class Game:
    sounds = []
    def __init__(self):
        self.turn = 1
    map = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    def next(self,x,y):
        self.map[x][y] = self.turn
        self.turn = -self.turn

    def check(self,x,y):
        if self.map[x][y] == 0:
            return True
        else:
            return False

    def reset(self):
        self.map = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]

class SoundIcon(ActionButton):
    def __init__(self,**kw):
        super(SoundIcon,self).__init__(**kw)
        self.icon = 'atlas://data/images/defaulttheme/audio-volume-'+setings['sound']
        print 'atlas://data/images/defaulttheme/audio-volume-'+setings['sound']
        Clock.schedule_interval(self.callback, 0.5)
    def on_press(self):
        if self.icon=='atlas://data/images/defaulttheme/audio-volume-high':
            self.icon = 'atlas://data/images/defaulttheme/audio-volume-muted'
            setings['sound'] = 'muted'
        else:
            self.icon = 'atlas://data/images/defaulttheme/audio-volume-high'
            setings['sound'] = 'high'
    def callback(self,i):
        self.icon = 'atlas://data/images/defaulttheme/audio-volume-'+setings['sound']
class GameGUI(Screen):
    def __init__(self,**kw):
        super(GameGUI,self).__init__(**kw)
        self.game = Game()
        self.build()
    def goback(self):
        sm.current = 'main'

    def build(self):

        with self.canvas.before:
            for i in range(1,3):
                Line(points=[Window.width/3*i,0 ,Window.width/3*i, Window.height-50], width=5)
            for i in range(1,3):
                Line(points=[0,Window.height/3*i ,Window.width, Window.height/3*i], width=5)
    def on_touch_down(self, touch):
        super(GameGUI,self).on_touch_down(touch)
        x = Window.width/3
        y = Window.height/3
        for i in range(3):
            for j in range(3):
                if x*i<touch.x<x*(i+1) and y*j<touch.y<y*(j+1):
                    self.draw(self.game.turn,x*i+x/2-50,y*j+1/2+50,i,j)
                    break

    def draw(self,turn,x,y,i,j):

        if self.game.check(i,j):
            with self.canvas.before:
                if turn==-1:
                    Ellipse(size=(100,100),pos=(x,y))
                if turn==1:
                    print 1
                    x = x + 50
                    y = y + 50
                    Line(points=[x-50,y-50,x+50,y+50],width=10)
                    Line(points=[x-50,y+50,x+50,y-50],width=10)

            self.game.next(i,j)
            s = self.check()
            if s==1:
                self.reset()
                sm.add_widget(SGUI('x',name='status'))
                sm.current = 'status'
            if s==-1:
                self.reset()
                sm.add_widget(SGUI('y',name='status'))
                sm.current = 'status'
        print self.game.map
    def check(self):
        for i in range(3):
            if self.game.map[i][0]==self.game.map[i][1]==self.game.map[i][2]==1:
                return -1
            if self.game.map[i][0]==self.game.map[i][1]==self.game.map[i][2]==-1:
                return 1
        return 0
    def reset(self):
        self.parent.canvas.clear()
        self.game.reset()
        self.build()

class GUI(Screen):
    def __init__(self,**kw):
        super(GUI,self).__init__(**kw)

    def startgame(self):
        sm.current = 'game'

class SGUI(Screen):
    def __init__(self,x,**kw):
        super(SGUI,self).__init__(**kw)
        self.add_widget(Label(text=x))

sm = ScreenManager()
sm.add_widget(GUI(name='main'))
sm.add_widget(GameGUI(name='game'))

sm.current = 'main'

class XOApp(App):
    def build(self):
        return sm

if __name__=='__main__':
    XOApp().run()