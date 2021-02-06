import pandas
import matplotlib
import matplotlib.pyplot as plt

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

print(table)

table.plot(x = 'Год')
plt.show()