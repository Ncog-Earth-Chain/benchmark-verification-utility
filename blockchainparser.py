import pandas as pd
import re 

# Loading data into pandas dataframe
# doc = []
# with open('data/blockchain.log') as file:
#     lines = file.readlines()
#     date_pattern = r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-zA-Z.,-]*[\s-]?(\d{1,2})?[,\s-]'
#     time_pattern = r'\d[0-9]:\d[0-9]:\d[0-9].\d[0-9]+\d'
#     for line in lines:
#         # print("Line>>", line)
#         try:
#             # Block
#             new_block = re.search('New block', line).group(0)
#             # print ("New block List>>", new_block)
#             if new_block:
#                 # print ("New block List>>", new_block)
#                 #Total TXN
#                 total_txn = line[193:194]
#                 # print("Total TXN>>", total_txn)
#                 try:
#                     blkchn_date = re.match(date_pattern, line).group(0)
#                     time_re = re.search(time_pattern, line).group(0)
#                     # print (index_value)
#                     blkchn_data = blkchn_date + time_re +" "+ total_txn
#                     doc.append(blkchn_data)
#                 except AttributeError:
#                     blkchn_date = re.match(date_pattern, line)
#                     time_re = re.search(time_pattern, line)
#                     # print(">>", blkchn_date)
#         except:
#             new_block = re.search('New block', line)
# df = pd.Series(doc)
# print (df)
# res = df.head(10)
# print(res)

#Return the total from the list
def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total


#Return a file
def open_file(filename):
    """docstring"""
    with open(filename, 'r') as file:
        data = file.readlines()
        return data
# print("Data>",open_file('data/jes.log'))

#function to get the blocks per Month and Date.
def get_blks_bydate(start_date, end_date):
    blk_date_dict = []
    total_txs_dict = []
    lines = open_file('data/blockchain.log')
    blkchn_pattern = r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-zA-Z.,-]*[\s-]?(\d{1,2}) '
    time_pattern = r'\d[0-9]:\d[0-9]:\d[0-9].\d[0-9]+\d'
    txs_pattern = r'\btxs\b=\d'
    # print("Start>", start_date, "end", end_date)
    for line in lines:
        new_block = re.search('New block', line)
        if new_block:
            blk_date_data = re.match(blkchn_pattern, line).group(0)
            time_data = re.search(time_pattern, line).group(0)
            txs_data = re.search(txs_pattern, line).group(0)
            blk_data = "2023 " + blk_date_data + time_data + " " + txs_data
            # blk_date_dict.append(blk_data)
            time_date = "2023 " + blk_date_data + time_data
            t_txs = int(txs_data[4])
            if start_date <= time_date <= end_date:
                # print("Base on time>>", line)
                blk_date_dict.append(blk_data)
                total_txs_dict.append(t_txs)
        pass    
    # print("Start>",s_date, "End>", e_date)
    # print (blk_date_dict)
    res_per_sec = len(blk_date_dict)
    print("Result of New Block by date range    >", res_per_sec)
    txs_total = sum_of_list(total_txs_dict)
    print("Total txs", txs_total)
    avg_txs = txs_total/len(total_txs_dict)
    print("Average per second", avg_txs)
 
    df = pd.Series(blk_date_dict)
    return df

# Based on this format " '2023 Feb 01 10:25:38.970', '2023 Feb 01 11:06:42.932' " we can get the info.
# print ("Result >>", get_blks_bydate('2023 Feb 01 10:25:38.970', '2023 Feb 01 11:06:42.932'))
if __name__ == "__main__":
    get_blks_bydate('2023 Feb 01 10:25:38.970', '2023 Feb 01 11:06:42.932')

