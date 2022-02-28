def localFrequencyFCompress(arr):
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
        data.append(-(counter + 1))

    print("Local Frequency Compression: " + str(round(100 - len(data)/len(arr) * 100, 2)) + "% less than the original size")

    return data

if __name__ == "__main__":
    arr = [3, 2, 1, 3, 3, 1, 2, 2, 2, 3, 1, 2, 2, 3, 1, 2, 3, 1, 2, 2, 3]
    data = localFrequencyFCompress(arr)
    print(data)