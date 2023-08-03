from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sys
sys.path.append('..')
from scr_menu import Menu
from scr_sale import Sale
from scr_sales import Sales

class SugarApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        sm = ScreenManager()
        sm.add_widget(Menu())
        sm.add_widget(Sale())
        sm.add_widget(Sales())
        return sm
    
if __name__ == '__main__':
    SugarApp().run()