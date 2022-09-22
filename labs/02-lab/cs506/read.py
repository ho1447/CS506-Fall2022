import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path) as input_file:
        read_input = csv.reader(input_file)
        input_matrix = []
        for row in read_input:
            row = [int(item) if item.isnumeric() else item for item in row]
            input_matrix.append(row)


    return input_matrix
