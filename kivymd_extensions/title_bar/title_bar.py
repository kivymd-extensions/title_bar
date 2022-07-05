from kivymd.uix.boxlayout import MDBoxLayout

from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.logger import Logger

import os

with open(
    os.path.join(os.path.dirname(__file__), "title_bar.kv"),
    encoding="utf-8",
) as kv:
    Builder.load_string(kv.read())


class MDTitleBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window_size = None, None

        if not Window.custom_titlebar:
            Window.custom_titlebar = True

            if not Window.set_custom_titlebar(self):
                Logger.error("Window: setting custom titlebar Not allowed on this system ")

    @staticmethod
    def roll_up(inst):
        inst.anim_complete()
        Window.minimize()

    def restore(self, inst):
        inst.anim_complete()

        if all(not x for x in self.window_size):
            Window.maximize()
            self.window_size = Window.size
        else:
            if Window.size == self.window_size:
                Window.restore()
            else:
                Window.maximize()
                self.window_size = Window.size
