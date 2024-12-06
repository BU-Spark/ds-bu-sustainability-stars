import pandas as pd

file_path = 'name.csv'
df_authors = pd.read_csv(file_path)

# Reformat the names from the CSV file to "FirstName LastName"
def reformat_name(name):
    split_name = name.split(',')
    if len(split_name) == 2:
        last_name, first_name = split_name[0].strip(), split_name[1].strip()
        return f"{first_name} {last_name}"
    return name

# Reformat names
df_authors['Formatted Names'] = df_authors.iloc[:, 0].apply(reformat_name)

# List of authors
authors_all = df_authors['Formatted Names'].tolist()

# Function to split the list into 6 equal parts
def split_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

# Split the list into 6 parts
split_lists = split_list(authors_all, 6)
split_lists

# Save each split list as a separate CSV file
for idx, sublist in enumerate(split_lists, start=1):
    df = pd.DataFrame(sublist)
    filename = f"list{idx}.csv"
    df.to_csv(filename, index=False)
