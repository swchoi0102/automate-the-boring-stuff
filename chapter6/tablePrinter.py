def printTable(tableData):

    num_cols = len(tableData[0])
    col_widths = [max([len(item) for item in data]) for data in tableData]

    for row in range(num_cols):
        line = ""
        for col, data in enumerate(tableData):
            line += data[row].rjust(col_widths[col]) + " "
        print(line)


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)


if __name__ == "__main__":
    main()
