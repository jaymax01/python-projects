import read
from collections import Counter

data_f = read.load_data()
# print(data_f)
# col = data_f.columns
# print(col)
urls = data_f['url']
urls_1 = urls.astype(str)
# print(urls_1)
# print(urls)
# print(urls_1.dtype)
u_list = []
for u in urls_1:
    u_spt = u.split('.')
    if len(u_spt) > 1:
        u_spt1 = u_spt[-2] + '.' + u_spt[-1]
        u_list.append(u_spt1)
    else:
        continue

# Print top 100 domains
counts = Counter(u_list).most_common(100)
print(counts)

# counts = urls.value_counts().head(100)
# print(counts)


    
    