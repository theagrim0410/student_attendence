from flask import Flask, render_template, request
import ploting
import plotting_all
import entry
import exit
import subprocess

app = Flask(__name__)

def speak(text):
    subprocess.Popen(['python', 'speak.py', text])
    
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/in')
def in1():
    entry.main2()
    return render_template('home.html')


@app.route('/out')
def out1():
    exit.main2()
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        name = request.form.get('Name')
        admission = request.form.get('addmision')
        if admission.lower() == "gcetall" and name.lower() == "teacher":
            plotting_all.get()
        else:
            ploting.plot(admission)

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
