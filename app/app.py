from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager


class MainWidget(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class HomePage(Screen):
    pass


class MainApp(MDApp):
    
    def build(self):
        return MainWidget()
    

MainApp().run()  