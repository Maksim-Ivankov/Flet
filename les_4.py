
import flet as ft
from time import sleep



# определить основную функцию
def main(page: ft.Page):
    page.title =  'ТУДУ лист'
    page.theme_mode='light'

    input_text = ft.TextField(hint_text='Введи задачу')

    def button_click(e):
        page.add(ft.Checkbox(label=input_text.value))

    page.add(
        ft.Row([
            input_text,
            ft.ElevatedButton(text='Добавить',on_click=button_click)
        ])
    )
    page.update()

ft.app(target=main)


















