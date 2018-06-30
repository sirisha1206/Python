from sklearn import datasets,metrics
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#loading the digits dataset
dataset = datasets.load_digits()
X = dataset.data
Y = dataset.target
#split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)


#knn neighbors classifier
knn = KNeighborsClassifier(n_neighbors=1)
#fit the model on training data
knn.fit(x_train, y_train)
#predicting the value of y
y_pred = knn.predict(x_test)
print("KNN Accuracy for k=1 :", metrics.accuracy_score(y_test, y_pred))

knn = KNeighborsClassifier(n_neighbors=60)
#fit the model on training data
knn.fit(x_train, y_train)
#predicting the value of y
y_pred = knn.predict(x_test)
#getting the accuracy score
print("KNN Accuracy for k=60 :", metrics.accuracy_score(y_test, y_pred))

#selecting the k value in the range of 1 - 60
knn_range = range(1, 60)
accuracy = []
#for different k values get the accuracy
for r in knn_range:
    knn = KNeighborsClassifier(n_neighbors=r)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    accuracy.append(metrics.accuracy_score(y_test, y_pred))
#plotting the graph for k values and accuracy values
plt.plot(knn_range, accuracy)
plt.title("KNN Model")
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.show()