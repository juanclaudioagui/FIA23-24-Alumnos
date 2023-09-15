En el fichero que se acompaña se contiene una versión bastante correcta de la red de metro de madrid.
En cada linea se encuentran los siguientes campos:
* **IdEst**. Es un entero, identificador único de la estación
* **Linea**. Número de línea, alfabético (Hay una línea R). Recuerda que las líneas son bidireccionales, de cabecera a termino, y viceversa.
* **Orden**. Número de Secuencia de la estación en la línea $( 1,2,... n)$
* **Tipo**. Tipo de estación en el línea. Hay varios tipos. **C** para cabecera de una línea normal. **CR** para la primera estación de una línea circular, **T**
  para estación terminal de una línea normal. **TR** para la última estación de una línea circular. e **I** para una estación intermedia de cualquier tipo de línea ( en una línea circular, la **TR** tiene
  a la estación **CR** como siguiente en el sentido y viceversa.
* **Estacion**. Nombre de la estación ( Hemos limpiado caracteres no básicos, no hay 'ñ's ni tildes, ni diéresis...
* **Tarifa**. La zona tarifaria en la que está la estación, por si quieres enseñar al buscador a 
* **x,y** . Coordenas UMT de la estación
* **DIRECCION**. La dirección oficial de la misma, por si utilizas callejeros

Es importante recordar que cuando varias líneas se cruzan en una estación, cada una de ellas tiene su registro, ya que la línea, el orden, y el tipo pueden cambiar. Ello es lo que permite el transbordo, como cambio, dentro de una estación de una línea a otra.

Todo este contenido es el postproceso de datos públicos que pueden encontrarse en https://datos.crtm.es/
