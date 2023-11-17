from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window


class ImageButton(ButtonBehavior, Image):
    pass


class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Header with the title and WiFi/battery indicators
        header = BoxLayout(size_hint_y=None, height=50)
        header.add_widget(Label(text='9:59', size_hint_x=None, width=100))
        header.add_widget(Label(text='Drifting Bottle', halign='center'))
        header.add_widget(
            Image(source='wifi.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, keep_ratio=True))
        self.add_widget(header)

        # Message label
        self.add_widget(Label(text='you dont have messages right now'))

        # Footer with the icons resized and evenly spaced
        footer = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        # Create ImageButtons for the footer
        footer.add_widget(ImageButton(source='bottle.jpg', allow_stretch=True, keep_ratio=True))
        footer.add_widget(ImageButton(source='search.png', allow_stretch=True, keep_ratio=True))
        footer.add_widget(ImageButton(source='person.png', allow_stretch=True, keep_ratio=True))
        self.add_widget(footer)


class DriftingBottleApp(App):
    def build(self):
        # Set the window size to typical phone dimensions

        return HomePage()


if __name__ == '__main__':
    DriftingBottleApp().run()
