def count_ingots(report):
    return sum((ord(x[0])-65)*9 + int(x[1]) for x in report.split(","))
