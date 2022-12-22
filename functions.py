import fileinput


def load_file():
    with open('all_stocks_5yr.csv', 'r') as i:
        file = [i.rstrip('\n').split(',') for i in i]

    res = []
    for i in range(1, len(file)):
        try:
            res.append([
                str(file[i][0]),
                float(file[i][1]),
                float(file[i][2]),
                float(file[i][3]),
                float(file[i][4]),
                int(file[i][5]),
                str(file[i][6])
            ])
        except ValueError:
            return res


def filter_func(value: str, data):
    res = []
    value = ''.join(value)

    column = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    if value in column:
        value = column.index(value)
    data.sort(key=lambda row: row[value])

    for i in data:
        res.append(i)
    return res


def limit_func(num, data):
    return data[:num]


def sort_func(method, data):
    res = []
    if method is False:
        return data
    else:
        data.sort(key=lambda x: x[6])
        for i in data:
            res.append(i)
        return res


def sort_revers(method, data):
    if method == 'asc':
        return sorted(data, reverse=True)
    elif method == 'desc':
        return sorted(data, reverse=False)


def get_date(name, date):
    res = []
    for line in fileinput.input(['all_stocks_5yr.csv']):
        if name in line and date in line:
            res.append(line)

    return res


def write_file(value, res):
    with open(value, "w") as f:
        for item in res:
            res = str(item).split(',')
            f.write(f"{res[0]} | {res[1]} | {res[2]} | {res[3]} | {res[4]} | {res[5]} | {res[6]}\n")



