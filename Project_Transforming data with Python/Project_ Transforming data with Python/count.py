import read
from collections import Counter

df = read.load_data() # importing the data
headlines = df['headline']
# print(headlines.head())

string = headlines.str.cat(sep='').lower() # series into a single string
# print(string)
spt_string = string.split() # split single string 
# print(spt_string)

c = Counter(spt_string).most_common(100)
print(c)

#  word count dictionary
# word_count = { }
# for word in spt_string:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
        
# # print top 100 words
# s = sorted(word_count, key=word_count.get, reverse=True)
# print(s[0:100])




