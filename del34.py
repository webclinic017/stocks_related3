from sklearn.datasets import fetch_openml
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import yfinance as yf
import datetime
import pandas as pd
import numpy as np
from finta import TA
import matplotlib.pyplot as plt
import sklearn
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

"""
Defining some constants for data mining
"""

NUM_DAYS = 2500     # The number of days of historical data to retrieve
INTERVAL = '1d'     # Sample rate of historical data
symbol = 'tsla'      # Symbol of the desired stock

# List of symbols for technical indicators
INDICATORS = ['RSI', 'MACD', 'STOCH','ADL', 'ATR', 'MOM', 'MFI', 'ROC', 'OBV', 'CCI', 'EMV', 'VORTEX']


"""
Next we pull the historical data using yfinance
Rename the column names because finta uses the lowercase names
"""

start = (datetime.date.today() - datetime.timedelta( NUM_DAYS ) )
end = datetime.datetime.today()

df = yf.download(symbol, start=start, end=end, interval=INTERVAL)
df.rename(columns={"Close": 'close', "High": 'high', "Low": 'low', 'Volume': 'volume', 'Open': 'open'}, inplace=True)
print(df.head(),' ================ df.head ==========================')
print(df.shape,' ================== df.shape ========================')


plt.figure(figsize=(16,8))
plt.title('nnn')
plt.xlabel('Days')
plt.ylabel('Close price')
plt.plot(df['close'])
plt.show()



df['result']=''
X=df['close']
y=df['result']
future_days=25
print(df,' Prediction without shifted future')
df['Prediction']=df[['close']].shift(-future_days)

df=df[['close','Prediction']]
print(df.tail(4))
print(df,' ==============   Prediction wuth shifted future  ===================')

##########################################################
##X=np.array(df.drop(['Prediction'],1))[:-future_days]
##print(X,' X')
##y=np.array(df['Prediction'])[:-future_days]
##print(y,' y')
###split data


##
X=np.array(df.drop(['Prediction'],1))[:-future_days]
print(X,' =================  X ===================== len(X)= ',len(X),'  ')
y=np.array(df['Prediction'])[:-future_days]
print(y,' ================  y  ============ len(y)= ',len(y),'  ')

##print('\n\n\n')
##print(X[-2:],' ========== 6666   ')
##print('\n\n\n')
##print(y[-2:],' ========== 6666   ')
##print('\n\n\n')



import sys
##sys.exit()
###########################################################
##print(df.shape[0])
##X=np.array(df.iloc[:-25])
##y=np.array(df.iloc[-25:])

###split data


############################################################
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.25)
import sys

# create models
tree=DecisionTreeRegressor().fit(x_train,y_train)
lr=LinearRegression().fit(x_train,y_train)

x_future=df.drop(['Prediction'],1)[:-future_days]
x_future=x_future.tail(future_days)
x_future=np.array(x_future)
print('\n\n\n')
print(x_future,'   ================== x_future ====================')
print('\n\n\n')

#show model tree prediction
tree_prediction=tree.predict(x_future)
print(tree_prediction,' ============= tree prediction ==============')
print()
lr_prediction=lr.predict(x_future)
print(lr_prediction)
##
#visualize the data

predictions=tree_prediction
valid=df[X.shape[0]:]
valid['Predictions']=predictions
print(valid,' ===== valid')
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days')
plt.ylabel('Close Price USD($)')
plt.plot(valid[['close','Predictions']])
plt.legend(['orin', 'val', 'Predict'])
plt.show()
##


