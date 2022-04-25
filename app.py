from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle= 'Welcome to VTM')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle= 'About Vertical Tank Maintenance')

@app.route('/estimate', methods= ['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = int(form['radius'])
        height= int(form['height'])
        top_area = 3.14 * (radius**2)
        side_area = 2*(3.14* (radius* height))
        total_area_in = top_area + side_area 
        total_area_sq_ft = total_area_in/ 144
        material_cost= total_area_sq_ft * 25
        labor_cost= total_area_sq_ft * 15 
        total_cost_estimate = material_cost + labor_cost
        return render_template('estimate.html', final_estimate = total_cost_estimate)
    return render_template ('estimate.html', pageTitle= 'Estimator Calculator ')

if __name__ == '__main__':
    app.run(debug=True)