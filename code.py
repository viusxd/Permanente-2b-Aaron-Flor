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


n = 15000

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
