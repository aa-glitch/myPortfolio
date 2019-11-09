import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
@app.route('/works.html')
def works():
    return render_template('works.html')
"""

@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject =data["subject"]
        message =data["message"]
        file = database.write(f'\n{email}, {subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as csvFile:
        email = data["email"]
        subject =data["subject"]
        message =data["message"]
        cs_writer = csv.writer(csvFile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cs_writer.writerow([email, subject, message])

# @app.route('/thankyou/<email>')
# def thankyou(email=None):
#     return render_template('thankyou.html', email=request.args.get('email'))

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data['email'])
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save. Try Again!' 
            # return redirect('url_for('thankyou', email=data['email']))
    else:
        return "Something went wrong. Try Again!"

if __name__ == '__main__':
    app.run()