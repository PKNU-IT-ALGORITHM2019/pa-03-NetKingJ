import random
import time

def swap(x, i, j):
  x[i], x[j] = x[j], x[i]

a = random.sample(range(1, 1001), 1000)

print("───────────────────────────────────────────────────────────────────────────────────────────────────")
print("           Random1000    Reverse1000   Reandom1000   Reverse10000    Rabdin100000    Reverse100000")
print("───────────────────────────────────────────────────────────────────────────────────────────────────")

#빠른정렬(마지막 값을 피봇으로 선택)
#def quickSort(A[], p, r):
#  if p<r:
#    q=partition(A, p, r)
#    quickSort(A, p, q-1)
#    quickSort(A, q+1, r)

#def partition(A[], p, r):
#  x = A[r]
#  i = p-1
#  for j=p in range(r-1):
#    if A[j]<=x:
#      i=i+1
#      A[i], A[j] = A[j], A[i]
#    A[i+1], A[r] = A[r], A[i+1]
#    return i+1

start_vect=time.time()
def quickSort(a, start, end):
    if start < end:
        left = start
        pivot = a[end]
        for i in range(start, end): 
            if a[i] < pivot:
                a[i], a[left] = a[left], a[i]
                left += 1
        a[left] , a[end] = a[end], a[left]
        quickSort(a, start, left-1)
        quickSort(a, left+1, end)
quickSort(a, 0, len(a)-1)
print("Quick1     %f"%((time.time() - start_vect)))

#빠른정렬(첫번째 값, 가운데 위치의 값, 그리고 마지막 값 중에서 중간값을 pivot으로 선택)

#빠른정렬(pivot을 랜덤하게 선택)

#버블정렬
start_vect=time.time()
for i in range(1, len(a)):
    for j in range(0, len(a)-1):
        if a[j] > a[j+1]:
           a[j+1], a[j] = a[j], a[j+1]
print("Bubble     %f"%((time.time() - start_vect)))

#선택정렬
start_vect=time.time()
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i] , a[j]  = a[j], a[i]
print("Selection  %f"%((time.time() - start_vect)))

#삽입정렬
start_vect=time.time()
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
          break
print("Insertion  %f"%((time.time() - start_vect)))

#합병정렬
#def mergeSort(A[], p, r):
#  if p < r:
#    q = (p+q)/2
#    mergeSort(A, p, q)
#    mergeSort(A, q+1, r)
#    merge(A, p, q, r)

#def merge(A[], p, q, r):
#  i, j, k = p, q+1, p
#  tmp = []
#  while i<=q and j<=r:
#    if data[i] <= data[j]:
#      tmp[k++]=data[i++]
#    else:
#      tmp[k++]=data[j++]
#  while i<=q:
#    tmp[k++]=data[i++]
#  while j<=r:
#    tmp[k++]=data[j++]
#  for i in range(p, r+1):
#    data[i]=tmp[i]

start_vect=time.time()
def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        la, ra = a[:mid], a[mid:]
        mergeSort(la)
        mergeSort(ra)
        li, ri, i = 0, 0, 0
        while li < len(la) and ri < len(ra):
            if la[li] < ra[ri]:
                a[i] = la[li]
                li += 1
            else:
                a[i] = ra[ri]
                ri += 1
            i += 1
        a[i:] = la[li:] if li != len(la) else ra[ri:]
mergeSort(a)
print("Merge      %f"%((time.time() - start_vect)))
print("───────────────────────────────────────────────────────────────────────────────────────────────────")
