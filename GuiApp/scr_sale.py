from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class Sale(Screen):
    Builder.load_file('sale.kv')
    total = ObjectProperty(None)
    # price = ObjectProperty(None)
    # how = ObjectProperty(None)