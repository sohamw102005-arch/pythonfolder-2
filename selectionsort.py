arr=[]

n= int(input("enter the number of element"))

for i in range(n):
    num = int(input("enter the number of element"))
    arr.append(num)


for i in range(n):
    min_index =i

for j in range(i+1, n):
      if arr[j] < arr[ min_index]:
      min_index =j

  arr[i] , arr[min_index] = arr[min_index] , arr[i]

print("sorted array")
print(arr)
