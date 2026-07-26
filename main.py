from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class CrushApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.label = Label(
            text="Hi Crush ❤️",
            font_size=40
        )

        self.question = Label(
            text="Did you love me?",
            font_size=30
        )

        yes_button = Button(
            text="Yes",
            font_size=25
        )
        no_button = Button(
            text="No",
            font_size=25
        )

        yes_button.bind(on_press=self.answer)
        no_button.bind(on_press=self.answer)

        layout.add_widget(self.label)
        layout.add_widget(self.question)
        layout.add_widget(yes_button)
        layout.add_widget(no_button)

        return layout

    def answer(self, instance):
        self.question.text = "Yes ❤️ I knew it!"


CrushApp().run()
