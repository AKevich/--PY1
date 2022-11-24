OUTPUT_FILE = "input.csv"


def to_csv_file(filename, headers, rows, delimiter=',', new_line='\n'):
    f = open(filename, 'w')
    for i in range(len(headers) - 1):
        f.write(f'{headers[i]}{delimiter}')
    f.write(f'{headers[-1]}{new_line}')
    for i in rows:
        for j in range(len(i) - 1):
            f.write(f'{i[j]}{delimiter}')
        f.write(f'{i[-1]}{new_line}')
    f.close()


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(OUTPUT_FILE, headers_list, data)




import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as f:
        q = [i.split(',') for i in f]
        head = q[0]
        dat = q[1:]
        head[-1] = head[-1][:-1]
        for i in dat:
            i[-1] = i[-1][:-1]
    slovar = [{head[i]: dat[j][i] for i in range(len(head))} for j in range(len(dat))]
    return slovar


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
