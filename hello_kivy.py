from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text='Tekan tombol')
        btn = Button(text='Click Me')
        btn.bind(on_press=self.say_hello)

        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def say_hello(self, instance):
        self.label.text = 'Hello World'


MyApp().run()

