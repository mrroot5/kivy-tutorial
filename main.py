#!/usr/bin/env python3
# mygrid.py
import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
import kivy.uix.gridlayout as gridl
# from kivy.uix.label import Label
# from kivy.uix.button import Button

class ButtonsGrid(gridl.GridLayout):
    pass

class ButtonsGridApp(App):
    def clicked(instance):
        print('The button <%s> is being pressed' % instance.text)

    def build(self):
        return ButtonsGrid()

if __name__ == '__main__':
    ButtonsGridApp().run()
