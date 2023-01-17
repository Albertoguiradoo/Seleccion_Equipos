import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Futbolístico"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER//// esto es para centrarlo en el medio


    equipos = ft.Dropdown(label="Equipos",width=400,options=[ft.dropdown.Option("Cadiz CF"),
                                                            ft.dropdown.Option("AOVE Villacarrillo"),
                                                            ft.dropdown.Option("Club Deportivo Alcoyano"),
                                                            ft.dropdown.Option("Málaga CF"),
                                                            ft.dropdown.Option("NewCastle UFC"),] ,on_change=dropdown_changed
    )
    page.add(equipos)



    #equipos_imagen = ""

    def dropdown_changed(e):
        if (equipos.value == "Cadiz CF"):
            equipos_imagen = "Imágenes/CadizCF.jpg"
            
        
        elif (equipos.value == "AOVE Villacarrillo"):
            equipos_imagen = "Imágenes/AOVE Villacarrillo.png"
            print("platano al poder")

        elif (equipos.value == "Málaga CF"):
            equipos_imagen = "Imágenes/MalagaCF.png"
            print("platano al poder")
        
        elif (equipos.value == "NewCastle UFC"):
            equipos_imagen = "Imágenes/NewcastleUFC.pmg"
            
        equipos_imagen.src=f"{equipos_imagen}"
        page.update()
        equipos_imagen = ft.Image(src=f"CadizCF.jpg")
    
        page.add(equipos_imagen)

ft.app(target=main,assets_dir="Imágenes")