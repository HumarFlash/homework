def sort_file(file):
    with open(file, "r+") as InputF, open("ans.txt", "w") as OutF:
        lines = []
        for line in InputF:
            line = list(line.split())
            data = line[0]
            temp = line[1]
            lines.append([data, int(temp)])
        lines = sorted(lines, key=lambda data: data[1])
        for line in lines:
            line[1] = str(line[1])
        for line in lines:
            OutF.write(f"{' '.join(line)}\n")


if __name__ == "__main__":
    file = input()
    sort_file(file)
