#!/usr/bin/env python3
# Py modules
import requests
# Kivy imports
import kivy
kivy.require('1.9.1') # replace with your current kivy version !
# Kivy modules
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy.uix.gridlayout as gridl

class VideoGrid(gridl.GridLayout):
    pass
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

class ContainerBox(BoxLayout):
    pass

class ButtonsGridApp(App):
    def build(self):
        return ContainerBox()

if __name__ == '__main__':
    ButtonsGridApp().run()
