import pandas as pd
import re 

# Loading data into pandas dataframe
doc = []
with open('data/blockchain.log') as file:
    lines = file.readlines()
    blkchn_pattern = r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-zA-Z.,-]*[\s-]?(\d{1,2})?[,\s-]'
    time_pattern = r'\d[0-9]:\d[0-9]:\d[0-9].\d[0-9]+\d'
    for line in lines:
        # print("Line>>", line)
        try:
            new_block = re.search('New block', line).group(0)
            # print ("New block List>>", new_block)
            if new_block:
                # print ("New block List>>", new_block)
                total_txn = line[193:194]
                # print("Total TXN>>", total_txn)
                try:
                    blkchn_date = re.match(blkchn_pattern, line).group(0)
                    time_re = re.search(time_pattern, line).group(0)
                    # print (index_value)
                    blkchn_data = blkchn_date + time_re +" "+ total_txn
                    doc.append(blkchn_data)
                except AttributeError:
                    blkchn_date = re.match(blkchn_pattern, line)
                    time_re = re.search(time_pattern, line)
                    # print(">>", blkchn_date)
        except:
            new_block = re.search('New block', line)
            
        
df = pd.Series(doc)
print (df)
res = df.head(10)
print(res)


