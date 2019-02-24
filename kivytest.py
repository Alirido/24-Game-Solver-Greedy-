import kivy
kivy.require('1.10.1') # put your kivy version

from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):
	pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

CustomWidgetApp().run()