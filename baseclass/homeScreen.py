from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp


from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextFieldRect
from kivy.uix.floatlayout import FloatLayout


class Banner(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.app = MDApp.get_running_app()

        self.operation = kwargs["operation"]        

        self.button = MDRectangleFlatButton(on_release=self.operations,text=kwargs["title"],
                                   pos_hint={"center_x": .5, "center_y": .4}, size_hint=(.8, .3))
  
        self.add_widget(self.button)

    def operations(self,widget):
        if self.operation == 'level_1':
            self.app.title="Getting Started With C"
            self.app.root.ids.screen_manager.current="level"


class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        self.app.title = "Home"

    def on_kv_post(self, base_widget):
        grid = self.ids["grid_banner"]
     
        
        operations = {"level_1": "Getting Started with C",
                      "level_2": "Flow Control",
                      "level_3": "Functions",
                      "level_4": "Arrays",
                      "level_5": "String",
                      "level_6": "Pointers",
                      "level_7": "Structure and Unions",

                      }
        for operation, title in operations.items():
            banner = Banner(title=title, operation=operation)
            grid.add_widget(banner)

    
        