import math

def localFrequencyDecompress(arr):
    data = []
    for x in arr:
        if x >= 0 or isinstance(x, float):
            data.append(x)
        else:
            for _ in range(1, abs(x)):
                data.append(data[len(data) - 1])
    return data

def localFrequencyCompress(arr):
    data = []

    if len(arr) <= 1: return arr

    last = arr[0]
    counter = 0
    for x in arr:
        if x != last:
            if counter == 1:
                data.append(last)
                counter = 1
                last = x
            else:
                data.append(last)
                data.append(-counter)
                counter = 1
                last = x
        else:
            counter += 1
    
    last = arr[len(arr) - 2]
    item = arr[len(arr) - 1]
    if x != last:
        data.append(item)
    else:
        data.append(item)
        data.append(-counter)

    return data