import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Twoje dane uwierzytelniające Spotify API. plik .env
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Zakresy dostępu
SCOPE = 'user-top-read user-read-recently-played user-read-playback-state user-modify-playback-state user-read-currently-playing'

# Konfiguracja uwierzytelniania
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    show_dialog=True,  # Wyświetl okno logowania za każdym razem
    cache_path='token.json'  # Zapisuje token do pliku
))

def test(x) -> None:
    
    test = json.dumps(x, indent=4)
    with open("test.json", "w") as file:
        file.write(test)
        

def get_recent_tracks(limit=5) -> None:
    
    recent = sp.current_user_recently_played(limit)
    
    print("\nTwoje ostatnio odtwarzane utwory:")

    for idx, item in enumerate(recent['items'], start=1):
        track = item['track']
        print(f"{idx}. {track['name']} - {track['artists'][0]['name']}")


def get_current_track() -> None:
    
    current = sp.current_user_playing_track()
    
    print("\nAktualnie odtwarzane")
    
    try:
        print(f"{current['item']['name']} - {current['item']['artists'][0]['name']}")
    except:
        print("Brak")

    
def get_top_tracks(limit=5) -> None:
    
    top = sp.current_user_top_tracks(limit)
    
    print("\nUlubione utwory:")
    
    for idx, item in enumerate(top['items'], start=1):
        print(f"{idx}. {item['name']} - {item['artists'][0]['name']}")
        
        
if __name__ == "__main__":
    #get_recent_tracks(5)
    get_top_tracks(5)
    get_current_track()
    
    #input()
    print()