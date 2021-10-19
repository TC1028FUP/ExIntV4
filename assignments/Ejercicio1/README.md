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

Escribe un programa que genere una lista de numeros de tamaño par, con los datos que ingrese el usuario y posteriormente divide la lista en partes iguales pero de manera intercalada, es decir, el primer dato de la lista se va a la primera lista y el segundo a la segunda y así sucesivamente hasta terminar de repartir los datos. Para lo anterios deberás crear las siguientes funciones.

Función **crea_lista** la cual recibe como parámetro un entero positivo n y cuya funcionalidad es recibir los n números del usuario y va creando una lista con ellos. El mensaje para pedirlos será: **">>>  "** La función deberá regresar la lista creada como resultado de la función.

Función **divide_lista** la cual recibe como parámetro una lista de tamaño par, la función crea una lista anidada con dos listas internas, dividiendo la lista recibida como parámetro en partes iguales pero de manera intercalada, es decir, el primer dato de la lista se va a la primera lista y el segundo a la segunda y así sucesivamente hasta terminar de repartir los datos. La función regresa la lista anidada creada.

En el **main**, se debe desplegar el mensaje **"Ingresa el tamaño de la lista, debe ser par: "**, si el número recibido es par, se ingresan los datos para la lista (llama a la función correspondiente que ya hace esto) y despliega la lista, posteriormente, llama a la función correspondiente que divide la lista en dos, generando la matriz con dos listas internas, despliega las dos listas internas, una en cada renglón. Si el tamaño recibido para los elementos de la lista no es positivo y par, deberá desplegar el mensaje **"Error"** y termina el programa.

## Ejemplo de ejecución del programa
```
Ingresa el tamaño de la lista, debe ser par: 8
>>> 5
>>> 8
>>> 21
>>> 20
>>> 36
>>> 100
>>> 1
>>> 2
[5, 8, 21, 20, 36, 100, 1, 2]
[5, 21, 36, 1]
[8, 20, 100, 2]
```
## Otro ejemplo
```
Ingresa el tamaño de la lista, debe ser par: 3
Error
```

**Nota:** No cambies ni quites el código `if __name__ == '__main__':` 

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
