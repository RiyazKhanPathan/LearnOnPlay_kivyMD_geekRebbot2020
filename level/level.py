from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
import os

class Banner(FloatLayout):
   def __init__(self, **kwargs):
      super().__init__()     
      self.info=kwargs["info"]
      self.operation=kwargs["operation"]
      
      self.button = MDRectangleFlatButton(on_release=self.operations,text=self.operation, pos_hint={"center_x": .5, "center_y": 1}, size_hint=(.8, .3))
      self.add_widget(self.button)
  
   def operations(self,widget):

      self.dialog = MDDialog(text=self.info,radius=[20, 7, 20, 7],)        
      self.dialog.open()



class Level(Screen):

   def __init__(self, **kw):
      super().__init__(**kw)
      self.app = MDApp.get_running_app()
   
   def play(self):
      os.chdir('./resources')
      os.startfile("C_Structure.mp4")
     

   def on_kv_post(self, base_widget):
      grid = self.ids["levels"]
   
      
      operations = {"Identifiers & Keywords":"Keywords:\n\n These are predefined, reserved words used in programming that have special meanings to the compiler they cannot be used as an identifier(VariableName) \n\nIdentifiers:\n\n These are unique which are given to a variable(Name given to memory reference) or function etc.\n\n\n\nTip: Avoid underscore and capital letters as prefix identifier \n\nEg: int learnOnPlay",
                     "Variables & Constants": "Variable:\n Variable names are just the symbolic representation of a memory location \n\n\nConstant:\n If you want to define a variable whose value cannot be changed, you can use the 'const' keyword or else use ' #define ' a preprocessor directive \n\n\n\nTip: Memory addresses were longer random digits which is impossible to remember to ease this we use variable so make it meaningful \n\nEg: int rollNoOfStudent = 121 \n       const double PI = 3.14 ",
                     "Data Types": "Data Types:\n These are declaration for variable which determine type and size of data.\n\n\n int    4(bytes) '%d, %i' \n\n char  1(byte)  '%c' \n\n float  4(bytes) '%f'\n\n double 8(bytes) '%lf' \n\n\n\n Tip: when you use (int,%c) or (char,%d) returns particular code and vice versa \n\nEg: print('%d','a') // prints ASCII code of 'a' ",
                     "Input/Output": "Input:\n\n\n\n scanf() function to take input from the user\n\nSyntax: scanf('formatSpecifier',&identifierName )\n\nEg: scanf('%d',&rollNumber) \n\n    Tip: On Successful input it returns no.of Input taken\n\n\n\n\nOutput:\n\n\n\n printf() function should be used to write on screen.\n\nSyntax: printf('formatSpecifier',identifierName )\n\nEg: printf('%d',rollNumber) \n\n    Tip: It returns no.of character written as output.",
                     "Operators": "Operators:\n A symbol to operate two operands.\n\n    1. Arithmetic operators( assignment = , decrement - , multiplication * , division / , modulo division % )\n\n    2. Increment ( ++ increments value by 1 ), Decrement ( -- decrements value by 1)\n\n    3. Assignment ( =, += add two operands and result will be stored in L.H.S. operand, -=, *=, /=, %=)\n\n    4. Relational Operators (returns 1 if relation between two operands is True else 0 [<,<=,>,>=,!= not equal,== equals])\n\n ",
                     

                     }
      for operation, info in operations.items():
         banner = Banner(operation=operation, info=info)
         grid.add_widget(banner)
   