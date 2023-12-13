from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Python Developer',
        'location': 'New York',
        'salary': '$80000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Miami',
        'salary': '$100000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Remote'
    },
    {
        'id': 4,
        'title': 'C++ Developer',
        'location': 'Houston',
        'salary': '$90000'
    },
    {
        'id': 5,
        'title': 'Web Developer',
        'location': 'Phoenix',
        'salary': '$75000'
    },
    {
        'id': 6,
        'title': 'Database Admin',
        'location': 'Remote',
        'salary': '$100000'
    }

]


@app.route("/")
def hello_world():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Property Appraiser')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)