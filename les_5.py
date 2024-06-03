
import flet as ft
from time import sleep



# определить основную функцию
def main(page: ft.Page):
    page.title =  'Форма ввода'
    page.theme_mode='light'


    first_name = ft.TextField(label='Введи имя',autofocus=True)
    last_name = ft.TextField(label='Введи фамилию')

    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f'Привет {first_name.value} {last_name.value}!'))
        first_name.value = ''
        last_name.value = ''
        page.update()

    hello = ft.ElevatedButton('Привет', on_click=btn_click)

    page.add(
        first_name,
        last_name,
        hello,
        greetings
    )
    

ft.app(target=main)


























