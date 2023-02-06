import flet as ft

def main(page: ft.Page):
    page.title = "Proyecto Futbolístico"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER//// esto es para centrarlo en el medio
    
    vEquipos=["Cadiz CF","AOVE Villacarrillo","Málaga CF","FC Barcelona","Club Deportivo Alcoyano"]
    vEquipos_Seleccionados = []


    def botonGuardar(e):
        equipo = dropDownEquipos.value 
        if (vEquipos_Seleccionados.count(equipo)==0):
            vEquipos_Seleccionados.append(equipo)
            lv.controls.append(ft.Text(equipo))
        else:
            dlg = ft.AlertDialog(title=ft.Text("EQUIPO REPETIDO!!!"))
            page.dialog = dlg
            dlg.open = True
        page.update()
    
        
    
    
    def cambiarFoto(e):
        if (
            dropDownEquipos.value == "Cadiz CF"):
            img.src = "Imágenes/CadizCF.jpg"
                
        elif (
            dropDownEquipos.value == "AOVE Villacarrillo"):
            img.src = "Imágenes/AOVE Villacarrillo.png"
                
        elif (
            dropDownEquipos.value == "Málaga CF"):
            img.src = "Imágenes/MalagaCF.png"
            
        elif (
            dropDownEquipos.value == "FC Barcelona"):
            img.src = "Imágenes/barsa.png"
        
        elif (
            dropDownEquipos.value == "Club Deportivo Alcoyano"):
            img.src = "Imágenes/CDAlcoyano.png"
                
        page.update()

    def cargarequipos():
        vEquipos=[]
        f=open("Equipos.txt", "r")

        for linea in f:
            vEquipos.append(linea)

        f.close()
        return vEquipos



#---------------Fin definiciones de funciones ------------



 #Componentes Flet
    img = ft.Image(src=f"g")
    bt=ft.ElevatedButton(text="Seleccionar equipo", on_click=botonGuardar)
    dropDownEquipos = ft.Dropdown(label="Equipos",on_change=cambiarFoto, width=400)
    lv = ft.ListView(expand=1, spacing=5, padding=20, auto_scroll=True)

    #----------Fin definiciones de variables----------------

    

    
#---------------Inicio programa principal----------------

    #Inserto los 
    # dropDownEquipos desde la lista   
    for equipo in vEquipos:
        dropDownEquipos.options.append(ft.dropdown.Option(equipo))

    
    
    #Añadir componestes a la vista
    page.add(dropDownEquipos,img,bt,lv)
    
   
                              



   
ft.app(target=main,assets_dir="Imágenes")