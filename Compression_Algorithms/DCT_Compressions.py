import math
import Compression_Algorithms.Aux_Compressions as aux
import DCT_Algorithms as dct

def DCT2Decompress(arr):
    data = aux.localFrequencyDecompress(arr)
    return dct.IDCT2(data)

def DCT2Compress(arr, threshold):
    data = []
    DCT2Data = dct.DCT2(arr)
    augData = []
    for x in DCT2Data:
        if abs(x) < threshold:
            augData.append(0)
        else:
            augData.append(x)
    data = aux.localFrequencyCompress(augData)
    return data