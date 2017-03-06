#!/usr/bin/env python3
# mygrid.py
# Py modules
import requests
# Kivy imports
import kivy
kivy.require('1.9.1') # replace with your current kivy version !
# Kivy modules
from kivy.app import App
import kivy.uix.gridlayout as gridl
# from kivy.properties import ObjectProperty
# from kivy.uix.label import Label
# from kivy.uix.button import Button

class ButtonsGrid(gridl.GridLayout):
    apiURL = 'https://api.github.com/'
    def forward(self, btn):
        print(btn.text)
        # r = requests.get(self.apiURL + "events")
        # response = r.json()
        # print(response)
    def right(self, btn):
        print(btn.text)
        # r = requests.get(self.apiURL + "events")
        # response = r.json()
        # print(response)
    def back(self, btn):
        print(btn.text)
        # r = requests.get(self.apiURL + "events")
        # response = r.json()
        # print(response)
    def left(self, btn):
        print(btn.text)
        # r = requests.get(self.apiURL + "events")
        # response = r.json()
        # print(response)

class ButtonsGridApp(App):
    def build(self):
        return ButtonsGrid()

if __name__ == '__main__':
    ButtonsGridApp().run()
