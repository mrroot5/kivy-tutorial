#!/usr/bin/env python3
# Py modules
from requests import get
# import iconfonts
# Kivy imports
import kivy
kivy.require('1.9.1') # replace with your current kivy version !
# Kivy modules
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import kivy.uix.gridlayout as gridl

class VideoGrid(gridl.GridLayout):
    pass
class ButtonsGrid(gridl.GridLayout):
    apiURL = 'https://api.github.com/'
    def do_request(self):
        r = get(self.apiURL + "events")
        response = r.json()
        print(response)

    def change_status(self, element, new_text = 'Status'):
        element.text = new_text

    def forward(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.change_status(status_bar, btn.text)
        # self.do_request()

    def right(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.change_status(status_bar, btn.text)
        # self.do_request()

    def back(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.change_status(status_bar, btn.text)
        # self.do_request()

    def left(self, btn):
        status_bar = self.parent.children[0].ids.status_text
        self.change_status(status_bar, btn.text)
        # self.do_request()

class StatusBar(ScrollView):
    pass

class ContainerBox(BoxLayout):
    pass

class ButtonsGridApp(App):
    def build(self):
        # iconfonts.register('default_font', 'iconfont_sample.ttf', 'iconfont_sample.fontd')
        return ContainerBox()

if __name__ == '__main__':
    ButtonsGridApp().run()
