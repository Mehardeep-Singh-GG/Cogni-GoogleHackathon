from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def show_form():
    return render_template('form1.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        learn = request.form['learn']
        implementation = request.form['implementation']
        # Here, you can process the form data as needed, such as saving to a database, etc.
        # For this example, let's just print the submitted data
        print("Learn:", learn)
        print("Implementation:", implementation)
        return render_template('loading.html')  # Redirect to the index page after form submission

@app.route('/form_2')
def show_form_2():
    return render_template('form2.html')

@app.route('/submit_form_2', methods=['POST'])
def submit_form_2():
    if request.method == 'POST':
        learn = request.form['learn']
        implementation = request.form['implementation']
        # Here, you can process the form data as needed, such as saving to a database, etc.
        # For this example, let's just print the submitted data
        print("Learn:", learn)
        print("Implementation:", implementation)
        return render_template('loading.html')  # Redirect to the index page after form submission



if __name__ == '__main__':
    app.run(debug=True)
