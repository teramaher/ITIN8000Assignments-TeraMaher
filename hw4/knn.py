import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# import some data to play with
iris = datasets.load_iris()

measure = iris.data[:, :4]
targetlab = iris.target
count = 0
target_names = iris.target_names
for mes in measure:
    print(mes, target_names[targetlab[count]])
    count = count + 1