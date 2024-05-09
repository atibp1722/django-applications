from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout


class MainWidget(BoxLayout):
    pass


class MainApp(MDApp):
    
    def build(self):
        return MainWidget()
    

MainApp().run()  