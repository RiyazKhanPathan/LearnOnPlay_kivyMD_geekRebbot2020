from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from baseclass.classes import Banner


class SampleTutorialScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        self.app.title = "Sample Tutorials"

    def on_kv_post(self, base_widget):
        grid = self.ids["grid_banner"]
        operations = {"binary": "Binary To Decimal",
                      "count_vowels": "No.of Vowels",
                      "is_leap": "Check for Leap Year",
                      "is_palindrome": "Check for Plaindrome",
                      "inverse": "String Reverse"
                      }
        for operation, title in operations.items():
            banner = Banner(title=title, operation=operation)
            grid.add_widget(banner)
