from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'fat_cat_dress_up'

@app.route('/')
def home():
    return render_template("screen1.html")

@app.route('/fur_color', methods=['GET', 'POST'])
def dressup():
    if request.method == 'POST':
        selected_color = request.form.get('color')
        session['color'] = selected_color
        return redirect(url_for('about'))
    return render_template("screen2.html")

@app.route('/accessorize')
def about():
    color = session.get('color', 'default')
    return render_template("screen3.html", selected_color=color)

@app.route('/your_fat_cat', methods=['GET', 'POST'])
def your_fat_cat():
    color = session.get('color', 'default')
    accessories = []

    if request.method == 'POST':
        accessories_str = request.form.get('accessories', '')
        if accessories_str:
            accessories = accessories_str.split(',')

    return render_template("screen4.html", selected_color=color, accessories=accessories)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
