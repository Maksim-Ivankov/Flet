
import flet as ft
from time import sleep

# определить основную функцию
def main(page: ft.Page):
    # настройки заголовка страницы
    page.title =  'Считалка'
    text = ft.Text()

    # добавляем на страницу
    page.add(text)

    for i in range(1,11):
        text.value = f'Считалочка {i}'
        sleep(1)
        page.update()


ft.app(target=main)

