# Title bar

## Installation

```bash
pip install kivymd_extensions.title_bar
# or
pip install https://github.com/kivymd-extensions/title_bar/archive/master.zip
```

### Dependencies:

- [KivyMD](https://github.com/kivymd/KivyMD) >= master version
- [Kivy](https://github.com/kivy/kivy) >= 2.0.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Python 3.6+](https://www.python.org/)

### Usage

```python
from kivymd.app import MDApp
from kivymd_extensions.title_bar import MDTitleBar


class MainApp(MDApp):
    def build(self):
        return MDTitleBar()


if __name__ == "__main__":
    MainApp().run()
```

![demo_img](https://user-images.githubusercontent.com/40869738/177749688-76cd38a9-42d0-432d-868f-d6d1077ac8e3.png)


### Support

If you need assistance, or you have a question, you can ask for help on our mailing list:

- **Discord server:** https://discord.gg/wu3qBST
- **Email:** kivydevelopment@gmail.com

## License

[MIT License](LICENSE)
