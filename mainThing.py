from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

#model = pickle.load(open('C:/Users/14086/Downloads/heart_model.sav', 'rb'))
conversion = {'No': 0, 'Yes': 1, 'Female': 0, 'Male': 1, '18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4, '45-49': 5, '50-54': 6, '55-59': 7, '60-64': 8, '65-69': 9, '70-74': 10, '75-79': 11, '80 or older': 12, 'American Indian/Alaskan Native': 0, 'Asian': 1, 'Black': 2, 'Hispanic': 3, 'Other': 4, 'White': 5, 'Fair': 0, 'Good': 1, 'Poor': 2, 'Very good': 3}
uniqueCol = {'HeartDisease': ['No', 'Yes'], 'BMI': [], 'Smoking': ['No', 'Yes'], 'AlcoholDrinking': ['No', 'Yes'], 'Stroke': ['No', 'Yes'], 'PhysicalHealth': [], 'MentalHealth': [], 'DiffWalking': ['No', 'Yes'], 'Sex': ['Female', 'Male'], 'AgeCategory': ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'], 'Race': ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White'], 'Diabetic': ['No', 'Yes'], 'PhysicalActivity': ['No', 'Yes'], 'GenHealth': ['Fair', 'Good', 'Poor', 'Very good'], 'SleepTime': [], 'Asthma': ['No', 'Yes'], 'KidneyDisease': ['No', 'Yes'], 'SkinCancer': ['No', 'Yes']}

def numeric_arr(arr):
  new_arr = []
  for i in range(len(arr)):
    if type(arr[i]) is float or type(arr[i]) is int:
      new_arr.append(arr[i])
    else:
      if '-' not in arr[i]: new_arr.append(conversion[arr[i]])
      elif arr[i] != '75-79':
        new_arr.append(conversion[arr[i]]+2)
      else:
        new_arr.append(conversion[arr[i]]+1)
  return new_arr

def prob_heart_disease(arr):
  arr = np.array(arr).reshape(1,-1)
  prob = model.predict_proba(arr)[0][1]
  return int(prob*100)

  
app = Flask(__name__)

@app.route('/')
def man():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    data = []
    for letter in 'abcdefghijklmnopq':
        data.append(request.form[letter])
    arr = []
    for d in data:
        try:
            arr.append(float(d))
        except:
            arr.append(d)

    arr = np.array(numeric_arr(arr))
    #prob = prob_heart_disease(arr)

    return render_template('result.html', prob=50)

if __name__ == "__main__":
    app.run(debug=False)