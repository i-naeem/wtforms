from flask import Flask, render_template
from forms import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '2cedbf5ee35939c74d7ea22c58dc4aba5793facaebdef3153de60de738dd3c5a'


@app.route('/')
def index():
    form = RegistrationForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
