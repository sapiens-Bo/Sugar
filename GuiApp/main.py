from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from scr_menu import Menu
from scr_sale import Sale

class SugarApp(App):
    def build(self):
        Window.size = 380, 840
        Window.clearcolor = (1,1,1,1)
        sm = ScreenManager()
        sm.add_widget(Menu())
        sm.add_widget(Sale())
        return sm
    
if __name__ == '__main__':
    SugarApp().run()