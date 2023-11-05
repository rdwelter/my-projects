# From https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ 
# first intro to pandas and sklearn, still don't really know how each function works
# but interesting to see a model of ml and start learning packages

import pandas as p
import matplotlib.pyplot as plt
import sklearn.model_selection as smo
import sklearn.metrics as sme
import sklearn.svm as ssv

def run():
    url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = p.read_csv(url, names=names)
    # print('dataset loaded')
    # dataset.hist()
    # plt.show()
    array = dataset.values
    # print(array)
    X = array[:, 0:4]
    y = array[:, 4]
    X_train, X_validation, Y_train, Y_validation = smo.train_test_split(X, y, test_size=0.2, random_state=1)
    model = ssv.SVC(gamma='auto')
    model.fit(X_train, Y_train)
    predictions = model.predict(X_validation)
    
    print(sme.accuracy_score(Y_validation, predictions))
    print(sme.confusion_matrix(Y_validation, predictions))
    print(sme.classification_report(Y_validation, predictions))
    
    # help(model.predict)

if __name__ == "__main__":
    run()