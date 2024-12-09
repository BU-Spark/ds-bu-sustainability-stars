Here is a brief instruction on the use of python scripts in this OpenBU folder:

1.List.py(optional):
This script can be used to break the whole name list to certain number of sub-lists.
replace file_path = 'name.csv', name.csv, with actual faculty list, or you can use the same name.csv in folder "list".
replace split_lists = split_list(authors_all, 6), 6, with the actual number of sub-lists you want.

2.WebScraping.py
This script can be used to scrape papers from OpenBu website.
repalce df = pd.read_csv("name.csv"), name.csv, with lists you broke in last script, or remain it unchanged
The final output will be saved in same folder named author_search_results, following with the number of list.

3.Combine.py(optional)
This script can be used to combine the results to a final results.
put all author_search_results in a folder named Results.
The final output will be saved in combined_output.csv'.
