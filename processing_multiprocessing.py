import time
import multiprocessing
from Utils import getPhotoInfo, getAlbumInfo, process_photo #type: ignore
import logging

def getPhotoAlbumInfoMultiprocessing(number, albumID=None):
    try:
        start_time = time.time()

        photosInfo = getPhotoInfo(number)
        if not photosInfo:
            logging.error(f"Error inesperado en la consulta: {photosInfo}")
            return f"Error inesperado en la consulta: {photosInfo}"

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.map(process_photo, photosInfo)

        result = [r for r in results if r is not None]

        end_time = time.time()
        total_time = end_time - start_time

        return {
            "resultados": result,
            "Tiempo total de ejecución": total_time
        }

    except Exception as e:
        logging.error(f"Error: {e}")
        return None
