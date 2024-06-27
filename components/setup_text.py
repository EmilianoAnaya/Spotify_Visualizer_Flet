import flet as ft

def app_text(text:str, size:int) -> ft.Text:
    return ft.Text(
        value=text,
        font_family="Verdana",
        size=size,
        weight="bold",
        animate_opacity=ft.animation.Animation(200, ft.AnimationCurve.EASE),
        text_align=ft.TextAlign.CENTER
    )