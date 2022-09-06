import pandas as pd
from students import students_list


data = pd.read_excel('groups.xlsx')



mydata = data[["фио", "группа"]]

print(mydata.values.tolist())




