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


# Resumen de la Experiencia

## Lógica de Evaluación del Problema

La lógica utilizada para la resolución de este problema comienza desde la utilización de diferentes archivos para el manejo de cada uno de los distintos modos con los que se pueden obtener resultados en esta aplicación hasta la separación de las funciones dentro de los ya mencionados archivos. La solución implementada en mi caso fue la siguiente, descrita a continuación:
   
   1. Creación del archivo Utils.py para desarrollar 3 funciones básicas que sirven para cada uno de los métodos que se van a utilizar dentro del archivo main.py como lo son:
      1.1. getPhotoInfo: función encargada de recopilar la información de las fotos tomando en cuenta un valor que puede ser o no indicado.
      1.2. getAlbumInfo: función encargada de recopilar la información de un album especifico tomando en cuenta un valor que debe ser indicado.
      1.3  process_photo: esta función se encarga de ejecutar "getAlbumInfo" ya que el modo multiprocesos necesita serializar las funciones y datos a utilizar por lo que dicha funcion no puede estar definida de manera local dentro del archivo que maneja este proceso.

   2. Teniendo estas funciones base listas se procedió a la creación de la solución para el modo secuencial utilizando la experiencia adquirida anteriormente. Procedí de esta manera porque siento que es el método más básico y me permitió tener una visión más clara y amplia de todo lo que se necesitaba 


## Cuándo y Por Qué Usar Secuencial, Multihilo o Multiproceso
La diferencia entre los tres procesos es notoria desde su primera ejecución por separado. Como desarrollador de esta solución tengo la siguiente opinión del uso de cada uno de ellos:
   1. Secuencial: el uso del modo secuencial es un metodo para trabajar con cantidades pequeñas, e incluso mucho más recomendable cuando se quiere obtener la información de una imagen en especifico debido a que al ser de manera secuencial la consulta con grandes cantidades de registros o en este caso fotos a consultar genera retraso en el tiempo de respuesta.
   2. Multiprocesos: Lo usuaria para trabajar una cantidad más grande de data sin llegar a la cantidad máxima de la misma. Máximo 1000 registros es lo recomendable debido a que pesar que los procesos se realizan de forma paralela cada uno ocupa su propio espacio en memoria y si bien genera a pesar de esto un tiempo de respuesta muchisimo menor al secuencial, sigue siendo un poco "lento" en comparación con el siguiente modo.
    3. Multihilos: Lo usaría para trabajar con la cantidad de registros en su totalidad, así como con pequeñas y mediana cantidades. El aprovechamiento de la memoria y la ejecución en paralelo de los distintos hilos hace que este modo sea el más ideal para trabajar con la data permitiendo así compartir datos de manera sencilla y ligera dentro los recursos a utilizar para la ejecución de esta solución.


## Licencia

Este proyecto está bajo la licencia MIT.


## Autores

- Luis José Hidalgo - Desarrollador principal
