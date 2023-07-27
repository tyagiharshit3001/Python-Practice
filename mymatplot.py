import matplotlib.pyplot as mpt
import pandas as pd
import xlrd
import numpy as np

"""
mpt.xlabel("Wind_Speed")
mpt.ylabel("Temperature")
mpt.title("Weather Data of Hapur City")
mpt.plot([1, 5, 7, 9], [20, 30, 60, 50], "D--", label="G1")
mpt.plot([2, 3, 6, 8], [13, 22, 43, 54], label="G2")
mpt.plot([1.5, 5.2, 7.6, 9.8], [21, 13, 19, 63], label="G3")
mpt.plot([0.5, 4, 5.9, 9.4], [31, 35, 68, 54], label="G4")
mpt.legend(loc="best", shadow=True, fontsize='small')
mpt.grid()
mpt.show()
"""

xpos = np.arange(len([1.5, 5.2, 7.6, 9.8]))
mpt.xticks(xpos, ['Mon', 'Tue', 'Wed', 'Thur'])
mpt.bar(xpos - 0.2, [21, 13, 54, 63], color="green", width=0.4, label="Delhi")
mpt.bar(xpos + 0.2, [13, 9, 43, 54], color="blue", width=0.4, label="Kolkata")
mpt.xlabel('Days')
mpt.ylabel('Temperature (in °C)')
mpt.title("Weather Data of Delhi & Kolkata")
mpt.legend(loc="upper left", shadow=True, fontsize='small')
mpt.show()

ypos = np.arange(len([1.5, 5.2, 7.6, 9.8]))
mpt.yticks(ypos, ['Mon', 'Tue', 'Wed', 'Thur'])
mpt.barh(ypos - 0.2, [21, 13, 54, 63], color="green", height=0.4, label="Delhi")
mpt.barh(ypos + 0.2, [13, 9, 43, 54], color="blue", height=0.4, label="Kolkata")
mpt.ylabel('Days')
mpt.xlabel('Temperature (in °C)')
mpt.title("Weather Data of Delhi & Kolkata")
mpt.legend(loc="lower right", shadow=True, fontsize='small')
mpt.show()
bld_sugar = np.array([113, 150, 89, 78, 98, 85, 89, 72, 90, 100, 123, 205, 450])
mpt.hist(bld_sugar)
mpt.show()

"""
df = pd.read_excel('sample-xls-file-for-testing.xls', 'Sheet1')
mpt.title("Units_Sold ")
new_gdf = df.groupby("Country")
new_df = new_gdf.mean()
print(new_df)
mpt.pie(new_df['Units_Sold'], labels=["Canada", "France", "Germany", "Mexico", 'USA'], radius=0.75, autopct='%0.1f%%',
        startangle=20, )
mpt.legend(loc="upper left", fontsize='small')
mpt.show()
"""
