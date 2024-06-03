
import flet as ft
from time import sleep



# определить основную функцию
def main(page: ft.Page):
    page.title =  'Кликер'
    page.theme_mode='light'
    page.vertical_alignment = 'center'
    
    txt_number = ft.TextField(value='0', width=100,text_align='center')

    def click_plus(e):
        txt_number.value = int(txt_number.value)-1
        page.update()

    def click_minus(e):
        txt_number.value = int(txt_number.value)+1
        page.update()
        

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=click_plus),
                txt_number,
                ft.IconButton(ft.icons.ADD,on_click=click_minus)
            ],
            alignment='center'
        )
    )
    

ft.app(target=main)


























