arr = []

def inputarr():
    x=int(input("Masukan tinggi badan : "))
    while x!=0:
        arr.append(x)
        x=int(input("Masukan tinggi badan : "))
        

def armax(arr):
    max=0
    for i in range(len(arr)):
        if(arr[i]>max):
            max=arr[i]
        
    return max


def armin(arr):
    min=arr[0]
    for i in range(len(arr)):
        if(arr[i]<min):
            min=arr[i]
        
    return min

def arav(arr):
    sum=0
    for i in range(len(arr)):
        sum = sum+arr[i]
    return sum/len(arr)

def arrange(num1, num2):
    if(num1>num2):
        return num1-num2
    else:
        return num2-num1


inputarr()
print("\n\n")
print("Badan tertinggi ",armax(arr))
print("Badan terpendek ",armin(arr))
print("Rata-rata tinggi badan",arav(arr))
print("Range tinggi badan",arrange(armax(arr),armin(arr)))