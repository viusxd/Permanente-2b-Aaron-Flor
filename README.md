# Permanente 2b

## Acerca

* El trabajo consiste en implementar y comparar ambos algoritmos, los dos tratan de ordenar diferentes elementes en una lista con la diferencia de que se ordenan de distinta manera.

## Vea ambos algoritmos

```python
def INSERTION_SORT(A):

    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

def BUBBLESORT(L):

    n = len(L)

    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                key = L[j]
                L[j] = L[j - 1]
                L[j - 1] = key
    return L

```

## Tabla de contenidos

Use for instance <https://github.com/viusxd/Permanente-2b-Aaron-Flor>:

> * [Permanente 2b](#Permanente-2b)
>   * [Acerca](#Acerca)
>   * [Tabla de contenidos](#tabla-de-contenidos)
>   * [Cómo usar](#Cómo-usar)
>     * [Screenshots](#screenshots)
>   * [Code](#code)

## Como usar

* Para poder usar estos algoritmos y poder compararlos es necesario cambiar el valor de n dentro del código.

### Screenshots

![unknown](https://user-images.githubusercontent.com/102131155/173859409-fa11068e-7e0d-4d65-afb6-203bba0cedd6.jpg)

## Gráfico y comparación

![WhatsApp Image 2022-06-15 at 12 54 48 PM](https://user-images.githubusercontent.com/102131155/173893302-a689bc8e-e08f-484f-a2dd-1104712f7f6e.jpeg)

## Code

```python

import random
import time

def INSERTION_SORT(A):

    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

def BUBBLESORT(L):

    n = len(L)

    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                key = L[j]
                L[j] = L[j - 1]
                L[j - 1] = key
    return L


n = 15000 #Valor de n que debe ser cambiado para poder comparar

lista = list(range(n))

random.shuffle(lista)

i_tiempo = time.time()
l_ordenada = INSERTION_SORT(lista)
f_tiempo = time.time()
print(f_tiempo - i_tiempo)

random.shuffle(lista)

i_tiempo = time.time()
l_ordenada = BUBBLESORT(lista)
f_tiempo = time.time()

print(f_tiempo - i_tiempo)


```

