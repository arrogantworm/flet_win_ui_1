import flet as ft


class RightMenu(ft.Container):
    def __init__(self):
        super().__init__()

        self.test_tasks_list = [
            ['tasks/1.png', 'Task 1', 'Do something'],
            ['tasks/2.png', 'Task 2', 'Do something'],
            ['tasks/3.png', 'Task 3', 'Do something'],
        ]

        self.bgcolor = ft.colors.WHITE54
        self.width = 200
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=20)

        self.content = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            width=200,
            spacing=0,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text('Задачи',
                        color=ft.colors.WHITE,
                        size=20,
                        weight='w700',),
                # Divider
                ft.Container(
                    height=40
                ),
            ]
        )

    def build(self):
        for task in self.test_tasks_list:
            self.content.controls.append(Task(task[0], task[1], task[2]))


class Task(ft.Container):
    def __init__(self, src, title, subtitle):
        super().__init__()

        self.bgcolor = ft.colors.TRANSPARENT
        self.width = 200
        self.height = 200
        self.alignment = ft.alignment.center
        self.padding = ft.padding.all(20)
        self.on_hover = self.hover

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(src=src,
                         width=30,
                         height=30,
                         border_radius=ft.border_radius.all(100),
                         animate_scale=200),
                ft.Text(title, size=14, color=ft.colors.WHITE, weight='w500', animate_scale=200),
                ft.Text(subtitle, size=14, color=ft.colors.WHITE70, weight='w200', animate_scale=200),
            ]
        )

    def hover(self, e):
        self.bgcolor = ft.colors.BLACK38 if e.data == 'true' else ft.colors.TRANSPARENT
        self.content.controls[0].scale = 1.4 if e.data == 'true' else 1
        for text in self.content.controls[1:]:
            text.scale = 1.4 if e.data == 'true' else 1
            text.update()
        self.content.controls[0].update()
        self.update()
