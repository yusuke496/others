# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime

#Window sizeの設定
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(padding=30, orientation='vertical')

        self.label=Label(text="I")
        self.add_widget(self.label)

        #Clock.schedule_interval(self.TimerCallback, 1.0)
        self.label=Label(text="J")
        self.add_widget(self.label)

        self.label=Label(text="I+J")
        self.add_widget(self.label)

        #self.textinput = TextInput(text='Hello world', multiline=False)
        #self.add_widget(self.textinput)

    def TimerCallback(self,dt):
        time=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.textinput.text=time

class TestApp(App):
    def build(self):
        self.root = RootWidget()
        self.title = 'magic F'
        return self.root

TestApp().run()
