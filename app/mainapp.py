from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.theming import ThemableBehavior



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
    

MainApp().run()  