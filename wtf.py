from flask import Flask, render_template
from forms import RegistrationForm


app = Flask(__name__)


@app.route('/')
def index():
    form = RegistrationForm()

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
