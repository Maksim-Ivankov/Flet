from random import randint
import flet as ft

def main(page: ft.Page):
    page.title =  'Игра'
    page.fonts = {
        'Space':'fonts/SpaceMission-rgyw9.otf'
    }
    page.padding = 20

    answer = randint(1,100)

    print(answer)
    
    player_1 = ft.TextField(hint_text='Угадай число от 1 до 100',label='Игрок 1',width=250)
    player_2 = ft.TextField(hint_text='Угадай число от 1 до 100',label='Игрок 2',width=250)

    result = ft.Text()

    def check_1(e):
        if int(player_1.value) < answer:
            result.value = 'Выше'
        elif int(player_1.value) > answer:
            result.value = 'Ниже'
        elif int(player_1.value) == answer:
            result.value = 'Игрок 1 выйграл игру'
        else:
            result.value('Ошибка')
        page.update()

    def check_2(e):
        if int(player_2.value) < answer:
            result.value = 'Выше'
        elif int(player_2.value) > answer:
            result.value = 'Ниже'
        elif int(player_2.value) == answer:
            result.value = 'Игрок 2 выйграл игру'
        else:
            result.value('Ошибка')
        page.update()

    check_player_1 = ft.ElevatedButton('Проверить',on_click=check_1)
    check_player_2 = ft.ElevatedButton('Проверить',on_click=check_2)

    page.add(
        ft.Card(
            ft.Container(
                content = ft.Row(
                    controls=[ft.Text(value='Space',size=50,font_family='Space')],
                    alignment='center'
                ),
                padding=2
            ),
        ),
        ft.Column(
            [
                ft.Row([player_1,check_player_1]),
                ft.Row([player_2,check_player_2]),
                result
            ],
            horizontal_alignment='center'
            
        )
        
    )


ft.app(target=main, assets_dir='assets')


