# TECHNICAL TEST PANDORAFMS

##Descripcion
A continuación se desgloza la siguiente aplicación para ser ejecutada en CLI en Python, la cual obtiene información detallada de las fotos indicando hasta el album al cual pertenece siguiendo criterios como la cantidad de fotos indicadas por el usuario en consola.

## Instalación

1. Clona el repositorio:  
   `git clone https://github.com/usuario/proyecto.git`
2. Instala las dependencias:
   `pip install -r requirements.txt`

## Uso

Para ejecutar el script dentro de tu CLI, se pueden utilizar los siguientes comando según sea el caso:

python main.py -photos n -mode modoUtilizado

Donde "n" representa el número de fotos del cual deseas obtener información, a su vez se aclara que de no establecer el mismo, el número de fotos será automáticamente la cantidad de fotos completas que posee el endpoit. Por otra parte, "modoUtilizado" se refiera al modo que deseas utilizar para hacer la consulta, dichos modos pueden ser: secuencial, multihilos y multiprocesos. De no especificar ninguno de estos se tomará como default el método "multiprocesos" para ofrecer los resultados esperados.

## Licencia

Este proyecto está bajo la licencia MIT.

## Autores

- Luis José Hidalgo - Desarrollador principal
