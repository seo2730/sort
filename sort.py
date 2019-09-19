import random
from timeit import default_timer as timer

def selection_sort(A) :
    for last in range(len(A)-1,0,-1):
        largest=0
        for i in range(1,last+1):
            if A[i]>A[largest]:
                largest=i
            
        x[largest],x[last] = x[last],x[largest]

####################################################
def bubble_sort(A):
    for last in range(len(A)-1,0,-1):
        sorted = True #finish
        for i in range(last):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                sorted=False #finish
            if sorted: #finish
                break

####################################################
def insertion_sort(A):
    for i in range(1,len(A)):
        loc=i-1
        new_item = A[i]
        while loc>=0 and new_item<A[loc]:
            A[loc+1] = A[loc]
            loc-=1
        A[loc+1]=new_item

####################################################
def merge_sort(A,p,r):
    if p<r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)

        i,j,t=p,q+1,0
        tmp = A[:]

        while i<=q and j<=r:
            if A[i] <= A[j]:
                tmp[t] = A[i]
                i+=1
            else:
                tmp[t] = A[j]
                j+=1
            t+=1

        while i<=q:
            tmp[t] = A[i]
            i+=1
            t+=1
            
        while j<=r:
            tmp[t] = A[j]
            j+=1
            t+=1

        i,t=p,0

        while i<=r:
            A[i] = tmp[t]  
            i+=1
            t+=1

####################################################
def merge_sort_simple(A):
    if len(A)>1:
        mid = len(A)//2
        la,ra=A[:mid],A[mid:]
        merge_sort_simple(la)
        merge_sort_simple(ra)
        li,ri,i=0,0,0
        while li < len(la) and ri < len(ra):
            if la[li] < ra[ri]:
                A[i]=la[li]
                li+=1

            else:
                A[i] = ra[ri]
                ri +=1

            i+=1
        A[i:]=la[li:] if li !=len(la) else ra[ri:]

####################################################
def quick_sort(A):
    if len(A) <= 1:
        return A
    
    x = A[len(A)//2]
    less=[]
    more=[]
    equal=[]

    for a in A:
        if a<x:
            less.append(a)

        elif a>x:
            more.append(a)

        else:
            equal.append(a)

    return quick_sort(less) + equal + quick_sort(more)

####################################################
def partition_1(A,p,r):
    x = A[p]
    left = p+1
    right = r

    while True:
        while left <= right and A[left] <=x:
            left+=1
        while left <= right and x <= A[right]:
            right -=1
        if right < left:
            break
        else:
            A[left],A[right]=A[right],A[left]

    A[p],A[right] = A[right],A[p]
    return right

def qsort_1(A,p,r):
    if p<r:
        q = partition_1(A,p,r)
        qsort_1(A,p,q-1)
        qsort_1(A,q+1,r)

def quick_sort_1(A):
    qsort_1(A,0,len(A)-1)

####################################################
def partition_2(A,p,r):
    x = A[r]
    i=p
    
    for j in range(p,r):
        if A[j] <= x:
            A[i],A[j] = A[j],A[i]
            i+=1

    A[i],A[r] = A[r],A[i]
    return i

def qsort_2(A,p,r):
    if p<r:
        q = partition_2(A,p,r)
        qsort_2(A,p,q-1)
        qsort_2(A,q+1,r)

def quick_sort_2(A):
    qsort_2(A,0,len(A)-1)

####################################################
def heapify(A,k,n):
    largest = k
    left = 2*k+1
    right = 2*k+2
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != k :
        A[k], A[largest] = A[largest], A[k]
        heapify(A,largest,n)

def heap_sort(A):
    n = len(A)
    for i in range(n//2 - 1,-1,-1):
        heapify(A,i,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i)

####################################################
def rsort(A,m):
    buckets = [ [] for _ in range(10)]
    for v in A:
        index = v//(10**m)
        index %= 10
        buckets[index].append(v)
    
    res = []
    for bucket in buckets:
        res.extend(bucket)
    
    return res

def radix_sort(A,k):
    for i in range(0,k):
        A = rsort(A,i)

    return A

def test(A):
    for i in range(1,len(A)):
        if A[i-1]>A[i]:
            return False
        return True
       
####################################################
def counting_sort(A,k):
    B = [0]*len(A)
    C = [0]*(k+1)
    for v in A:
        C[v] +=1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for i in range(len(A)-1,-1,-1):
        v=A[i]
        B[C[v]-1] = v
        C[v] -=1
    
    return B

if __name__ == "__main__":
    x = random.sample(range(10000),100)
    start=timer()
    
    #selection_sort(x)
    #bubble_sort(x)
    #insertion_sort(x)
    #merge_sort(x,0,len(x)-1)
    #merge_sort_simple(x)
    #quick_sort(x)
    #quick_sort_1(x)
    #quick_sort_2(x)
    #heap_sort(x)
    #x = radix_sort(x,4)
    x = counting_sort(x,9999)
    print(timer()-start)
    print(x)
    print(test(x))
