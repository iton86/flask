from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

data = {
    "2022-01-01": "Data for January 1st, 2022",
    "2022-01-02": "Data for January 2nd, 2022",
    "2022-01-03": "Data for January 3rd, 2022"
}

data = pd.read_csv("google_analytics_api_data.csv")

# @app.route('/data/<date>', methods=['GET'])
# def get_data_by_date(date):
#     if date in data:
#         return jsonify({date: data[date]})
#     else:
#         return jsonify({"error": "Data not found for date {}".format(date)}), 404

@app.route('/data/<date>', methods=['GET'])
def get_data_by_date(date):
    date = int(date)
    if date in list(data['date'].unique()):
        return jsonify({date: data.query("date == @date")})
    else:
        return jsonify({"error": "Data not found for date {}".format(date)}), 404    
    
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
