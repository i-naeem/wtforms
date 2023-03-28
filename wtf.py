from flask import Flask, render_template, request
from forms import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '2cedbf5ee35939c74d7ea22c58dc4aba5793facaebdef3153de60de738dd3c5a'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        return request.form.to_dict()
    form = RegistrationForm()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
