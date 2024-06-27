import json
import asyncio
import flet as ft
from constants import IMAGE_LOGO, DATA_FILE
from components.app_text import app_text
from SpotifyAuth import get_Spotify

class Spotify_Visualizer:
    def __init__(self):
        self.flag:bool = False
        self.flag_song:bool = True
        self.current_track = ""
        self.current_id_track = ""
        with open(DATA_FILE) as file:
            credentials = json.load(file)
            CLIENT_ID = credentials["Client_ID"]
            CLIENT_SECRET = credentials["Client_Secret"]
        file.close()
        self.spotify = get_Spotify(CLIENT_ID, CLIENT_SECRET)

    def main(self, page: ft.Page):
        self.page = page
        self.page.window.icon = IMAGE_LOGO
        self.page.window.height = 310
        self.page.window.width = 1128
        self.page.window.resizable = False
        self.page.window.maximizable = False
        self.page.window.frameless = True
        self.page.window.bgcolor = ft.colors.TRANSPARENT
        self.page.bgcolor = ft.colors.TRANSPARENT 
        self.page.window.prevent_close = True
        self.page.window.on_event=self.window_event

        self.dark_background = ft.Container(
            bgcolor=ft.colors.BLACK,
            opacity=0.6,
        )
        
        self.img_album_info = ft.Image(
            src=IMAGE_LOGO,
            width=815,
            height=210,
            fit=ft.ImageFit.FILL,
        )

        self.song_name = app_text("Waiting for a Song to Track", 30, True)
        self.song_artist = app_text("Select a Song from your Spotify", 15, False)

        self.song_data = ft.Column(
            [
                self.song_name,
                self.song_artist,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0
        )

        self.img_stack = ft.Stack(
            [
                self.img_album_info,
                self.dark_background,
                ft.Container(
                    content=self.song_data,
                    alignment=ft.alignment.center_left,
                    margin=ft.margin.only(left=70)
                )
            ],
        )

        self.song_information = ft.Container(
            content=self.img_stack,
            width=815,
            height=210,
            animate=ft.animation.Animation(900, ft.AnimationCurve.EASE),
            on_animation_end=self.show_song,
            border_radius=ft.border_radius.horizontal(0, 30)
        )

        self.song_album_cover = ft.Image(
            src=IMAGE_LOGO,
            width=300,
            height=300,
            fit=ft.ImageFit.FILL,
            border_radius=ft.border_radius.all(20),
            opacity=1,
            animate_opacity=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        )

        self.page.add(
            ft.WindowDragArea(
                ft.Row(
                    [
                        self.song_album_cover,
                        self.song_information,
                    ],
                    spacing=0,
                ),
            )
        )
        asyncio.run(self.Song_Timer())

    async def Song_Timer(self):
        while self.flag_song:
            await asyncio.sleep(3)
            self.CheckCurrentTrack()

    def CheckSameSong(self, results) -> bool:
        if results['item']['id'] == self.current_id_track:
            return True
        self.current_id_track = results['item']['id']
        self.current_track = results
        return False
    
    def CheckCurrentTrack(self) -> None:
        results = self.spotify.current_user_playing_track()
        if not results:
            return
        if not self.CheckSameSong(results):
            self.close_container()

    def Set_Album_Covers(self, Album_Cover:str) -> None:
        self.song_album_cover.src = Album_Cover
        self.img_album_info.src = Album_Cover

    def Set_Song_Info(self, Song_Title:str, Song_Artists:list) -> None:
        self.song_name.value = Song_Title
        SongArtists = ' - '.join(Artists['name'] for Artists in Song_Artists)
        self.song_artist.value = SongArtists

    def show_song(self, e):
        if not self.flag:
            self.Set_Album_Covers(self.current_track['item']['album']['images'][1]['url'])
            self.Set_Song_Info(self.current_track['item']['name'], self.current_track['item']['artists'])
            self.open_container()

    def open_container(self):
        self.flag = True
        self.song_album_cover.opacity = 1
        self.song_information.width = 815
        self.song_information.update()
        self.song_name.opacity = 1
        self.song_name.update()
        self.song_artist.opacity = 1
        self.song_artist.update() 
        self.song_album_cover.update()
        self.img_album_info.update() 
        self.page.update()
    
    def close_container(self):
        self.flag = False
        self.song_album_cover.opacity = 0
        self.song_information.width = 0
        self.song_information.update()
        self.song_name.opacity = 0
        self.song_name.update()
        self.song_artist.opacity = 0
        self.song_artist.update()
        self.song_album_cover.update()

    def window_event(self, e):
        if e.data == "close":    
            self.flag_song = False
            self.page.window.destroy()


app = Spotify_Visualizer()
ft.app(target=app.main)