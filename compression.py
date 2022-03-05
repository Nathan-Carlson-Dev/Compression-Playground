import math
import Compression_Algorithms.DCT_Compressions as dctc

if __name__ == "__main__":
    arr = [1, 1, 1, 2, 2, 1, 5, 5, 1]
    
    freq = {}
    
    for x in arr:
        if x in freq.keys():
            freq[x] += 1
        else:
            freq[x] = 1
    
    sum = 0
    for x in freq.values():
        sum += x

    print("average frequency: " + str(sum/(max(freq.keys()) - min(freq.keys()) + 1)))
    print(dctc.DCT2Decompress(dctc.DCT2Compress(arr, 2)))