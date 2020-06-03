# Funciones

* En `python` las funciones tienen el tipo `Function` y se pueden asignar a variables o pasar como argumentos.
* Es un bloque de codigo reusable (es como una caja negra con entrada y salida)
* (RETURN)
  * UNA FUNCION QUE NO TIENE RETURN DEVUELVE `None`
  * Puede devolver mas de una cosa
  * El return no es obligatorio
  * Puede haber mas de un return
  
## (Parámetros & Argumentos) 

Las funciones se le pasan argumentos (respecto a la llamada) y reciben parámetros (respecto la firma de una función)

* Argumentos y Parametros son opcionales. Puede haber funciones que no recibir ningún argumento
  
* El orden IMPORTA:

```python
def miriam(x,y):
    return x
x = 4
y = 3
miriam(y,x)
```

* El numero de parametros que defines es el mismo con el que tienes que llamar a una función
  
* PARAMETROS POR DEFECTO El numero de argumentos y parametros para una misma función puede variar. Ejemplo, se puede llamar a una función definida con 2 parametro usando solo un argumento
  
```python
def suma(x,y,z=10):
    return x+y+z
suma(5,8)
```

## TIPOS DE FUNCIONES

* PURAS: La salida depende SOLO de los parametros de entrada
* IMPURAS: La salida depende de variables/funciones globales fuera del scope.
* DETERMINISTAS: bajo los mismos argumentos, siempre devuelve lo mismo
* NO-DETERMINISTAS: devuelve una cosa diferente cada vez que la llamas


## Estructura
  
* Variables GLOBALES respecto todas las funciones
* Variables LOCALES respecto de la propia funcion

```python
nombre="Pepe"

def saluda(nombre):
    nombre="Juan"
    print("Hola", nombre)
nombre="Luis"
saluda(nombre)
```

## Otros

* Se puede definir una función dentro de otra. La función definida esta en el SCOPE de la funcion padre.
* RECURSIVIDAD: Una función se puede llamar a si misma.
* Las funciones, si se definen con def siempre hay que poner un nombre. Pero pueden tener o no nombre🚧 (funciones anónimas `lambda` en python)

* Se definen con la palabra `def` (en python)
  - Se pueden definir en cualquier parte del código

* En python, hay funciones ya existentes (built-in functions) (len, range, zip, max, min, print, etc...)



# Funciones
* ☢️Es un bloque de código Reusable (como una caja negra)
    * Se usa el pass para no escribir bloque de codigo y evitar un SyntaxError
    * Un "fn" puede tener varios nombres (funcion como objecto o tipo de dato)
* ☢️ ABSTRACIÓN
* TIPOS DE FUNCIONES
    * PURAS (su valor de salida solo depende de los datos de entrada)
    * IMPURAS (su valor de salida depende de los datos en entrada y el contexto "scope" global)
    * DETERMINISTAS (los mismos valores de entrada producen las mismas salidas)
    * NO-DETERMINISTAS (los mismos valores de entrada producen diferentes salidas)
* (CALL) Se pueden llamar
    * dentro de una función puedes llamar también a otra función
    * se puede definir una función dentro de otra
    * RECURSIVIDAD: Una función se puede llamar a si misma
* (ARGS & PARAMS) Las funciones se le pasan argumentos (respecto a la llamada) y reciben parámetros (respecto la firma de una función)
    * Ojo: Puede haber funciones que no recibir ningún argumento
    * El numero de argumentos y parametros para una misma función puede variar en número. Ejemplo, se puede llamar a una misma función con 2,3 o mas argumentos.
    * El orden IMPORTA
    * Existen los parámetros con un valor POR DEFECTO
* Se definen con `def` (en python)
    * Se pueden definir en cualquier parte del código
* (RETURN) Devuelve un valor
    * No es obligatorio poner return
    * puede devolver una estructura de datos con multiples cosas
    * **UNA FUNCIÓN QUE NO TIENE RETURN DEVUELVE None**
        * Por ejemplo: print, que devuelve none pero realiza la tarea de imprimir por consola (stdout)
* En python, hay funciones ya existentes (built-in functions) (len, range, zip, max, min, print, etc...)
* (STRUCTURE)
    * Variables locales: Las variables definidas dentro de una función solo son accesibles desde dentro de esta
    * Variables globales: Son variables definidas fuera de una función, desde dentro se pueden leer y modificar
* Las funciones también se llaman métodos cuando pertenecen a un objeto
    * Una función no es un método
    * Un método si es una función
* **CALLBACK**: Una función recibie como argumento otra función


