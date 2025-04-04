import numpy as np
import pandas as pd
import gradio as gr

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import warnings
warnings.filterwarnings('ignore')

# importing data
data = pd.read_csv('diabetes.csv')

# # checking data
print(data.head())
#
# getting variables
x = data.drop(['Outcome'], axis=1)
y = data['Outcome']

# splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y)

# scaling data
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

# instantiating and training model
model = MLPClassifier(max_iter=1000, alpha=1)
model.fit(x_train, y_train)
print("Model Accuracy on training set:", model.score(x_train, y_train))
print("Model Accuracy on Test Set:", model.score(x_test, y_test))

# creating gradio function
print(data.columns)

def diabetes(Pregnancies, Glucose, Blood_Pressure, SkinThickness, Insulin, BMI, Diabetes_Pedigree, Age):
    x = np.array([Pregnancies, Glucose, Blood_Pressure, SkinThickness, Insulin, BMI, Diabetes_Pedigree, Age])
    prediction = model.predict(x.reshape(1, -1))
    return prediction

outputs = gr.Textbox()
app = gr.Interface(fn=diabetes,
                   inputs=['number', 'number', 'number', 'number', 'number', 'number', 'number', 'number'],
                   outputs=outputs, description="This is a diabetes model")

# to launch app
app.launch(share=True)
