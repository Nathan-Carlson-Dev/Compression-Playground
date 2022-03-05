def BuildDataSet(title, header, width, height, distribution, updater):
    data = []
    for y in range(0, height):
        row = []
        for x in range(0, width):
            row.append(distribution())
            updater()
        data.append(row)
    file = open("Analysis/Datasets/" + title + "DataSet.csv", "w")
    for x in range(0, width - 1):
        file.write(header + ",")
    file.write(header + "\n")
    for y in range(0, height):
        for x in range(0, width - 1):
            file.write(str(data[y][x]) + ",")
        file.write(str(data[y][width - 1]) + "\n")
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
        file.write(str(data[y][len(data[x]) - 1]) + "\n")
    file.close()
    return "Analysis/Metrics/" + title + "MetricSet.csv"
