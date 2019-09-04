import random
from timeit import default_timer as timer

def selection_sort(A) :
    for last in range(len(A)-1,0,-1):
        largest=0
        for i in range(1,last+1):
            if A[i]>A[largest]:
                largest=i
            
        x[largest],x[last] = x[last],x[largest]

def bubble_sort(A):
    for last in range(len(A)-1,0,-1):
        sorted = True #finish
        for i in range(last):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                sorted=False #finish
            if sorted: #finish
                break

def insertion_sort(A):
    for i in range(1,len(A)):
        loc=i-1
        new_item = A[i]
        while loc>=0 and new_item<A[loc]:
            A[loc+1] = A[loc]
            loc=loc-1
        A[loc+1]=new_item

def test(A):
    for i in range(1,len(A)):
        if A[i-1]>A[i]:
            return False
        return True


if __name__ == "__main__":
    x = random.sample(range(10000),100)
    start=timer()
    insertion_sort(x)
    #bubble_sort(x)
    #selection_sort(x)
    print(timer()-start)
    print(x)
    print(test(x))