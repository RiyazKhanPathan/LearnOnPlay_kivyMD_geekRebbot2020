from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from datetime import datetime


class SettingsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
     

    def on_pre_enter(self, *args):
        self.app.title = "Settings"

    def change_mode(self, checkbox, value):
        if value:
            self.app.theme_cls.theme_style = "Light"
        else:
            self.app.theme_cls.theme_style = "Dark"

    