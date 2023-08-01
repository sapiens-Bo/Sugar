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
        if self.how.text in database.method_pay:
            try:
                total = int(self.total.text)
                price = float(self.price.text)
                how = self.how.text
                database.addSales(total, price, how)
                database.calcResult()
            except ValueError:
                print('Oops!', ValueError)
            self.total.text = ''
            self.price.text = ''
            self.how.text = ''
            self.ids.res.text = f'Терминал: {database.terminal}\nНаличные: {database.cash}\nМобильный банк: {database.mob_bank}\nВсего: {database.sum}'
