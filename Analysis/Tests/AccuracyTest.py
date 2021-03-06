import statistics
import Analysis.SetBuilders as setBuilder
import Analysis.Updater as upd

def AccuracyTest(title, generator, update, reset, info):
    
    updater = upd.Updater(generator, update, reset, info)
    (rawData, _) = setBuilder.BuildDataSet(title, updater)
    metrics = []

    for data in rawData:

        size = len(data)
        avg = statistics.mean(data)
        stdev = statistics.stdev(data)
        avgFreq = size/len(set(data))

        processedData = info["action"](data)
        err = [abs(data[x] - processedData[x]) for x in range(0, size)]

        errAvg = statistics.mean(err)
        errStdev = statistics.stdev(err)
        errAvgFreq = size/len(set(err))

        metric = [size, avg, stdev, avgFreq, errAvg, errStdev, errAvgFreq]

        if("additional_headers" in info and "additional_info" in info):
            metric = info["additional_info"] + metric

        metrics.append(metric)

    headers = ["size", "Avg", "Std Dev", "Avg Freq", "Err Avg", "Err Std Dev", "Err Avg Freq"]

    if("additional_headers" in info and "additional_info" in info):
        headers = info["additional_headers"] + headers

    setBuilder.BuildMetricSet(title, headers, metrics)

    return (metrics, rawData)