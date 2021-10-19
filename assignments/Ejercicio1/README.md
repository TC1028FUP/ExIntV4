![Tec de Monterrey](../../images/logotecmty.png)
# Divide una lista por número de caracteres
## Involucra ciclos, listas, condicionales

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
# Area de funciones aquí

def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

Diseña e implementa un programa que recibe números positivos para conformar una lista, la despliega a pantalla y posteriormente procesa esa lista y construye dos más, donde en la primera están los números mútiplos de n y en otra lista donde están los que no son múltiplos de n. Para lo anterior DEBES CREAR las siguientes funciones en tu programa:

Función **crea_lista** la cual no tiene parámetros y cuya funcionalidad es recibir números del usuario y va creando una lista con ellos. El mensaje para pedirlas será: **">>>  "** El proceso de recepción de números termina cuando el usuario ingresa un número negativo. La función deberá regresar la lista creada como resultado de la función.

Función **divide_lista** la cual recibe como parámetro una lista y un número n, la función crea una lista anidada con dos listas internas, donde la primera tiene los números que son múltiplos de n y en la segunda los que no son múltiplos de n. La función regresa la lista anidada.

En el **main**, se debe desplegar el mensaje **"Ingresa números positivos, para terminar de capturar ingresa un negativo"**, luego se ingresan los datos para la lista (llama a la función correspondiente) y despliega la lista, posteriormente, pide el número del cuál quieres identificar múltiplos con este mensaje: **"Múltiplos de: "** y luego llama a la función correspondiente para que divida la lista de acuerdo a los que son múltiplos de ese número n y los que no. Por último despliega las dos listas, una en cada renglón, primero la de múltiplos de n y luego de la lista de los que no son múltiplos. Nota: El número para determinar si son múltiplos deberá ser mayor que cero, de lo contrario, deberá desplegar el mensaje "Error" y termina el programa.

## Ejemplo de ejecución del programa
```
Ingresa números positivos, para terminar de capturar ingresa un negativo
>>> 5
>>> 8
>>> 21
>>> 20
>>> 36
>>> 100
>>> -1
[5, 8, 21, 20, 36, 100]
Múltiplos de: s
[5, 20, 100]       
[8, 21, 36]
```
.


**Nota:** No cambies ni quites el código `if __name__ == '__main__':` 

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
