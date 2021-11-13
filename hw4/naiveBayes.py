from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

X, y = load_iris(return_X_y=True)
range = range(1,6)
for k in range:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=None, shuffle=True)
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    print("{:.0%}".format(metrics.accuracy_score(y_test,y_pred)))

