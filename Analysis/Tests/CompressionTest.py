import statistics
import Analysis.SetBuilders as setBuilder
import Analysis.Updater as upd

def CompressionTest(title, generator, update, reset, info):

    updater = upd.Updater(generator, update, reset, info)
    (rawData, _) = setBuilder.BuildDataSet(title, updater)
    metrics = []

    for data in rawData:
        size = len(data)

        compressedData = info["action"][0](data)
        compressedSize = len(compressedData)

        processedData = info["action"][1](compressedData)
        err = [abs(data[i] - processedData[i]) for i in range(0, size)]
        avg = statistics.mean(err)
        stdev = statistics.stdev(err)

        metric = [size, compressedSize, avg, stdev]

        if("additional_headers" in info and "additional_info" in info):
            metric = info["additional_info"] + metric

        metrics.append(metric)

    headers = ["Orig Size", "Compressed Size", "Err Avg", "Err Std Dev"]

    if("additional_headers" in info and "additional_info" in info):
        headers = info["additional_headers"] + headers

    setBuilder.BuildMetricSet(title, headers, metrics)

    return (metrics, rawData)