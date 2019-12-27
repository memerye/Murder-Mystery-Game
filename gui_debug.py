from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        return redirect(url_for("login"))
    else:
        return render_template("welcome.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    message = None
    # Hard coding!!!!!
    user_existing = False
    if request.method == "POST":
        if request.form["action"] == "signup":
            if user_existing is True:
                error = "The user has existed"
            else:
                message = "You've signed up"
                return render_template("login.html", msg1=message)
        elif request.form["action"] == "login":
            if request.form["username"] != "lily" \
                    or request.form["psw"] != "123":
                error = "Invalid login please try again"
            else:
                return redirect(url_for("choose_ch",
                                        u_name=request.form["username"]))
    return render_template("login.html", error=error)


@app.route("/<u_name>/choose_ch", methods=["GET", "POST"])
def choose_ch(u_name):
    if request.method == "POST":
        # check if user has chosen one ch or if it matches to the chosen one
        ch_name = request.form["choose_ch"]
        return redirect(url_for("play", u_name=u_name, ch_name=ch_name))
    else:
        return render_template("choose_ch.html")


@app.route("/<u_name>/play/<ch_name>/", methods=["GET", "POST"])
def play(u_name, ch_name):
    if request.method == "GET":
        message = {"u_name": u_name, "ch_name": ch_name}
        return render_template("play.html", msg_info=message)


@app.route("/start_round1/")
def start_round1():
    name1 = request.args.get("name_ready_for_1")
    # Receive the names that are ready.
    # OK! Everyone is ready for round 1?
    check = "lily"
    if str(name1).lower() == check:
        return jsonify(result="1")
    else:
        return jsonify(result="0")


@app.route("/start_round2/")
def start_round2():
    name1 = request.args.get("name_ready_for_2")
    # Receive the names that are ready.
    # OK! Everyone is ready for round 1?
    check = "lily"
    if str(name1).lower() == check:
        return jsonify(result="1")
    else:
        return jsonify(result="0")


@app.route("/clue_num/")
def clue_num():
    # return: place=[已搜, 所有】
    return jsonify(p1=[1, 3], p2=[1, 4], p3=[0, 3])


@app.route("/find_clue/")
def find_clue():
    name = str(request.args.get("name_find_clue1")).lower()
    place = str(request.args.get("name_place")).lower()
    # somehow get the clue in someplace for someone
    # update numbers in place
    return jsonify(u_name=name, place=place, clue="线索1", hidden=True)


if __name__ == "__main__":
    app.run(debug=True)
