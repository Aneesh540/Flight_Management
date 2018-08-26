from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:ANEESH540@localhost:5432/lecture3")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    heading = "All available flights"
    return render_template("index.html",heading=heading,flights=flights)


@app.route("/book_a_flight",methods=["POST"])
def book_a_flight():
    flight_id = int(request.form.get("flight_id"))
    flights = db.execute("SELECT * FROM flights where id = :id", {"id":flight_id})
    passenger = db.execute("select * from passengers where flight_id = :id",{"id":flight_id})
    return render_template("flight_detail.html",flights=flights,passenger=passenger,flight_id="Details")



if __name__=="__main__":
    app.run(debug=True)
