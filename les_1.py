
import flet as ft

# определить основную функцию
def main(page: ft.Page):
    # настройки заголовка страницы
    page.title =  'Привет, мир!'
    text = ft.Text(value='Мое первое приложениe',color='white')

    # добавляем на страницу
    page.controls.append(text)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER) # откроет в браузере
# ft.app(target=main)











































