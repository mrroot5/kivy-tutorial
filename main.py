#!/usr/bin/env python3
# Py modules
from requests import get
# Kivy imports
import kivy
kivy.require('1.9.1') # replace with your current kivy version !
# Kivy modules
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import kivy.uix.gridlayout as gridl

class VideoGrid(gridl.GridLayout):
    def video_loaded(self):
        status_bar = self.parent.children[0].ids.status_text
        self.parent.change_status(status_bar, 'Video Loaded')

class ButtonsGrid(gridl.GridLayout):
    apiURL = 'https://api.github.com/'
    def do_request(self):
        r = get(self.apiURL + "events")
        return r.json()

    def forward(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.parent.change_status(status_bar, btn.text)
        self.parent.change_status(status_bar, self.do_request())

    def right(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.parent.change_status(status_bar, btn.text)
        # self.parent.change_status(status_bar, self.do_request())

    def back(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.parent.change_status(status_bar, btn.text)
        # self.parent.change_status(status_bar, self.do_request())

    def left(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.parent.change_status(status_bar, btn.text)
        # self.parent.change_status(status_bar, self.do_request())

class StatusBar(ScrollView):
    pass

class ContainerBox(BoxLayout):
    def change_status(self, element, new_text = 'Status'):
        element.text = new_text

class ButtonsGridApp(App):
    def build(self):
        return ContainerBox()

if __name__ == '__main__':
    ButtonsGridApp().run()
