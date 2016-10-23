def cnt(y):
    return sum((ord(x[0])-65)*9 + int(x[1]) for x in y.split(","))

def count_reports(full_report, from_date, to_date):
    x = [x.split(" ") for x in sorted(full_report.split("\n"))]
    return sum(cnt(z[1]) for z in (filter(lambda y: y[0] >= from_date and y[0] <= to_date, x)))
