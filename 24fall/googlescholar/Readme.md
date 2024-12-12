## file:
all_author_papers_2022_2024_gs.csv: raw data from google scholar
data.ipynb: code used to gererate the data, chunk_start = 1 to start with first author, else start with (chunk_start-1)*30 th author(order is the name in name.csv)
name.csv: name list of BU faculties until 2023

## how to use:
make sure name.csv and data.ipynb is in same folder. Run two cell in data.ipynb, for second cell, change chunk_start to adjust the starting position of author, all paper from 30 authors will be in a same csv file. After getting all the papers, run third cell to combine everything.
