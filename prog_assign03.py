import random
import time

print("-------------------------------------------------------------------------------------------------")
print("           Random1000    Reverse1000   Random1000    Reverse10000    Random100000    Reverse100000")
print("-------------------------------------------------------------------------------------------------")

#버블정렬
def bubbleSort(a):
  for i in range(1, len(a)):
      for j in range(0, len(a)-1):
          if a[j] > a[j+1]:
             a[j+1], a[j] = a[j], a[j+1]

#선택정렬
def selectionSort(a):
  for i in range(len(a)-1):
      for j in range(i+1, len(a)):
          if a[i] > a[j]:
              a[i] , a[j]  = a[j], a[i]

#삽입정렬
def insertionSort(a):
  for i in range(1, len(a)):
      for j in range(i, 0, -1):
          if a[j] < a[j-1]:
              a[j], a[j-1] = a[j-1], a[j]
          else:
            break

#합병정렬
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

#빠른정렬(첫번째 값, 가운데 위치의 값, 그리고 마지막 값 중에서 중간값을 pivot으로 선택)
def quickSort2(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    lesser_a, equal_a, greater_a = [], [], []
    for num in a:
        if num < pivot:
            lesser_a.append(num)
        elif num > pivot:
            greater_a.append(num)
        else:
            equal_a.append(num)
    return quickSort2(lesser_a) + equal_a + quickSort2(greater_a)

#빠른정렬(pivot을 랜덤하게 선택)
def quickSort3(a, left, right):
  randomIndex = ran.random


#Random1000
n1 = random.sample(range(1, 1001), 1000)
start_vect=time.time()
bubbleSort(n1)
bsn1 = (time.time() - start_vect)
start_vect=time.time()
selectionSort(n1)
ssn1 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n1)
isn1 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n1)
msn1 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n1)
qs2n1 = (time.time() - start_vect)

#Reverse1000
n2 = []
for i in range(1000):
  n2.append(i+1)
start_vect=time.time()
bubbleSort(n2)
bsn2 = (time.time() - start_vect)
start_vect=time.time()
selectionSort(n2)
ssn2 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n2)
isn2 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n2)
msn2 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n2)
qs2n2 = (time.time() - start_vect)

#Random10000
n3 = random.sample(range(1, 1001), 1000)
start_vect=time.time()
bubbleSort(n3)
bsn3 = (time.time() - start_vect)
start_vect=time.time()
selectionSort(n3)
ssn3 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n3)
isn3 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n3)
msn3 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n3)
qs2n3 = (time.time() - start_vect)

#Reverse10000
n4 = []
for i in range(1000):
  n4.append(i+1)
start_vect=time.time()
bubbleSort(n4)
bsn4 = (time.time() - start_vect)
start_vect=time.time()
selectionSort(n4)
ssn4 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n4)
isn4 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n4)
msn4 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n4)
qs2n4 = (time.time() - start_vect)

#Random100000
n5 = random.sample(range(1, 1001), 1000)
start_vect=time.time()
bubbleSort(n5)
bsn5 = (time.time() - start_vect)
start_vect=time.time()
selectionSort(n5)
ssn5 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n5)
isn5 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n5)
msn5 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n5)
qs2n5 = (time.time() - start_vect)

#Reverse100000
n6 = []
for i in range(1000):
  n6.append(i+1)
start_vect=time.time()
bubbleSort(n6)
bsn6 = (time.time() - start_vect)
start_vect=time.time()
selectionSort(n6)
ssn6 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n6)
isn6 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n6)
msn6 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n6)
qs2n6 = (time.time() - start_vect)

print("Bubble     %f      %f      %f      %f        %f        %f"%(bsn1, bsn2, bsn3, bsn4, bsn5, bsn6))
print("Selection  %f      %f      %f      %f        %f        %f"%(ssn1, ssn2, ssn3, ssn4, ssn5, ssn6))
print("Insertion  %f      %f      %f      %f        %f        %f"%(isn1, isn2, isn3, isn4, isn5, isn6))
print("Merge      %f      %f      %f      %f        %f        %f"%(msn1, msn2, msn3, msn4, msn5, msn6))
print("Quick1     %f      %f      %f      %f        %f        %f"%(qs2n1, qs2n2, qs2n3, qs2n4, qs2n5, qs2n6))
print("Quick2     %f      %f      %f      %f        %f        %f"%(qs2n1, qs2n2, qs2n3, qs2n4, qs2n5, qs2n6))
print("Quick3     %f      %f      %f      %f        %f        %f"%(qs2n1, qs2n2, qs2n3, qs2n4, qs2n5, qs2n6))

print("-------------------------------------------------------------------------------------------------")
