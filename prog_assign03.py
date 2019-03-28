import random
import time
import sys
sys.setrecursionlimit(100000000) #재귀호출 한도 10000000

print("---------------------------------------------------------------------------------------------------")
print("           Random1000    Reverse1000   Random10000    Reverse10000    Random100000    Reverse100000")
print("---------------------------------------------------------------------------------------------------")

#버블정렬
def bubbleSort(a):
  for i in range(len(a)-1):
      for j in range(len(a)-1):
          if a[j] > a[j+1]:
             a[j+1], a[j] = a[j], a[j+1]
  return a

#선택정렬
def selectionSort(a):
  for sel in range( len(a) - 1 ):
    min = a[sel]
    minindex = sel
    for step in range( sel + 1, len(a) ):
      if min > a[step]:
        min = a[step]
        minindex = step            
    a[minindex] = a[sel]
    a[sel] = min
  return a

#삽입정렬
def insertionSort(a):
  for i in range(1, len(a)):
      for j in range(i, 0, -1):
          if a[j] < a[j-1]:
              a[j], a[j-1] = a[j-1], a[j]
          else:
            break
  return a

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
    return a

#빠른정렬(마지막 값을 피봇으로 선택)
def quickSort1(a, lo, hi):
  if lo < hi:
    p = partition1(a, lo, hi)
    quickSort1(a, lo, p-1)
    quickSort1(a, p+1, hi)
  return a

def partition1(a, lo, hi):
  x = a[hi]
  i = lo - 1
  for j in range(lo, hi):
    if a[j] <= x:
      i = i + 1
      a[i], a[j] = a[j], a[i]
  a[i+1], a[hi] = a[hi], a[i+1]
  return i + 1

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
def quickSort3(A, lo, hi):
  if lo < hi:
      p = partition3(A, lo, hi)
      quickSort3(A, lo, p-1)
      quickSort3(A, p+1, hi)
  return A

def partition3(A, lo, hi):
  pivotIndex = random.randint(lo, hi)
  pivotValue = A[pivotIndex]
  A[pivotIndex], A[hi] = A[hi], A[pivotIndex]
  storeIndex = lo
  for i in range(lo, hi):
      if A[i] < pivotValue:
          A[i], A[storeIndex] = A[storeIndex], A[i]
          storeIndex += 1
  A[storeIndex], A[hi] = A[hi], A[storeIndex]
  return storeIndex

#힙정렬
def heapSort(unsorted_list):
  parent_node = (int)((len(unsorted_list) - 2) / 2)
  
  for parent in range(parent_node, -1, -1):
      build_max_heap(unsorted_list, parent, len(unsorted_list) - 1)
      
  for sorted_num in range(len(unsorted_list) - 1, 0, -1):
      unsorted_list[sorted_num], unsorted_list[0] =\
          unsorted_list[0], unsorted_list[sorted_num]
      build_max_heap(unsorted_list, 0, sorted_num - 1)
  return unsorted_list

def build_max_heap(maxheap_list, parent, end):
  child = parent * 2 + 1
    
  while child <= end:
      if child + 1 <= end and maxheap_list[child] < maxheap_list[child + 1]:
          child += 1
        
      if maxheap_list[parent] < maxheap_list[child]:
          maxheap_list[parent], maxheap_list[child] =\
              maxheap_list[child], maxheap_list[parent]
          parent = child
          child = parent * 2 + 1
      else:
          break

#라이브러리(표준 라이브러리가 제공하는 정렬 알고리즘)
def library(a):
  a.sort()
  return a

#Random1000
n1 = [random.randint(1, 1000) for _ in range(1000)]
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
quickSort1(n1, 0, len(n1)-1)
qs1n1 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n1)
qs2n1 = (time.time() - start_vect)
start_vect=time.time()
quickSort3(n1, 0, len(n1)-1)
qs3n1 = (time.time() - start_vect)
start_vect=time.time()
heapSort(n1)
hsn1 = (time.time() - start_vect)
start_vect=time.time()
library(n1)
lbn1 = (time.time() - start_vect)

#Reverse1000
n2 = []
for i in range(1000):
  n2.append(i+1)
n2.reverse()
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
quickSort1(n2, 0, len(n2)-1)
qs1n2 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n2)
qs2n2 = (time.time() - start_vect)
start_vect=time.time()
quickSort3(n2, 0, len(n2)-1)
qs3n2 = (time.time() - start_vect)
start_vect=time.time()
heapSort(n2)
hsn2 = (time.time() - start_vect)
start_vect=time.time()
library(n2)
lbn2 = (time.time() - start_vect)

