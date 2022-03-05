from asyncio.windows_events import NULL
import Analysis.SetBuilders as setBuilder
import math
import statistics

def AccuracyTest(title, distribution, compressionFunction, decompressionFunction, width, height, Updater):
    (rawData, _) = setBuilder.BuildDataSet(title, "Accuracy Test", width, height, distribution, Updater)
    metrics = []
    for data in rawData:
        size = len(data)
        avg = statistics.mean(data)
        stdev = statistics.stdev(data)
        avgFreq = size/len(set(data))
        processedData = decompressionFunction(compressionFunction(data))
        err = [data[i] - processedData[i] for i in range(0, size)]
        avgErr = statistics.mean(err)
        stdevErr = statistics.stdev(err)
        avgFreqErr = size/len(set(data))
        metric = [size, avg, stdev, avgFreq, avgErr, stdevErr, avgFreqErr]
        metrics.append(metric)
    headers =["Size", "Avg", "Std Dev", "Avg Freq", "Avg Err", "Std Dev Err", "Avg Freq Err"]
    setBuilder.BuildMetricSet(title, headers, metrics)
    return metrics