import pickle
import pandas as pd
from array_converter import array
from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder='template', static_folder='template/static')
with open('price_predict.pkl', 'rb') as file:
    model = pickle.load(file)


def get_data(path):
    df = pd.read_csv(path)
    return df
path = 'dataset/kc_house_data.csv'
df = get_data(path)


@app.route('/')
def display_gui():
    return render_template('pred_page.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    floors = float(request.form['floors'])
    waterfront = int(request.form['waterfront'])
    grade = int(request.form['grade'])

    prediction = float(model.predict(array.get_array(bedrooms=bedrooms, bathrooms=bathrooms,
                                               floors=floors, waterfront=waterfront,
                                               grade=grade).reshape(1,-1)))
    
    def limit_comma_pred(value, limit=2):
        v = str(value).split(".")
        return float(v[0]+"."+v[1][:limit])
    
    return render_template('pred_page.html', prediction=f'${limit_comma_pred(prediction)}')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='localhost', port=port, debug=True)
