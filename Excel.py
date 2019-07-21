from matplotlib import pyplot as plt
fig = plt.figure()
import numpy as np
import os


x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Milk',
                 unpack=True,
                 delimiter=",")

plt.plot(x, y, label="Milk")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Vegetables',
                 unpack=True,
                 delimiter=",")
plt.plot(x, y, label="Vegetables")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Stimulants',
                 unpack=True,
                 delimiter=",")
plt.plot(x, y, label="Stimulants")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Alcohol',
                 unpack=True,
                 delimiter=",")
plt.plot(x, y, label="Alcohol")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Fruits',
                 unpack=True,
                 delimiter=",")
plt.plot(x, y, label="Fruits")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Starch',
                 unpack=True,
                 delimiter=",")
plt.plot(x, y, label="Starch-rich foods")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Oils',
                 unpack=True,
                 delimiter=",")
plt.plot(x, y, label="Oils")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
x,y = np.loadtxt('/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Data for Poore/Sweden Sugar',
                 unpack=True,
                 delimiter=",")
plt.plot(x, y, label="Sugars")
plt.ylabel('CO2 emissions/ kg per cap')
plt.xlabel('Year')
plt.legend(loc= "best",fontsize=5)
plt.title("Sweden's CO2 Emissions per capita ", fontsize=10)
save_results_to = '/Users/marielmorquecho/PycharmProjects/giraffe/venv/Raw/Figures Poore/'
plt.savefig(save_results_to + 'SwedenPoore.png')
plt.show()


