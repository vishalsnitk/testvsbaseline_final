# 

from flask import Flask, render_template
from dataprocessing import generate_dataframe
import os

app = Flask(__name__)

@app.route('/')
def home():
    current_directory = os.path.join(app.root_path, 'static', 'test')
    df = generate_dataframe(current_directory)
    pivot_table = df.pivot(index='TestName', columns='Baseline', values='CumulativeTime').fillna(0)
    return render_template('testvsbaseline.html', table=pivot_table)

@app.route('/test/<test_name>')
def test_detail(test_name):
    # Handle the logic for the test detail page here
    return f"Details for test: {test_name}"

if __name__ == '__main__':
    app.run(debug=True)
