
import flet as ft
from time import sleep

# определить основную функцию
def main(page: ft.Page):
    # настройки заголовка страницы
    page.title =  'Таблица'

    # добавляем на страницу
    page.add(
        ft.Row(controls=[ft.Text(value='Фрукты:\n')]),
        ft.Row(
            controls=[
                ft.Text('Яблоко'),
                ft.Text('Банан'),
                ft.Text('Киви'),
            ]
        ),
        ft.Column(controls=[ft.Text(value='Пиво:\n')]),
        ft.Column(
            controls=[
                ft.Text('Бавария'),
                ft.Text('Жига'),
                ft.Text('Балтика'),
            ]
        )
    )

    page.update()


ft.app(target=main)
