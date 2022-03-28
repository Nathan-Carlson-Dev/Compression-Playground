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

    if len(arr) <= 1:
        return arr

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


def LZWEncode(arr, Range):
    dictionary = {}
    (mini, maxi) = Range
    index = 0

    code = [mini, maxi]

    W = [arr[0]]
    for x in range(1, len(arr)):
        checkW = W.copy()
        checkW.append(arr[x])
        checkW = checkW
        if not checkW in dictionary.values():
            dictionary[index] = checkW
            code.append([(k + maxi + 1 if (W == v) else W[0] + 1)
                        for k, v in dictionary.items()][0])
            index += 1
            W = [arr[x]]
        else:
            W = checkW
    code.append([(k + maxi + 1 if (W == v) else W[0])
                for k, v in dictionary.items()][0])
    return code, dictionary


def LZWDecode(arr):
    (mini, maxi) = (arr[0], arr[1])

    W = [arr[2]]
    data = []
    dictionary = {}
    k = 0
    for x in range(2, len(arr) - 1):
        if (arr[x] >= mini and arr[x] <= maxi) or arr[x] in dictionary.keys():
            data.append(arr[x])
            W.append(arr[x])
            dictionary[arr[x]]
