from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
iris = load_iris()
scaler = StandardScaler()


for x in range(0, 5):
    train_data, test_data, train_labels, test_labels = train_test_split(iris.data,iris.target,test_size=0.2,random_state=None, shuffle=True)
    # we fit the train data
    scaler.fit(train_data)
    # scaling the train data
    train_data = scaler.transform(train_data)
    test_data = scaler.transform(test_data)
    mlp = MLPClassifier(hidden_layer_sizes=(10, 6), max_iter=1000)
    # let's fit the training data to our model
    mlp.fit(train_data, train_labels)
    predictions_train = mlp.predict(train_data)
    predictions_test = mlp.predict(test_data)
    print("{:.0%}".format(accuracy_score(predictions_test, test_labels)))
