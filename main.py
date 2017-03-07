#!/usr/bin/env python3
# Py modules
from requests import get
# Kivy imports
import kivy
 # replace with your current kivy version !
kivy.require('1.9.1')
# Kivy modules
from kivy.app import App
import kivy.uix.gridlayout as gridl

class ButtonsGrid(gridl.GridLayout):
    pass

class ButtonsGridApp(App):
    def build(self):
        return ButtonsGrid()

if __name__ == '__main__':
    ButtonsGridApp().run()
