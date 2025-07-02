'''
Function to merge two or more csv files in one.
>>>merge_CSV_files([file1.csv, file2.csv], all_files.csv)

Output file should have all the columns of both csv without losing data
'''
import csv

def merge_csv_files(*csv_files, output_path):

    output = []
    fields = []
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            data = list(csv.DictReader(f))
            for key in data[0].keys():
                fields.append(key)
            for row in data:
                output.append(row)
    fieldNames = []
    for field in fields:
        if field not in fieldNames:
            fieldNames.append(field)

    with open(output_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        for row in output:
            writer.writer(row)

    print(output)


merge_csv_files('./csv/class1.csv','./csv/class2.csv',output_path='./csv/all_students.csv')