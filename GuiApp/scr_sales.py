from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import database

class Sales(Screen):
    Builder.load_file('sales.kv')

    def updateScr(self):
        self.ids.table.text = database.outTable('sales')