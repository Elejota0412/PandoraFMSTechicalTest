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

   2. Teniendo estas funciones base listas se procedió a la creación de la solución para el modo secuencial (processing_sequential.py) utilizando mi experiencia profesional adquirida anteriormente. Procedí de esta manera porque siento que es el método más básico y me permitió tener una visión más clara y amplia de todo lo que se necesitaba para poder obtener el resultado deseado; primero se hace la consulta a la función base "getPhotoInfo" para obtener toda la información de las fotos, se toma el número de fotos a consultar otorgado por el usuario, en caso de no ortorgarlo se hace la consulta a todas las fotos, una vez se obtiene la información de las fotos por cada una de las fotos obtenidas se recoge su "albumId" con el cual se hace la consulta a la segunda función base "getAlbumInfo" por cada una de las fotos obtenidas para obtener la información pertinente del album al que pertenecen. Una vez obtenida la información necesaria se procede a la construcción del JSON final de salida con la información requerida tanto de la fotos como del album y además se agrega el valor añadido de "Tiempo de ejecución" para saber el tiempo que tarda la consulta en realizarse, usando el módulo "time" para contar el tiempo en el que empieza y el que termina la consulta para luego restar esos valores y obtener el tiempo de ejecución final.
   
   3. Luego seguí con el módulo multihilos (processing_threading.py), el cual como comenté anteriormente tiene la base del secuencial pero optimizado el modulo "threading" para su mejor ejecución. Se comienza por la consulta a la función base "getPhotoInfo" para obtener toda la información de las fotos, se toma el número de fotos a consultar otorgado por el usuario, en caso de no ortorgarlo se hace la consulta a todas las fotos, con el módulo "time" se toma el tiempo en el que empieza y el que termina la consulta para luego restar esos valores y obtener el tiempo de ejecución final, luego se inicializan dos arreglos vacíos para trabajar con ellos más adelante "result" y "threads"; seguidamente se define la función "process_photo" para procesar cada imagen obtenida en la primera consulta de la cual se obtiene su "albumId" con el cual se hace la consulta a la segunda función base "getAlbumInfo" para obtener la información pertinente del album al que pertenecen armando de una vez un JSON de resultado por cada foto y se van guardando en el arreglo previamente definido de "result". Luego se hace la creación y se comienza a ejecutar un nuevo hilo para procesar cada foto que se obtuvo en la consulta incial usando la función "process_photo" que se explica anteriormente. Se hace de esta manera ya que la biblioteca "threading" permite que el procesamiento de las fotos que se obtuvieron ocurra de forma paralela, lo que lograr mejorar el tiempo de ejecución y rendimiento de gran manera, luego se itera sobre cada hilo que se comienza con anterioridad para esperar que todos los hilos terminen de ejecutarse antes de continuar la salida; además se agrega el valor añadido de "Tiempo de ejecución" para saber el tiempo que tarda la consulta en realizarse.
   
   4. Por último se creó el modo multiprocesos (processing_multiprocessing.py), siguiendo igualmente la base del modo secuencial: Se comienza por la consulta a la función base "getPhotoInfo" para obtener toda la información de las fotos, se toma el número de fotos a consultar otorgado por el usuario, en caso de no ortorgarlo se hace la consulta a todas las fotos, con el módulo "time" se toma el tiempo en el que empieza y el que termina la consulta para luego restar esos valores y obtener el tiempo de ejecución final, luego se utiliza la biblioteca multiprocessing para procesar las fotos que se obtuvieron de forma paralela, usando "with multiprocessing.Pool(processes=multiprocessing.cpu_count())" se crea un grupo de procesos en paralelo para ejecutarse al mismo tiempo utilizando el número de núcleos del CPU que están disponibles en la máquina que realiza el proceso con este modo para de esta manera optimizar la consulta y mejorar el rendimiento de la misma al manejar de una mejor forma los recursos que se tiene a la mano. Utilizando la función "map" se utiliza para ejecutar la función "process_photo" la cual está definida en el archivo de funciones basicas también debido a que el modo multiprocesos necesita serializar las funciones y datos a utilizar por lo que dicha funcion no puede estar definida de manera local, luego se filtran los resultados para eliminar cualquier valor resultado que tenga un valor "None", generando así una lista de resultados válidos; además se agrega el valor añadido de "Tiempo de ejecución" para saber el tiempo que tarda la consulta en realizarse.

   5. Debo admitir que con el módulo de multiprocesos tuve un poco de dificultad porque nunca había trabajado de esta manera pero con las consultas a diferentes documentaciones en linea y el apoyo de profesionales allegados a mi pude construir el modo para realizar la consulta de esta forma.

## Cuándo y Por Qué Usar Secuencial, Multihilo o Multiproceso

La diferencia entre los tres procesos es notoria desde su primera ejecución por separado. Como desarrollador de esta solución tengo la siguiente opinión del uso de cada uno de ellos:

   1. Secuencial: el uso del modo secuencial es un metodo para trabajar con cantidades pequeñas, e incluso mucho más recomendable cuando se quiere obtener la información de una imagen en especifico debido a que al ser de manera secuencial la consulta con grandes cantidades de registros o en este caso fotos a consultar genera retraso en el tiempo de respuesta.
   
   2. Multiprocesos: Lo usuaria para trabajar una cantidad más grande de data sin llegar a la cantidad máxima de la misma. Máximo 1000 registros es lo recomendable debido a que pesar que los procesos se realizan de forma paralela cada uno ocupa su propio espacio en memoria y si bien genera a pesar de esto un tiempo de respuesta muchisimo menor al secuencial, sigue siendo un poco "lento" en comparación con el siguiente modo.
   
   3. Multihilos: Lo usaría para trabajar con la cantidad de registros en su totalidad, así como con pequeñas y mediana cantidades. El aprovechamiento de la memoria y la ejecución en paralelo de los distintos hilos hace que este modo sea el más ideal para trabajar con la data permitiendo así compartir datos de manera sencilla y ligera dentro los recursos a utilizar para la ejecución de esta solución.


## Licencia

Este proyecto está bajo la licencia MIT.


## Autores

- Luis José Hidalgo - Desarrollador principal
