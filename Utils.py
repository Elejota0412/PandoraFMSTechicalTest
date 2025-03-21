import requests #type: ignore
import logging

photosURL = "https://jsonplaceholder.typicode.com/photos/"
albumsURL = "https://jsonplaceholder.typicode.com/albums/"

def getPhotoInfo(number=None):
    url = photosURL

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data if number is None or number <= 0 else data[:number]
        else:
            logging.error(f"Error al realizar la solicitud: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error: {e}")
        return None

def getAlbumInfo(albumID):
    if not albumID:
        return "DEBE COLOCAR EL ID DE UN ÁLBUM VÁLIDO"

    url = f"{albumsURL}{albumID}/"

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error al realizar la solicitud: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error: {e}")
        return None
    
def process_photo(photo):
    album_info = getAlbumInfo(photo["albumId"])
    if album_info and isinstance(album_info, dict):
        return {
            "Modo de ejecución": "Multiprocesos",
            "Foto ID": photo["id"],
            "Título": photo["title"],
            "URL": photo["url"],
            "Álbum ID": album_info["id"],
            "Álbum Título": album_info["title"],
        }
    return None