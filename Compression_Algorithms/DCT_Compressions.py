import math
import Compression_Algorithms.Aux_Compressions as aux
import DCT_Algorithms as dct

def DCT2Decompress(arr):
    return dct.IDCT2(aux.localFrequencyDecompress(arr))

def DCT2Compress(arr, threshold, fix):
    DCT2Data = dct.DCT2(arr)
    augData = []
    for x in DCT2Data:
        if abs(x) < threshold:
            augData.append(0)
        else:
            augData.append(x - (x % fix))
    return aux.LZWEncode(augData, (min(augData), max(augData)))