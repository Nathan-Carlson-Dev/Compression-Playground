import time
import random
import math
import Compression_Algorithms.Aux_Compressions as aux
import DCT_Algorithms as dct
import Compression_Algorithms.DCT_Compressions as dctc

if __name__ == "__main__":
    start = time.time()
    arr = [math.floor(random.uniform(0, 256)) for x in range(0, 128)]
    data, _ = dctc.DCT2Compress(arr, 256, 128)
    print(len(data)/len(arr))
    print(data)
    print("Seconds: " + str(time.time() - start))