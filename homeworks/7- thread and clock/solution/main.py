from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.clock import Clock


class GUI(Widget):
    def __init__(self, **kw):
        super(GUI, self).__init__(**kw)
        self.count = 1
        self.re = 1
        with self.canvas:
            self.rect = Rectangle(source='images/13.png', size=self.size)
        Clock.schedule_interval(self.move, .20)

    def move(self, dt):
        print dt
        if self.count == 6:
            self.count = 1
        if self.re == 1:
            self.rect.source = "images/"+str(self.count)+'.png'
            self.rect.pos = (self.rect.pos[0]+10, self.rect.pos[1])
        if self.re == 2:
            self.rect.source = "images/"+str(self.count+7)+'.png'
            self.rect.pos = (self.rect.pos[0]-10, self.rect.pos[1])
        if self.rect.pos[0] + self.rect.size[1] > Window.width:
            self.re = 2
        if 0 > self.rect.pos[0]:
            self.re = 1
        self.count += 1



class AdamakApp(App):
    def build(self):
        return GUI()

if __name__ == '__main__':
    AdamakApp().run()
