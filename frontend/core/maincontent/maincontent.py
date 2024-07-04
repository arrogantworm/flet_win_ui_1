import flet as ft


class MainContent(ft.Container):
    def __init__(self):
        super().__init__()

        self.bgcolor = ft.colors.BLACK54
        self.expand = True
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(10, 50, 20)

        self.content = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                # Top Text
                ft.ResponsiveRow(

                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Text('Предстоящие встречи',
                                size=14,
                                color=ft.colors.WHITE)
                    ]
                ),
                # Divider
                ft.Container(
                    height=40,
                ),
                # MeetingInformation
                ft.ResponsiveRow(
                    columns=14,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        # Встреча,
                        MeetingDescription(),
                        # Кто проводит,
                        MeetingHost(),
                    ]
                )

            ]
        )


class MeetingDescription(ft.Column):
    def __init__(self):
        super().__init__()
        self.col = {'xs': 12, 'sm': 12, 'md': 6, 'lg': 6, 'xl': 6}
        self.controls = [
            # Title
            ft.Text(
                'Очень важная встреча',
                size=20,
                color=ft.colors.WHITE,
            ),
            # Date
            ft.Text(
                '10.07.2024 @ 14:00',
                size=22,
                color=ft.colors.WHITE,
            ),
            # Description
            ft.Text(
                'Хорошая тема письма должна быть креативной и привлекательной, а также намекать на то, о чем идет речь в письме с просьбой о встрече.',
                size=14,
                color=ft.colors.WHITE70,
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.IconButton(icon=ft.icons.ADD,
                                  icon_color=ft.colors.WHITE,
                                  hover_color=ft.colors.BLACK38,
                                  icon_size=14,
                                  ),
                    ft.Text('Записаться'),
                ]
            )
        ]


class MeetingHost(ft.Column):
    def __init__(self):
        super().__init__()
        self.col = {'xs': 12, 'sm': 12, 'md': 6, 'lg': 6, 'xl': 6}
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    # Host Description
                    ft.Column(
                        col={'xs': 8, 'sm': 8, 'md': 6, 'lg': 6, 'xl': 6},
                        controls=[
                            # Name
                            ft.Text(
                                'Имя Фамилия',
                                size=22,
                                color=ft.colors.WHITE,
                                weight='w200',
                            ),
                            # Description
                            ft.Text(
                                'Докторская колбаса',
                                size=14,
                                color=ft.colors.WHITE,
                            ),
                        ]
                    ),
                    # Picture
                    ft.Column(
                        col={'xs': 8, 'sm': 8, 'md': 6, 'lg': 6, 'xl': 6},
                        controls=[
                            ft.Image(
                                src='host/1.png',
                                border_radius=ft.border_radius.all(100),
                            )
                        ]
                    )
                ]
            )
        ]
