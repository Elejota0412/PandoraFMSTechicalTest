import time
from Utils import getPhotoInfo, getAlbumInfo, process_photo #type: ignore
import logging

def getPhotoAlbumInfo(number, albumID):
    try:
        start_time = time.time()

        photosInfo = getPhotoInfo(number)
        if not photosInfo:
            logging.error("Error al obtener las fotos desde la URL.")
            return {"error": "ERROR AL OBTENER LAS FOTOS DESDE LA URL"}

        result = []

        for photo in photosInfo:
            album_info = getAlbumInfo(photo["albumId"])

            if album_info and isinstance(album_info, dict):
                json_dict = {
                    "Modo de ejecución": "Secuencial",
                    "Foto ID": photo["id"],
                    "Título": photo["title"],
                    "URL": photo["url"],
                    "Álbum ID": album_info["id"],
                    "Álbum Título": album_info["title"],
                }
                result.append(json_dict)
            else:
                logging.warning(f"Álbum con ID {photo['albumId']} no encontrado o es inválido.")
                return f"Error: Álbum con ID {photo['albumId']} no encontrado o es inválido."

        end_time = time.time()
        total_time = end_time - start_time

        return {
            "resultados": result,
            "Tiempo total de ejecución": total_time
        }
    except Exception as e:
        logging.error(f"Error al procesar la información del álbum: {e}")
        return {"error": f"Error al procesar la información: {e}"}