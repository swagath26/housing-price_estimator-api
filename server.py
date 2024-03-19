from flask import Flask, request, jsonify
import util

app =  Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        "locations" : util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

@app.route("/get_area_type_names")
def get_area_type_names():
    response = jsonify({
        "area_types" : util.get_area_type_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response


@app.route('/predict_price')
def predict_home_price():
    price = 0
    area = request.args.get('total_sqft')
    location = request.args.get('location')
    area_type = request.args.get('area_type')
    bathrooms = request.args.get('bath')
    bedrooms = request.args.get('bedrooms')
    price = util.get_estimated_price(int(bathrooms), int(bedrooms), float(area), area_type, location)
    response = jsonify({
        'success' : True,
        'estimated_price' : price
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

if __name__ == "__main__":
    print("Starting server for house price prediction!")
    app.run()