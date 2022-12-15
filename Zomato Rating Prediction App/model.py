import pandas as pd
import pickle
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('zomato.csv')
x = df.drop('rate', axis=1)
y = df['rate']

x_train, x_test, y_train, y_test = train_test_split(x,y, 
	                        test_size = 0.3, random_state= 10)

et_model = ExtraTreesRegressor(n_estimators = 120)
et_model.fit(x_train, y_train)
y_predict = et_model.predict(x_test)
pickle.dump(et_model,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
score = r2_score(y_test, y_predict)
print(score*100)