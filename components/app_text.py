import flet as ft

def app_text(text:str, size:int, italic:bool) -> ft.Text:
    return ft.Text(
        value=text,
        font_family="Verdana",
        size=size,
        italic=italic,
        weight="bold",
        max_lines=1,
        overflow=ft.TextOverflow.ELLIPSIS,
        animate_opacity=ft.animation.Animation(200, ft.AnimationCurve.EASE)
    )