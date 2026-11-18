from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SoniyaApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        layout.add_widget(Label(
            text="[b]SONIYA AI[/b]\nYour Personal Assistant",
            markup=True,
            font_size=28
        ))

        button = Button(
            text="START SONIYA",
            font_size=22
        )

        layout.add_widget(button)
        return layout

SoniyaApp().run()
