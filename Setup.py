import os
import json
import flet as ft
from constants import IMAGE_LOGO
from components.setup_text import app_text
from components.setup_entry import Setup_Entry
from SpotifyAuth import get_Spotify

class Setup_Visualizer:
    def __init__(self) -> None:
        self.spotify = None
        if os.path.exists(".cache"):    
            os.remove(".cache")

        print("DO NOT CLOSE THIS WINDOW, YOU'LL NEED IT FOR THE REDIRECT URI FOR THE AUTHENTICATION!")

    def main(self, page:ft.Page):
        self.page = page
        self.client_id = Setup_Entry(title_entry="CLIENT_ID")
        self.client_secret = Setup_Entry(title_entry="CLIENT_SECRET")
        self.btn_submit = ft.ElevatedButton(
            text="Submit",
            on_click=self.Submit_Credentials,
            color=ft.colors.WHITE,
            height=40,
            width=140,
        )
        
        self.items_column = ft.Column(
            [
                app_text("Spotify Visualizer", 20),
                app_text("Insert your Spotify Credentials so you the widget can authenticate the session at your dashboard app", 12,),
                self.client_id,
                self.client_secret,
                self.btn_submit
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=23
        )
        
        self.container = ft.Container(
            content=self.items_column,
            alignment=ft.alignment.top_center
        )
        
        self.img_logo = ft.Image(
            src=IMAGE_LOGO,
            width=440,
            height=303,
            fit=ft.ImageFit.FILL,
            opacity=0.4,
        )
        
        self.stack = ft.Stack(
            [
                self.img_logo,
                self.container
            ],
            width=440,
            height=360,
        )

        self.page.window.width = 420
        self.page.window.height = 360
        self.page.bgcolor = ft.colors.BLACK
        self.page.window.resizable = False
        self.page.window.maximizable = False
        self.page.add(self.stack)
    
    def Show_error(self) -> None:
        self.page.open(
                ft.AlertDialog(
                    title=ft.Text("Error.\nFill all the entries correctly.",size=14),
                    actions_alignment=ft.MainAxisAlignment.END               
                )
            )
    
    def Check_User(self, client_id:str, client_secret:str) -> None:
        self.spotify.current_user()
        if os.path.exists(".cache"):
            data =  {
                        "Client_ID": client_id,
                        "Client_Secret": client_secret
                    }
            with open('credentials/data.json',"w") as file:
                json.dump(data,file,indent=4)
            print("Success, you may now close this window and execute App.vbs\nWARNING: If you open up this file again, the Access Token will be lost and you'll have to\nregister your credentials again.")

    
    def Submit_Credentials(self, e):
        id_client = self.client_id.value.strip()
        secret_client = self.client_secret.value.strip()
        if not id_client or not secret_client:
            self.Show_error()
            return
        self.spotify=get_Spotify(id_client,secret_client)
        self.Check_User(id_client,secret_client)



app = Setup_Visualizer()
ft.app(target=app.main)