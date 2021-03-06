import math

def DCT3(arr):
    data = []
    N = len(arr)
    for k in range(0, len(arr)):
        t = 0.5 * arr[0]
        for n in range(1, len(arr)):
            t += arr[n] * math.cos((math.pi/N)*(k + 0.5) * n)
        data.append(t)
    return data

def IDCT2(arr):
    return [int(2 * x/ len(arr) + 0.5) for x in DCT3(arr)]

def DCT2(arr):
    data = []
    N = len(arr)
    for k in range(0, len(arr)):
        t = 0
        for n in range(0, len(arr)):
            t += arr[n]*math.cos((math.pi/N)*(n + 0.5)*k)
        data.append(int(t + 0.5))
    return data