from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem,ThreeLineAvatarListItem
from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty
import requests


class ContentNavigationDrawer(BoxLayout):
    pass


class HomePage(Screen):
    pass


class AboutPage(Screen):
    pass


class WeatherList(ThreeLineAvatarListItem):
    source=StringProperty('string')


class MainWidget(BoxLayout):
    pass


class MainApp(MDApp):
    
    def build(self):
        return MainWidget()
    
    def on_start(self):
        value='12,32,15,37,17'
        hlist=self.root.ids.home_list
        response=requests.get('https://api.openweathermap.org/data/2.5/box/city?bbox='+value+'&appid=ecd2457b5bc4ae41ec0b12d3cf7f300f')
        output=response.json()
        response_list=output['list']

        for i in response_list:
            name=i['name']
            temp=str(i['main']['temp'])
            temp_max=str(i['main']['temp_max'])
            temp_min=str(i['main']['temp_min'])
            weather_desc=i['weather'][0]['description']

            icon=''

            if weather_desc=='clear sky':
                icon='data/sunny.png'
            elif weather_desc=='few clouds':
                icon='data/cloudy.png'
            elif weather_desc=='scattered clouds':
                icon='data/scattered-clouds.png'
            elif weather_desc=='broken clouds':
                icon='data/broken-clouds.png'
            elif weather_desc=='shower rain':
                icon='data/shower-rain.png'
            elif weather_desc=='rain':
                icon='data/rain.png'
            elif weather_desc=='thunderstorm':
                icon='data/thunderstorm.png'
            elif weather_desc=='snow':
                icon='data/snowy.png'
            elif weather_desc=='mist':
                icon='data/misty.png'
            else:
                icon='data/sunny.png'

            i=WeatherList(text=name,secondary_text=temp,tertiary_text=weather_desc,source=icon)
            hlist.add_widget(i)
        

MainApp().run()  