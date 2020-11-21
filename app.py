from flask import Flask,request,render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/', methods = ['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        Blood_Pressure = int(request.form['Blood_Pressure'])
        Skin_Thickness = int(request.form['Skin'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        Pedigree = float(request.form['Pedigree'])
        Age = int(request.form['Age'])

        prediction = model.predict([[Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,Pedigree,Age]])

        if prediction == 1:
            return render_template('index.html', prediction_text = "You might have diabetes. Please consult with your doctor. ")
        else :
            return render_template('index.html', prediction_text = "You don't have diabetes.")
               
if __name__ == "__main__":
    app.run(debug = True)
