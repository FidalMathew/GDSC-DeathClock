from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import numpy as np
import math

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def getQuery():
    if request.method == "POST":

        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
        else:
            return 'Content-Type not supported!'

        data1 = json["data1"]
        input = (data1, 2, 0, 6, 6, 1, 1, 70, 0, 0,
                 0, 11, 0, 1)  # row 1 data values

        # converting input data (tuple) to a numpy array
        input_data_arr = np.asarray(input)
        print(input_data_arr)

        input_data_reshaped = input_data_arr.reshape(1, -1)
        print(input_data_reshaped)

        # 2D array as model.predict() takes in 2D array as an argument
        # 3 and 2 -> 6
        # 1 and 6 -> 6

        # arr = np.array([[data1, data2, data3, data4]])
        prediction = model.predict(input_data_reshaped)
        ans = math.floor(prediction)

        # pred = model.predict(arr)

    response = jsonify({"pred": ans})
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
