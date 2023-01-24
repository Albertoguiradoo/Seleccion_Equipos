import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Futbolístico"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER//// esto es para centrarlo en el medio
    
    vEquipos=["Cadiz CF","AOVE Villacarrillo","Málaga CF"," NewCastle UFC","Club Deportivo Alcoyano"]
    vEquipos_Seleccionados = []


   
    
    def cambiarFoto(e):
        if (equipos.value == "Cadiz CF"):
            img.src = "Imágenes/CadizCF.jpg"
                
        elif (equipos.value == "AOVE Villacarrillo"):
            img.src = "Imágenes/AOVE Villacarrillo.png"
                
        elif (equipos.value == "Málaga CF"):
            img.src = "Imágenes/MalagaCF.png"
            
        elif (equipos.value == "NewCastle UFC"):
            img.src = "Imágenes/NewcastleUFC.png"
        
        elif (equipos.value == "Club Deportivo Alcoyano"):
            img.src = "Imágenes/CDAlcoyano.png"
        page.update()



    equipos = ft.Dropdown(label="Equipos",on_change=cambiarFoto, width=400)


    #Inserto los equipos desde la lista   
    for equipo in vEquipos:
        equipos.options.append(ft.dropdown.Option(equipo))

    
    img = ft.Image(src=f"g")
    
    
    


    page.add(equipos,img)
    


    

       
   
ft.app(target=main,assets_dir="Imágenes")