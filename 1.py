from sort_file import sort_file


def output(mid_temp, month, month_deviation):
    print(mid_temp)
    for elem in range(len(month_deviation)):
        month_deviation[elem] = (month_deviation[elem], month[int(month_deviation[elem][0]) - 1])
    for elem in month_deviation:
        print(f'Month = {elem[0][0]}, Average temperature = {elem[1]}, Deviation = {elem[0][1]}')


def deviation(month, mid_temp):
    month_deviation = {}
    for elem in range(len(month)):
        month_deviation[f'{elem + 1}'] = (round(abs(abs(month[elem]) - abs(mid_temp)), 1))
    return month_deviation


def mid_month(lines):
    mid_temp_month = []
    data = 0
    for month in range(1, 13):
        data_month = 0
        current_data = lines[data][0][-2:]
        if current_data[0] == '0':
            current_data = current_data[1]
        sum_temp_month = 0
        while int(current_data) == month and len(lines) > data:
            current_data = lines[data][0][-2:]
            if current_data[0] == '0':
                current_data = current_data[1]
            sum_temp_month += int(lines[data][1])
            data += 1
            data_month += 1
        data_month -= 1
        mid_temp_month.append(round(sum_temp_month / data_month, 1))
    return mid_temp_month


def main():
    sort_file("1.txt")
    with open("ans.txt", "r") as InputF:
        lines = []
        for line in InputF:
            line = list(line.split())
            lines.append(line)
        sum_values = 0
        for elem in lines:
            sum_values += int(elem[1])
        mid_temp = round(sum_values / len(lines), 1)
        lines = sorted(lines, key=lambda data: int(data[0][-2:]))
        month = mid_month(lines)
        month_deviation = list(deviation(month, mid_temp).items())
        month_deviation.sort(key=lambda x: x[1])
        output(mid_temp, month, month_deviation)


main()
