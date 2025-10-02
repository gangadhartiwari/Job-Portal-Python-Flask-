from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id" : 1, 
        "title" : "Data Analyst",
        "location" : "Pune", 
        "salary" : 400000
    },

    {
        "id" : 2, 
        "title" : "Software Engineer",
        "location" : "Banglore", 
        "salary" : 1000000
    }, 
    {
        "id" : 3, 
        "title" : "Data Scientist",
        "location" : "Chennai", 
        "salary" : 1500000
    },
    {
        "id" : 4, 
        "title" : "AI/ML Eng.",
        "location" : "USA", 
        "salary" : 2500000
    }
]

@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS, company_name = "GDT")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)

