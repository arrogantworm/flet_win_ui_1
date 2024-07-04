import flet as ft
from core.layout import Layout


def main(page: ft.Page):

    page.padding = 0
    page.title = 'FletUI #1'
    page.bgcolor = ft.colors.TRANSPARENT
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.window_min_width = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.add(Layout())


ft.app(main, assets_dir='assets')
