'''
Function to merge two or more csv files in one.
>>>merge_CSV_files([file1.csv, file2.csv], all_files.csv)

Output file should have all the columns of both csv without losing data
'''
import csv

def merge_csv_files(*csv_files, output_path):

    merged_data = []
    all_fields = {}
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            all_fields = reader.fieldnames
            for row in data:
                merged_data.append(row)

    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_fields)
        writer.writeheader()
        for row in merged_data:
            writer.writerow(row)


merge_csv_files('./csv/class1.csv','./csv/class2.csv',output_path='./csv/all_students.csv')