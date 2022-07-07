from kivymd.app import MDApp

from kivy.lang.builder import Builder
from kivy.factory import Factory

Factory.register(
    "MDTitleBar",
    module="kivymd_extensions.title_bar.title_bar",
)

KV = """
MDScreen:
    MDTitleBar:
        id: title_bar

    MDTopAppBar:
        id: toolbar
        title: "MDTopAppBar"
        size_hint_y: None
        y: title_bar.y - self.height
    
    ScrollView:
        id: scroll_view
        size_hint: (None, None)
        size: (root.width, root.height - title_bar.height - toolbar.height - dp(10))
        always_overscroll: False
        
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            padding: dp(0), max(scroll_view.height / 2 - primary_color_btn.height - dp(5), dp(0)), dp(0), dp(0)
            spacing: dp(10)
            
            MDRaisedButton:
                id: primary_color_btn
                text: "Update primary color"
                pos_hint: {"center_x": .5}
                on_release: app.update_color()
        
            MDRaisedButton:
                text: "Update theme"
                pos_hint: {"center_x": .5}
                on_release: app.change_theme()
"""

colors = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
          'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']


class CustomTitleBar(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = colors.copy()
        self.screen = Builder.load_string(KV)

        self.title = "My App"

    def build(self):
        return self.screen

    def update_color(self):
        self.colors.remove(self.theme_cls.primary_palette)

        if not self.colors:
            self.colors = colors.copy()

        self.theme_cls.primary_palette = self.colors[0]

    def change_theme(self):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'


if __name__ == "__main__":
    CustomTitleBar().run()
