from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import sys
sys.path.append('..')
import database

class Sale(Screen):
    Builder.load_file('sale.kv')
    total = ObjectProperty(None)
    price = ObjectProperty(None)
    how = ObjectProperty(None)

    def btnSale(self):
        total = self.total.text
        price = self.price.text
        how = self.how.text

        database.addSales(total, price, how)

        self.total.text = ''
        self.price.text = ''
        self.how.text = ''