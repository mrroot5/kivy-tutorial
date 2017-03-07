#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        f = BoxLayout(orientation='vertical')
        s = Scatter()
        l = Label(text='Hello World!!',
                  font_size=150)
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == '__main__':
    MyApp().run()
