import pandas as pd
from csv import writer
from csv import reader


def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

df = pd.read_csv(r'F:\rpl_hist\rpl_2010_to_2019.csv', sep=';')

nOt = len(df.Хозяева.unique())  # number of teams
sorted_list = sorted(df.Хозяева.unique())
team_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
team_id_dict = dict(zip(sorted_list, team_id_list))
header1 = 'Хозяева_ID'
header2 = 'Гости_ID'
add_column_in_csv('rpl_2010_to_2019_2.csv', 'rpl_2010_to_2019_3.csv',
                  lambda row, line_num: row.insert(1, team_id_dict.get(row[0]))


#nOt = len(df.Хозяева.unique())  # number of teams
#sorted_list = sorted(df.Хозяева.unique())
#team_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                #29, 30, 31]
#id_team_dict = dict(zip(team_id_list, sorted_list))

