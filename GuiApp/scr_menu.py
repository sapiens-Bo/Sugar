from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import database

class Menu(Screen):
    Builder.load_file('menu.kv')

    def clearTable(self):
        database.delPos('sales')
    


