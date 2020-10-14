import read
df_2 = read.load_data()
time = df_2['submission_time']
# print(time)

def extract_hr(time): # extracting the hour 
    from dateutil import parser
    dt = parser.parse(time)
    hour = dt.hour
    return hour

# t_0 = time[0]
# time_1 = extract_hr(t_0)
# print(time_1)

df_2['submission_hours'] = time.apply(extract_hr)
freq_hours = df_2['submission_hours'].value_counts()
print(freq_hours)

