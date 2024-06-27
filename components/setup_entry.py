import flet as ft

class Setup_Entry(ft.TextField):
    def __init__(self, title_entry):
        super().__init__()
        self.value = None
        self.label=title_entry
        self.bgcolor=ft.colors.BLACK54
        self.width=310
        self.border_color=ft.colors.WHITE