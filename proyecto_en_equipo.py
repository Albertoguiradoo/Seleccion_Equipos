import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Futbolístico"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER//// esto es para centrarlo en el medio

    def cambiarFoto(e):
        if (equipos.value == "Cadiz CF"):
            img.src = "Imágenes/CadizCF.jpg"
                
        elif (equipos.value == "AOVE Villacarrillo"):
            img.src = "Imágenes/AOVE Villacarrillo.png"
                
        elif (equipos.value == "Málaga CF"):
            img.src = "Imágenes/MalagaCF.png"
                
            
        elif (equipos.value == "NewCastle UFC"):
            img.src = "Imágenes/NewcastleUFC.pmg"
                
        page.update()



    equipos = ft.Dropdown(label="Equipos",on_change=cambiarFoto, width=400,options=[ft.dropdown.Option("Cadiz CF"),
                                                            ft.dropdown.Option("AOVE Villacarrillo"),
                                                            ft.dropdown.Option("Club Deportivo Alcoyano"),
                                                            ft.dropdown.Option("Málaga CF"),
                                                            ft.dropdown.Option("NewCastle UFC"),])


    img = ft.Image(src=f"g")


    page.add(equipos,img)
    


    

       
   
ft.app(target=main,assets_dir="Imágenes")