from kivymd.app import MDApp
from kivy.lang import Builder
from functools import partial
import os

import sqlite3


# Screen Classes
from baseclass.sampleTutorialScreen import SampleTutorialScreen
from baseclass.settingsscreen import SettingsScreen
from baseclass.classes import ListIcon
from baseclass.loginScreen import LoginScreen
from baseclass.homeScreen import HomeScreen
from level.level import Level


class MyApp(MDApp):
    def __init__(self, **kw):
        super().__init__(**kw)

    
       
        self.list_screen = {
            LoginScreen: ("loginScreen","Login","login"),

            HomeScreen:("homeScreen","Home","home"),
            
            SampleTutorialScreen: ("sampleTutorialScreen", "Sample Tutorials", "file-code"),
            SettingsScreen: ("settingsscreen", "Change Theme", "theme-light-dark"),
            Level: ("level", "Level", ""),
        }
        
      
    def build(self):
        self.title = "Learn ON Play"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')

    def on_start(self):
        for screen, details in self.list_screen.items():
            kivyFileName, text, icon = details
            Builder.load_file(f"kv/{kivyFileName}.kv")
            self.root.ids.screen_manager.add_widget(screen(name=kivyFileName))

            # Hiding from NavList
            if kivyFileName!="level":
                self.root.ids.nav_list.add_widget(ListIcon(text=text, icon=icon,on_release=partial(self.button_list_actions,text,kivyFileName)))
  

        
    def button_list_actions(self, screenTitle, currentScreen):
        self.title = screenTitle
        self.root.ids.screen_manager.current = currentScreen
        self.root.ids.nav_drawer.set_state()


if __name__ in ('__main__'):
    MyApp().run()
