def BuildDataSet(title, updater):
    data = []
    for y in range(0, updater.info["height"]):
        line = []
        for x in range(0, updater.info["width"]):
            line.append(updater.generate())
        data.append(line)
        updater.update()
    updater.reset()
    file = open("Analysis/Datasets/" + title + "DataSet.csv", "w")
    for y in range(0, updater.info["height"]):
        for x in range(0, updater.info["width"] - 1):
            file.write(str(data[y][x]) + ",")
        file.write(str(data[y][updater.info["width"] - 1]) + "\n")
        updater.update()
    file.close()
    return (data, "Analysis/Datasets/" + title + "DataSet.csv")

def BuildMetricSet(title, headers, data):
    file = open("Analysis/Metrics/" + title + "MetricSet.csv", "w")
    file.write("cases, ")
    for x in range(0, len(headers) - 1):
        file.write(headers[x] + ",")
    file.write(headers[len(headers) - 1] + "\n")
    for y in range(0, len(data)):
        file.write(str(y + 1) + ", ")
        for x in range(0, len(data[y]) - 1):
            file.write(str(data[y][x]) + ",")
        file.write(str(data[y][len(data[y]) - 1]) + "\n")
    file.close()
    return "Analysis/Metrics/" + title + "MetricSet.csv"
