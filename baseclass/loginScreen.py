from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
import os.path
import sqlite3
from kivymd.app import MDApp
manager = ScreenManager()


class LoginScreen(Screen):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Lop.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    flag=0
    # Button event that will be called on login
    def verify(self,username,password):
         
        if username=="" or password=="":
            self.ids['incorrectCredentials'].text="Please provide user name and password"

        elif username!="" and password!="":
           

            try:
                if self.flag==0:
                   
                    self.cursor.execute("select * from Login Where Username='%s' and Password='%s'" %(username,password))
                    data = self.cursor.fetchone()
                    self.app = MDApp.get_running_app()
                    
                    if data is None:
                        self.ids['incorrectCredentials'].text= "Account not available"
                    elif data[0]==username and data[1]==password:
                        self.flag=1
                        self.cursor.execute('update Login set status="active" where Username="%s"' % (username))
                        self.app.root.ids['userNameLabel'].text = username + "  :  " + "Active".upper() + "\n" + "Score : " + str(data[3])
                        self.manager.transition = SlideTransition(direction="left")
                        self.manager.current = 'homeScreen'
                        self.ids['loginButton'].text="logout"
                    
                    else:
                        self.ids['incorrectCredentials'].text="Incorrect Credentials"
                else:
                    self.flag=0

                    self.app.root.ids['userNameLabel'].text = ""
                    self.ids['password'].text=""
                    self.ids['loginButton'].text="login"
                    self.cursor.execute('update Login set status="Inactive" where Username="%s"' % (username))
                    self.connection.commit()
                    

            except Exception as e:
                self.ids['incorrectCredentials'].text= str(e)

          
        
        
    def registration(self,username,password):
        try:
           
            if username=="" or password=="":
                self.manager.get_screen(self.manager.current).ids['register'].on_click=self.manager.get_screen(self.manager.current).ids['titlePanel'].text="Provide username and password"   
            else:
                q="insert into Login values('"+username+"','"+password+"',Null,Null,Null)"
                self.cursor.execute(q)
                self.connection.commit()
                self.manager.get_screen(self.manager.current).ids['register'].on_click=self.manager.get_screen(self.manager.current).ids['titlePanel'].text="Registered, Click login to continue "   
        except Exception:
                self.manager.get_screen(self.manager.current).ids['titlePanel'].text="You already have an account, Click Login"  
                self.cursor.close()
                self.connection.close()


