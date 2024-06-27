
# How to use this Widget
1.- Create a virtual enviroment for the widget and activate it:
```sh
python -m venv .venv
```
```sh
source .venv/scripts/activate
```

2.- Once created the virtual enviroment, install to it the following libraries:
* Spotipy
```sh
pip install spotipy
```
* Flet
```sh
pip install flet
```

3.- Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard), login to your account and create an App.

4.- On the screen for creating the App, you can put whatever title and description you want for the application, but for the section of "Redirect URIs" make sure to write down:
```sh
https://localhost:8888/callback
```
5.- Once created the app in the Dashboard, open it and head to settings.

6.- In the Basic Information section, you'll need your CLIENT_ID and CLIENT_SECRET so you can pass the Authentication for the use of the widget. Open the Setup.bat

7.- The Setup.bat will open up with a terminal and the Interface where you are gonna paste and submit your Credentials. 

![image](https://github.com/EmilianoAnaya/Spotify-Visualizer/assets/150195114/06467e07-bddc-428d-932b-6caea5a6fc90)


8.- Once you have entered your credentials, your browser will redirect you to Spotify so you can authenticate your account, then you will be redirected to a new page that will not load, copy the link to the new page and paste it into the terminal when prompted.

9.- Once pasted the link, the setup will be done and now you can execute the App.vbs file. After this you only need to use this file to use the Widget.

## Captures of the Widget

![image](https://github.com/EmilianoAnaya/Spotify-Visualizer/assets/150195114/56cc2a58-7796-4a0e-a4ae-771d87dcccf4)

![image](https://github.com/EmilianoAnaya/Spotify-Visualizer/assets/150195114/3bcb4ed9-2698-4449-bbd1-4950ec8cf486)

![image](https://github.com/EmilianoAnaya/Spotify-Visualizer/assets/150195114/e3ba096b-1402-4da7-89f8-34080a6c2b65)
