# -*- coding: utf-8 -*-

import argparse
import logging
import time
import json

from processing_sequential import getPhotoAlbumInfo                                 #type: ignore
from processing_threading import getPhotoAlbumInfoThreaded                          #type: ignore
from processing_multiprocessing import getPhotoAlbumInfoMultiprocessing             #type: ignore

logging.basicConfig(
    filename='appPandora.log',
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obtener información de fotos y álbumes desde JSONPlaceholder API.")
    parser.add_argument("-photos", "--photos", type=int, help="Cantidad de fotos a obtener (opcional)")
    parser.add_argument("-mode", "--mode", choices=["secuencial", "multihilos", "multiprocesos"], default="multiprocesos",
                        help="Modo de ejecución: secuencial, multihilos o multiprocesos")

    args = parser.parse_args()

    if args.mode == "secuencial":
        photo_album_info = getPhotoAlbumInfo(args.photos, None)
    elif args.mode == "multihilos":
        photo_album_info = getPhotoAlbumInfoThreaded(args.photos, None)
    else:
        photo_album_info = getPhotoAlbumInfoMultiprocessing(args.photos, None)

    print(json.dumps(photo_album_info, ensure_ascii=False, indent=4))

    logging.info(json.dumps(photo_album_info, ensure_ascii=False, indent=4))