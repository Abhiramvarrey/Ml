from django.shortcuts import render
import joblib
import pandas as pd

def welcome(request):
    return render(request, 'index.html')


# Load the trained model and label encoder
model = joblib.load('models\\random_forest_model.sav')
label_encoder = joblib.load('models\\device_label_encoder.sav')


def predict_failure(request):
    # Convert date to datetime if necessary
    date = pd.to_datetime(request.GET['date'])
    metrics=[]
    metrics.append(request.GET['metrics1'])
    metrics.append(request.GET['metrics2'])
    metrics.append(request.GET['metrics3'])
    metrics.append(request.GET['metrics4'])
    metrics.append(request.GET['metrics5'])
    metrics.append(request.GET['metrics6'])
    metrics.append(request.GET['metrics7'])
    metrics.append(request.GET['metrics8'])
    metrics.append(request.GET['metrics9'])
    device = request.GET['device']

    # Encode the date
    date_encoded = int(date.strftime('%j'))

    # Encode the device
    device_encoded = label_encoder.transform([device])[0]

    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'device': [device_encoded],
        'metric1': [metrics[0]],
        'metric2': [metrics[1]],
        'metric3': [metrics[2]],
        'metric4': [metrics[3]],
        'metric5': [metrics[4]],
        'metric6': [metrics[5]],
        'metric7': [metrics[6]],
        'metric8': [metrics[7]],
        'metric9': [metrics[8]]
    })

    # Make the prediction
    prediction = model.predict(input_data)
    return render(request,'result.html',{'prediction':prediction[0]})


'''# Example usage
date = '1/1/2015'
device = 'S1F01085'
metrics = [215630672, 55, 0, 52, 6, 407438, 0, 0, 7]
prediction = predict_failure(date, device, metrics)
print(f"Prediction (0 for no failure, 1 for failure): {prediction}")'''


def user(request):
    username = request.GET["username"]
    return render(request, 'user.html', {'name': username})
