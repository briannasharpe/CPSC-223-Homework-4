import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('breast-cancer-wisconsin.csv')
df = pd.DataFrame(data)

conn = sqlite3.connect('breast_cancer.db', isolation_level=None)
cur = conn.cursor()

# data frame to SQL table
#cur.execute('DROP TABLE breast_cancer')
#data.to_sql('breast_cancer', con=conn, if_exists='replace')
'''
# data frame to JSON
data.to_json('breast_cancer.json', orient='columns')

# calculation of standard deviation and mean of data
print('[standard deviation]')
bc_standard_dev = data.std()
print(bc_standard_dev)
print('[mean]x')
bc_mean = data.mean()
print(bc_mean)

print('clump_thickness')
plt.clf()
data['clump_thickness'].plot.kde()
plt.show()

print('size_uniformity')
plt.clf()
data['size_uniformity'].plot.kde()
plt.show()

print('shape_uniformity')
plt.clf()
data['shape_uniformity'].plot.kde()
plt.show()

print('marginal_adhesion')
plt.clf()
data['marginal_adhesion'].plot.kde()
plt.show()

print('epithelial_size')
plt.clf()
data['epithelial_size'].plot.kde()
plt.show()

print('bland_chromatin')
plt.clf()
data['bland_chromatin'].plot.kde()
plt.show()

print('normal_nucleoli')
plt.clf()
data['normal_nucleoli'].plot.kde()
plt.show()

print('mitoses')
plt.clf()
data['mitoses'].plot.kde()
plt.show()

correlation = data.corr()
print(correlation)

plt.clf()
data.plot(kind='scatter', x='size_uniformity', y='shape_uniformity')
plt.show()
'''
print('----- group -----')

data.groupby('class')
print('[standard deviation]')
print(data.groupby('class').std())
print('[mean]')
print(data.groupby('class').mean())

print('clump_thickness')
plt.clf()
data.groupby('class')['clump_thickness'].plot.kde()
plt.show()

print('size_uniformity')
plt.clf()
data.groupby('class')['size_uniformity'].plot.kde()
plt.show()

print('shape_uniformity')
plt.clf()
data.groupby('class')['shape_uniformity'].plot.kde()
plt.show()

print('marginal_adhesion')
plt.clf()
data.groupby('class')['marginal_adhesion'].plot.kde()
plt.show()

print('epithelial_size')
plt.clf()
data.groupby('class')['epithelial_size'].plot.kde()
plt.show()

print('bland_chromatin')
plt.clf()
data.groupby('class')['bland_chromatin'].plot.kde()
plt.show()

print('normal_nucleoli')
plt.clf()
data.groupby('class')['normal_nucleoli'].plot.kde()
plt.show()

print('mitoses')
plt.clf()
data.groupby('class')['mitoses'].plot.kde()
plt.show()