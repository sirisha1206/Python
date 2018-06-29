from sklearn import datasets,metrics
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#loading the iris dataset
iris = datasets.load_iris()
X= iris.data
Y= iris.target
target_names = iris.target_names
#splitting the data into training and testing data
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2)

#Linear Discriminant analysis
lda = LinearDiscriminantAnalysis()
#fitting the model for LDA
x_fit = lda.fit(x_train,y_train).transform(X)
#predicting the value of y for LDA
y_ldapred=lda.predict(x_test)
#printing the accuracy score for lda
print('Accuracy for Linear Discriminant Analysis:',metrics.accuracy_score(y_ldapred,y_test))
#plotting the graph for LDA
plt.figure()
colours = ['navy', 'pink', 'turquoise']
for colour, k, target_name in zip(colours, [0, 1, 2], target_names):
    plt.scatter(x_fit[Y == k, 0], x_fit[Y == k, 1], alpha=.8, color=colour,label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('Linear Discriminant Analysis for  IRIS dataset')
plt.show()

#Logistic Regression
logreg = LogisticRegression()
#fitting the model for training dataset in logistic regression
lr = logreg.fit(x_train,y_train)
#predicting the value of y for logistic regression
y_logpred=logreg.predict(x_test)
#printing the accuracy score for logistic regression
print('Accuracy for Logistic Regression:',metrics.accuracy_score(y_logpred,y_test))

