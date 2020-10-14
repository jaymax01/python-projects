def load_data(): # method for loading the dataset
    import pandas as pd
    col_Names=["submission_time", "upvotes", "url", "headline"]
    data = pd.read_csv("hn_stories.csv",names=col_Names)
    return data
#first_ten = data.head()
#print(load_data())
