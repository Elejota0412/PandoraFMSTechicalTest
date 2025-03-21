import requests #type: ignore
import logging 

photosURL = "https://jsonplaceholder.typicode.com/photos/"
albumsURL = "https://jsonplaceholder.typicode.com/albums/"

def getPhotoInfo(self, number):
    url = photosURL

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            if number is not None and number > 0:
                limited_data = data[:number]
            else:
                limited_data = data
            
            return limited_data
        else:
            logging.error("Error al realizar la solicitud:", response.status_code)
            return None
    except Exception as e:
        logging.error("Error:", e)
        return None

def getAlbumInfo(self, albumID):
    pass

def getPhotoAlbumInfo(self):
    pass