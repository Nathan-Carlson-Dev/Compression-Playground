import math
import random
import Compression_Algorithms.DCT_Compressions as dctc
import Analysis.SetBuilders as dsb
import Analysis.Tests.AccuracyTest as accuracy

if __name__ == "__main__":
    accuracy.AccuracyTest("UniformAccuracy", lambda: int(random.uniform(0, 9)), lambda x: dctc.DCT2Compress(x, 4), dctc.DCT2Decompress, 256, 10, lambda: 0)
    accuracy.AccuracyTest("NormalAccuracy", lambda: abs(int(random.gauss(9, 3))), lambda x: dctc.DCT2Compress(x, 4), dctc.DCT2Decompress, 256, 10, lambda: 0)