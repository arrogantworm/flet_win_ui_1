import flet as ft


class LeftMenu(ft.Container):
    def __init__(self):
        super().__init__()

        self.bgcolor = ft.colors.WHITE54
        self.expand = False
        self.width = 90
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(20, 50, 20)

        self.content = ft.Column(
            width=90,
            spacing=30,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.icons.NOTIFICATIONS_OUTLINED,
                              icon_color=ft.colors.WHITE,
                              hover_color=ft.colors.BLACK38,
                              icon_size=32,),
                ft.IconButton(ft.icons.VIDEO_CAMERA_BACK_OUTLINED,
                              icon_color=ft.colors.WHITE,
                              hover_color=ft.colors.BLACK38,
                              icon_size=32,),
                ft.IconButton(ft.icons.MESSAGE_OUTLINED,
                              icon_color=ft.colors.WHITE,
                              hover_color=ft.colors.BLACK38,
                              icon_size=32,),
                ft.IconButton(ft.icons.CALENDAR_MONTH_OUTLINED,
                              icon_color=ft.colors.WHITE,
                              hover_color=ft.colors.BLACK38,
                              icon_size=32,),
            ]
        )
