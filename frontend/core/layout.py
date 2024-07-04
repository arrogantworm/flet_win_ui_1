import flet as ft
from core.leftmenu.leftmenu import LeftMenu
from core.maincontent.maincontent import MainContent
from core.rightmenu.rightmenu import RightMenu


class Layout(ft.Container):
    def __init__(self):
        super().__init__()

        # Parameters
        self.expand = True
        self.bgcolor = ft.colors.TRANSPARENT

        # Content
        self.leftmenu = LeftMenu()
        self.main_content = MainContent()
        self.rightmenu = RightMenu()

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.leftmenu,
                self.main_content,
                self.rightmenu,
            ]
        )
