
import flet as ft
from time import sleep



# определить основную функцию
def main(page: ft.Page):
    page.title =  'Валидация инпутов'
    page.theme_mode='light'
    page.horizontal_alignment = 'center'
    page.padding = 20

    user_name = ft.TextField(label='Введи имя',width=300)
    print_name_column = ft.Column()

    def call_hello(e):
        if not user_name.value:
            user_name.error_text = 'Введи имя'
            page.update()
        else:
            page.clean()
            print_name_column.controls.append(ft.Text(f'Привет {user_name.value}!')) 
            page.add(print_name_column)

    

    page.add(
        user_name,
        ft.ElevatedButton('Скажи привет!',on_click=call_hello),
        
    )
    

ft.app(target=main)


























