import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Futbolístico"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER//// esto es para centrarlo en el medio
    
    def boton(e):
        t.value = f"Equipo seleccionado:  {equipos.value}"
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(text="seleccionar", on_click=boton)
    equipos = ft.Dropdown(label="Equipos",width=500,options=[ft.dropdown.Option("Mogón CF"),
                                        ft.dropdown.Option("Villacarrillo"),
                                        ft.dropdown.Option("Club Deportivo Alcoyano"),
                                        ft.dropdown.Option("Málaga CF"),
                                        ft.dropdown.Option("New Castle UFC"),])
    page.add(equipos, b, t)




ft.app(target=main)