import time
import threading
from Utils import getPhotoInfo, getAlbumInfo #type: ignore
import logging

def getPhotoAlbumInfoThreaded(number, albumID=None):
    try:
        start_time = time.time()

        photosInfo = getPhotoInfo(number)
        if not photosInfo:
            return "ERROR AL OBTENER LAS FOTOS DESDE LA URL"

        result = []
        threads = []

        def process_photo(photo):
            album_info = getAlbumInfo(photo["albumId"])

            if album_info and isinstance(album_info, dict):
                json_dict = {
                    "Modo de ejecución": "Multihilos",
                    "Foto ID": photo["id"],
                    "Título": photo["title"],
                    "URL": photo["url"],
                    "Álbum ID": album_info["id"],
                    "Álbum Título": album_info["title"],
                }
                result.append(json_dict)

        for photo in photosInfo:
            thread = threading.Thread(target=process_photo, args=(photo,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.time()
        total_time = end_time - start_time

        return {
            "resultados": result,
            "Tiempo total de ejecución": total_time
        }

    except Exception as e:
        logging.error(f"Error: {e}")
        return None