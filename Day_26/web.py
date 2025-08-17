#Exercice jour26

#Structures
python_for_web/
│
├── static/
│   └── css/
│       └── main.css
├── templates/
│   ├── layout.html
│   ├── home.html
│   ├── about.html
│   └── post.html
├── app.py
├── requirements.txt
└── Procfile


#ROUTES

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Empêche le cache des fichiers statiques

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)  # Tu peux traiter/afficher le texte ici
        return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


#XML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}"/>
    <title>{% if title %}30 Days of Python - {{ title }}{% else %}30 Days of Python{% endif %}</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('home') }}">Home</a></li>
                <li><a href="{{ url_for('about') }}">About</a></li>
                <li><a href="{{ url_for('post') }}">Text Analyzer</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>


{% extends 'layout.html' %}
{% block content %}
<h1>Welcome to {{ name }}</h1>
<ul>
    {% for tech in techs %}
        <li>{{ tech }}</li>
    {% endfor %}
</ul>
{% endblock %}


{% extends 'layout.html' %}
{% block content %}
<div>
    <h1>Text Analyzer</h1>
    <form action="{{ url_for('post') }}" method="POST">
        <textarea rows="10" name="content"></textarea>
        <br>
        <input type="submit" value="Analyser le texte">
    </form>
</div>
{% endblock %}
