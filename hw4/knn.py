from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
iris = load_iris()
type(iris)

X = iris.data[:, :4]
y = iris.target
X_train,X_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=None, shuffle=True)




range = range(1,6)
scores = {}
scores_list = []
for k in range:
    knn = KNeighborsClassifier(n_neighbors=k, weights='uniform')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores[k] = metrics.accuracy_score(y_test, y_pred)
    #scores_list.append(metrics.accuracy_score(y_test,y_pred))
    print("{:.0%}".format(metrics.accuracy_score(y_test,y_pred)))

