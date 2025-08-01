import csv

def merge_csv(csv_list, output_path):
    fieldnames = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    with open(output_path, 'w', encoding=' utf-8', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

# Please, uncomment the line below to execute the code with the example given
# merge_csv(['./csv/class1.csv','./csv/class2.csv'],'./csv/all_students.csv')
