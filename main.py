import pandas

data = pandas.read_csv("onlinefoods.csv")
#print(data["latitude"])

data_latitude = list(data["latitude"])
max_data_latitude = max(data_latitude)
row_max = data[data.latitude == max_data_latitude]
#U liniji 10 stampamo Pin Code(mozda ih ima i vise) sa maksimalnim latitude
#print(row_max["Pin code"])

#Za istu kolonu cemo uzeti avegare
sum = 0
for item in data_latitude:
    sum += item

#Prosjecna vrijednost za kolonu latitude
average_row_latitude = sum / len(data_latitude)
#print(average_row_latitude)

#Razlika izmedju prosjecne vrijednosti i maksimalne

procent_latitude = (max_data_latitude / average_row_latitude) * 100
#print(procent_latitude)

def normalizacija(colum):
    max_val = max(colum)
    min_val = min(colum)
    norm_colum = [(x - min_val) / (max_val - min_val) for x in colum]
    return norm_colum

norm_latitude = normalizacija(data_latitude)

df = pandas.DataFrame(norm_latitude)
df.to_csv("latitude.csv")



#Korelacija
positive_corr = df.corr().unstack().sort_values(ascending=False)

print(positive_corr)
