import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER





    img = ft.Image(src=f"CadizCF.jpg")
    
    page.add(img)












ft.app(target=main,assets_dir="Imágenes")