#Random10000
n3 = [random.randint(1, 10000) for _ in range(10000)]
start_vect=time.time()
#bubbleSort(n3)
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
#quickSort1(n3, 0, len(n3)-1)
qs1n3 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n3)
qs2n3 = (time.time() - start_vect)
start_vect=time.time()
quickSort3(n3, 0, len(n3)-1)
qs3n3 = (time.time() - start_vect)
start_vect=time.time()
heapSort(n3)
hsn3 = (time.time() - start_vect)
start_vect=time.time()
library(n3)
lbn3 = (time.time() - start_vect)

#Reverse10000
n4 = []
for i in range(100000):
  n4.append(i+1)
n4.reverse()
start_vect=time.time()
#bubbleSort(n4)
bsn4 = (time.time() - start_vect)
start_vect=time.time()
#selectionSort(n4)
ssn4 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n4)
isn4 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n4)
msn4 = (time.time() - start_vect)
start_vect=time.time()
#quickSort1(n4, 0, len(n4)-1)
qs1n4 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n4)
qs2n4 = (time.time() - start_vect)
start_vect=time.time()
quickSort3(n4, 0, len(n4)-1)
qs3n4 = (time.time() - start_vect)
start_vect=time.time()
heapSort(n4)
hsn4 = (time.time() - start_vect)
start_vect=time.time()
library(n4)
lbn4 = (time.time() - start_vect)

#Random100000
n5 = [random.randint(1, 100000) for _ in range(100000)]
start_vect=time.time()
#bubbleSort(n5)
bsn5 = (time.time() - start_vect)
start_vect=time.time()
#selectionSort(n5)
ssn5 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n5)
isn5 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n5)
msn5 = (time.time() - start_vect)
start_vect=time.time()
#quickSort1(n5, 0, len(n5)-1)
qs1n5 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n5)
qs2n5 = (time.time() - start_vect)
start_vect=time.time()
quickSort3(n5, 0, len(n5)-1)
qs3n5 = (time.time() - start_vect)
start_vect=time.time()
heapSort(n5)
hsn5 = (time.time() - start_vect)
start_vect=time.time()
library(n5)
lbn5 = (time.time() - start_vect)

#Reverse100000
n6 = []
for i in range(10000):
  n6.append(i+1)
n6.reverse()
start_vect=time.time()
#bubbleSort(n6)
bsn6 = (time.time() - start_vect)
start_vect=time.time()
#selectionSort(n6)
ssn6 = (time.time() - start_vect)
start_vect=time.time()
insertionSort(n6)
isn6 = (time.time() - start_vect)
start_vect=time.time()
mergeSort(n6)
msn6 = (time.time() - start_vect)
start_vect=time.time()
#quickSort1(n6, 0, len(n6)-1)
qs1n6 = (time.time() - start_vect)
start_vect=time.time()
quickSort2(n6)
qs2n6 = (time.time() - start_vect)
start_vect=time.time()
quickSort3(n6, 0, len(n6)-1)
qs3n6 = (time.time() - start_vect)
start_vect=time.time()
heapSort(n6)
hsn6 = (time.time() - start_vect)
start_vect=time.time()
library(n6)
lbn6 = (time.time() - start_vect)

print("Bubble     %f      %f      %f       %f        %f        %f"%(bsn1, bsn2, bsn3, bsn4, bsn5, bsn6))
print("Selection  %f      %f      %f       %f        %f        %f"%(ssn1, ssn2, ssn3, ssn4, ssn5, ssn6))
print("Insertion  %f      %f      %f       %f        %f        %f"%(isn1, isn2, isn3, isn4, isn5, isn6))
print("Merge      %f      %f      %f       %f        %f        %f"%(msn1, msn2, msn3, msn4, msn5, msn6))
print("Quick1     %f      %f      %f       %f        %f        %f"%(qs1n1, qs1n2, qs1n3, qs1n4, qs1n5, qs1n6))
print("Quick2     %f      %f      %f       %f        %f        %f"%(qs2n1, qs2n2, qs2n3, qs2n4, qs2n5, qs2n6))
print("Quick3     %f      %f      %f       %f        %f        %f"%(qs3n1, qs3n2, qs3n3, qs3n4, qs3n5, qs3n6))
print("Heap       %f      %f      %f       %f        %f        %f"%(hsn1, hsn2, hsn3, hsn4, hsn5, hsn6))
print("Library    %f      %f      %f       %f        %f        %f"%(lbn1, lbn2, lbn3, lbn4, lbn5, lbn6))

print("---------------------------------------------------------------------------------------------------")
