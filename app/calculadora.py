import flet as ft         

def main(page: ft.Page):
    page.bgcolor = "black"
    page.title = "CALCULADORA BASICA"
    page.theme_mode = "light"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.window.width = 350
    page.window.height = 400
    page.window.min_width = 350
    page.window.max_width = 350
    page.window.min_height = 400
    page.window.max_height = 400
    page.window.icon = "imagen_cal.ico"
    page.window.resizable = False
    page.window.center()
    page.update()
    
    entrada = ft.TextField(
        color="white",
        cursor_color="white",
        text_align="right",
        border_color="blue"
    )
    
    entrada.focus()

    def manejar_teclas(e: ft.KeyboardEvent):
        tecla = e.key

        if tecla.isdigit():
            agregar(tecla)

        elif tecla in ["+", "-", "*", "/"]:
            agregar(tecla)

        elif tecla == "Backspace":
            entrada.value = entrada.value[:-1]
            entrada.update()

        elif tecla == "Enter":
            calcular(None)

    page.on_keyboard_event = manejar_teclas

    def agregar(valor):
        entrada.value = (entrada.value or "") + valor
        entrada.update()

    def borrar(e):
        entrada.value = ""
        entrada.update()
        
    def calcular(e):
        try:
            entrada.value = str(eval(entrada.value))
        except:
            entrada.value = "ERROR"
        entrada.update()
        
    fila_botones = ft.Row(
        controls=[
            ft.Button("+", on_click=lambda e: agregar("+"), color="white", bgcolor="blue"),
            ft.Button("-", on_click=lambda e: agregar("-"), color="white", bgcolor="blue"),
            ft.Button("*", on_click=lambda e: agregar("*"), color="white", bgcolor="blue"),
            ft.Button("/", on_click=lambda e: agregar("/"), color="white", bgcolor="blue"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )
    
    fila_botones_2 = ft.Row(
        controls=[
            ft.Button("7", on_click=lambda e: agregar("7"), color="white", bgcolor="blue"),
            ft.Button("8", on_click=lambda e: agregar("8"), color="white", bgcolor="blue"),
            ft.Button("9", on_click=lambda e: agregar("9"), color="white", bgcolor="blue"),
            ft.Button("<-", on_click=borrar, color="white", bgcolor="blue"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )
    
    fila_botones_3 = ft.Row(
        controls=[
            ft.Button("6", on_click=lambda e: agregar("6"), color="white", bgcolor="blue"),
            ft.Button("5", on_click=lambda e: agregar("5"), color="white", bgcolor="blue"),
            ft.Button("4", on_click=lambda e: agregar("4"), color="white", bgcolor="blue"),
            ft.Button("0", on_click=lambda e: agregar("0"), color="white", bgcolor="blue"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )
    
    fila_botones_4 = ft.Row(
        controls=[
            ft.Button("3", on_click=lambda e: agregar("3"), color="white", bgcolor="blue"),
            ft.Button("2", on_click=lambda e: agregar("2"), color="white", bgcolor="blue"),
            ft.Button("1", on_click=lambda e: agregar("1"), color="white", bgcolor="blue"),
            ft.Button("=", on_click=calcular, color="white", bgcolor="blue"),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )
    
    fila_boton = ft.Row(
        controls=[
            ft.Button("C", on_click=borrar, color="white", bgcolor="red", expand=2),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    
    page.add(entrada, fila_botones, fila_botones_2, fila_botones_3,
             fila_botones_4, fila_boton)

ft.run(main, assets_dir="assets")

