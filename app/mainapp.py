from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.theming import ThemableBehavior
import requests


class ContentNavigationDrawer(BoxLayout):
    pass


class HomePage(Screen):
    pass


class AboutPage(Screen):
    pass


class MainWidget(BoxLayout):
    pass


class MainApp(MDApp):
    
    def build(self):
        return MainWidget()
    
    def on_start(self):
        value=12,32,15,37,17
        hlist=self.root.ids.home_list
        response=requests.get('https://api.openweathermap.org/data/2.5/box/city?bbox='+value+'&appid=ecd2457b5bc4ae41ec0b12d3cf7f300f')
    

MainApp().run()  