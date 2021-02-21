!#/usr/bin/python3

import pandas
import matplotlib
import matplotlib.pyplot as plt
#definition of func
def removeZeros(string):
       return int(string.replace(" ", "")) 

table = pandas.read_html(
       "https://worldtable.info/gosudarstvo/tablica-rozhdaemosti-po-godam-rossija.html",
       header = 0,
       converters = {
              0: removeZeros,
              1: removeZeros
       }
       )[0]
#show table
print(table)
#print plot
table.plot(x = 'Год', kind='line')
plt.show()