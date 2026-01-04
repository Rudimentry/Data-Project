from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random as r
import csv
import ast
import os




app = Flask(__name__)
#randomized marks
def calculation():
    return {
        "Cmath": r.randint(30,75),
        "Omath": r.randint(30,75),
        "Science": r.randint(30,75),
        "Nepali": r.randint(30,75),
        "English": r.randint(30,75),
        "Computer": r.randint(17,50),
        "Social": r.randint(30,75)}
#main window
@app.route('/')
def main():
    new_marks=calculation()
    return render_template('home.html', marks=new_marks)
#time for the save shit
@app.route('/save', methods=['POST'])
def save():
    choice = request.form.get('choice')
    raw = request.form.get('all_marks')
    if choice == "Science":
        choice=1
    else:
        choice=0


    marks_dih = ast.literal_eval(raw)
    marks_dih['Result'] = choice
    
    file= 'data.csv'
    exist = os.path.isfile(file)
    with open(file,'a' ,newline="") as f:
        headers= list(marks_dih.keys())



        writer = csv.DictWriter(f , fieldnames=headers)




        if not exist:
            writer.writeheader()
        writer.writerow(marks_dih)






    return redirect(url_for('main'))
        
        
        




#actual run of web app
if __name__ == '__main__':
    app.run(debug=True)

    