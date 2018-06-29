from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.datasets import load_digits

#loading the digits dataset
dataset = load_digits()
x = dataset.data
y = dataset.target
#splitting the datset into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#Linear Kernel Model
model = svm.SVC(kernel='linear')
#fitting the model based on training data
model.fit(x_train, y_train)
#predicting the value of y for linear model
y_lpred=model.predict(x_test)
print('Accuracy for Linear Kernel:',metrics.accuracy_score(y_test,y_lpred))

#RBF Kernel Model
model = svm.SVC(kernel='rbf')
#fitting the model based on training data
model.fit(x_train, y_train)
#predicting the value of y for RBF model
y_rpred=model.predict(x_test)
print('Accuracy for RBF Kernel:',metrics.accuracy_score(y_test,y_rpred))