##
##tmp = data.iloc[-60:]
##tmp['close'].plot()
##
##
##"""
##Next we clean our data and perform feature engineering to create new technical indicator features that our
##model can learn from
##"""
##
##def _exponential_smooth(data, alpha):
##    """
##    Function that exponentially smooths dataset so values are less 'rigid'
##    :param alpha: weight factor to weight recent values more
##    """
##    
##    return data.ewm(alpha=alpha).mean()
##
##data = _exponential_smooth(data, 0.65)
##
##tmp1 = data.iloc[-60:]
##tmp1['close'].plot()
##
##def _get_indicator_data(data):
##    """
##    Function that uses the finta API to calculate technical indicators used as the features
##    :return:
##    """
##
##    for indicator in INDICATORS:
##        ind_data = eval('TA.' + indicator + '(data)')
##        if not isinstance(ind_data, pd.DataFrame):
##            ind_data = ind_data.to_frame()
##        data = data.merge(ind_data, left_index=True, right_index=True)
##    data.rename(columns={"14 period EMV.": '14 period EMV'}, inplace=True)
##
##    # Also calculate moving averages for features
##    data['ema50'] = data['close'] / data['close'].ewm(50).mean()
##    data['ema21'] = data['close'] / data['close'].ewm(21).mean()
##    data['ema15'] = data['close'] / data['close'].ewm(14).mean()
##    data['ema5'] = data['close'] / data['close'].ewm(5).mean()
##
##    # Instead of using the actual volume value (which changes over time), we normalize it with a moving volume average
##    data['normVol'] = data['volume'] / data['volume'].ewm(5).mean()
##
##    # Remove columns that won't be used as features
##    del (data['open'])
##    del (data['high'])
##    del (data['low'])
##    del (data['volume'])
##    del (data['Adj Close'])
##    
##    return data
##
##data = _get_indicator_data(data)
##print(data.columns)
##
##def _produce_prediction(data, window):
##    """
##    Function that produces the 'truth' values
##    At a given row, it looks 'window' rows ahead to see if the price increased (1) or decreased (0)
##    :param window: number of days, or rows to look ahead to see what the price did
##    """
##    
##    prediction = (data.shift(-window)['close'] >= data['close'])
##    prediction = prediction.iloc[:-window]
##    data['pred'] = prediction.astype(int)
##    
##    return data
##
##data = _produce_prediction(data, window=15)
##del (data['close'])
##data = data.dropna() # Some indicators produce NaN values for the first few rows, we just remove them here
##print(data.tail())
##print('\n\n\n')
##print('*******************************************************')
##print('\n\n\n')
##
##
##def _train_random_forest(X_train, y_train, X_test, y_test):
##
##    """
##    Function that uses random forest classifier to train the model
##    :return:
##    """
##    
##    # Create a new random forest classifier
##    rf = RandomForestClassifier()
##    
##    # Dictionary of all values we want to test for n_estimators
##    params_rf = {'n_estimators': [110,130,140,150,160,180,200]}
##    
##    # Use gridsearch to test all values for n_estimators
##    rf_gs = GridSearchCV(rf, params_rf, cv=5)
##    
##    # Fit model to training data
##    rf_gs.fit(X_train, y_train)
##    
##    # Save best model
##    rf_best = rf_gs.best_estimator_
##    
##    # Check best n_estimators value
##    print(rf_gs.best_params_)
##    
##    prediction = rf_best.predict(X_test)
##
##    print(classification_report(y_test, prediction))
##    print(confusion_matrix(y_test, prediction))
##
##    print(df.columns)
##    
##    
##    return rf_best
##
##X=df[['close', '14 period RSI', 'MACD', 'SIGNAL', '14 period STOCH %K', 'MFV',
##       '14 period ATR', 'MOM', '14 period MFI', 'ROC', 'OBV', '20 period CCI',
##       '14 period EMV', 'VIm', 'VIp', 'ema50', 'ema21', 'ema15', 'ema5',
##       'normVol']]
##
##y=df[['result']]
##X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
##
##rf_model = _train_random_forest(X_train, y_train, X_test, y_test)
##print(rf_model,'     rf_model')
##
##def _train_KNN(X_train, y_train, X_test, y_test):
##
##    knn = KNeighborsClassifier()
##    # Create a dictionary of all values we want to test for n_neighbors
##    params_knn = {'n_neighbors': np.arange(1, 25)}
##    
##    # Use gridsearch to test all values for n_neighbors
##    knn_gs = GridSearchCV(knn, params_knn, cv=5)
##    
##    # Fit model to training data
##    knn_gs.fit(X_train, y_train)
##    
##    # Save best model
##    knn_best = knn_gs.best_estimator_
##     
##    # Check best n_neigbors value
##    print(knn_gs.best_params_)
##    
##    prediction = knn_best.predict(X_test)
##
##    print(classification_report(y_test, prediction))
##    print(confusion_matrix(y_test, prediction))
##    
##    return knn_best
##    
##    
##knn_model = _train_KNN(X_train, y_train, X_test, y_test)
##
##
##def _ensemble_model(rf_model, knn_model, gbt_model, X_train, y_train, X_test, y_test):
##    
##    # Create a dictionary of our models
##    estimators=[('knn', knn_model), ('rf', rf_model), ('gbt', gbt_model)]
##    
##    # Create our voting classifier, inputting our models
##    ensemble = VotingClassifier(estimators, voting='hard')
##    
##    #fit model to training data
##    ensemble.fit(X_train, y_train)
##    
##    #test our model on the test data
##    print(ensemble.score(X_test, y_test))
##    
##    prediction = ensemble.predict(X_test)
##
##    print(classification_report(y_test, prediction))
##    print(confusion_matrix(y_test, prediction))
##    
##    return ensemble
##    
##ensemble_model = _ensemble_model(rf_model, knn_model, gbt_model, X_train, y_train, X_test, y_test)
##
##def cross_Validation(data):
##
##    # Split data into equal partitions of size len_train
##    
##    num_train = 10 # Increment of how many starting points (len(data) / num_train  =  number of train-test sets)
##    len_train = 40 # Length of each train-test set
##    
##    # Lists to store the results from each model
##    rf_RESULTS = []
##    knn_RESULTS = []
##    ensemble_RESULTS = []
##    
##    i = 0
##    while True:
##        
##        # Partition the data into chunks of size len_train every num_train days
##        df = data.iloc[i * num_train : (i * num_train) + len_train]
##        i += 1
##        print(i * num_train, (i * num_train) + len_train)
##        
##        if len(df) < 40:
##            break
##
##        y = df['pred']
##        features = [x for x in df.columns if x not in df['pred']]
##        X = df[features]
##
##        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 7 * len(X) // 10,shuffle=False)
##
##
##def cross_Validation(data):
##
##    # Split data into equal partitions of size len_train
##    
##    num_train = 10 # Increment of how many starting points (len(data) / num_train  =  number of train-test sets)
##    len_train = 40 # Length of each train-test set
##    
##    # Lists to store the results from each model
##    rf_RESULTS = []
##    knn_RESULTS = []
##    ensemble_RESULTS = []
##    
##    i = 0
##    while True:
##        
##        # Partition the data into chunks of size len_train every num_train days
##        df = data.iloc[i * num_train : (i * num_train) + len_train]
##        i += 1
##        print(i * num_train, (i * num_train) + len_train)
##        
##        if len(df) < 40:
##            break
##        
##        y = df['pred']
##        features = [x for x in df.columns if x not in ['pred']]
##        X = df[features]
##
##        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 7 * len(X) // 10,shuffle=False)
##        
##        rf_model = _train_random_forest(X_train, y_train, X_test, y_test)
##        knn_model = _train_KNN(X_train, y_train, X_test, y_test)
##        ensemble_model = _ensemble_model(rf_model, knn_model, X_train, y_train, X_test, y_test)
##        
##        rf_prediction = rf_model.predict(X_test)
##        knn_prediction = knn_model.predict(X_test)
##        ensemble_prediction = ensemble_model.predict(X_test)
##        
##        print('rf prediction is ', rf_prediction)
##        print('knn prediction is ', knn_prediction)
##        print('ensemble prediction is ', ensemble_prediction)
##        print('truth values are ', y_test.values)
##        
##        rf_accuracy = accuracy_score(y_test.values, rf_prediction)
##        knn_accuracy = accuracy_score(y_test.values, knn_prediction)
##        ensemble_accuracy = accuracy_score(y_test.values, ensemble_prediction)
##        
##        print(rf_accuracy, knn_accuracy, ensemble_accuracy)
##        rf_RESULTS.append(rf_accuracy)
##        knn_RESULTS.append(knn_accuracy)
##        ensemble_RESULTS.append(ensemble_accuracy)
##        
##        
##    print('RF Accuracy = ' + str( sum(rf_RESULTS) / len(rf_RESULTS)))
##    print('KNN Accuracy = ' + str( sum(knn_RESULTS) / len(knn_RESULTS)))
##    print('Ensemble Accuracy = ' + str( sum(ensemble_RESULTS) / len(ensemble_RESULTS)))
##    
##    
##cross_Validation(data)
