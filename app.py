from flask import Flask, url_for, request, render_template, redirect, session
import functions
import os


app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
    return redirect(url_for("set"))


@app.route("/set", methods = ["POST", "GET"])
def set():
    if request.method == "POST":
        root = request.form["root"]
        if os.path.exists(root) and os.path.isdir(root):
            session["root"] = root
            return redirect(url_for("options"))
        else:
            text = "It is no a valid path to directory, try again."
            return render_template("index.html", msg = text)
    else:
        return render_template("index.html")

@app.route("/options", methods=["POST", "GET"])
def options():
    if "root" in session:
        root = session["root"]
    else:
        return redirect(url_for("set"))

    if "button_0" in request.form:
        return redirect(url_for("move"))
    elif "button_1" in request.form:
        return redirect(url_for("whole_list"))
    elif "button_2" in request.form:
        return redirect(url_for("info"))
    elif "button_3" in request.form:
        return redirect(url_for("delete_file"))
    elif "button_4" in request.form:
        return redirect(url_for("create_file"))
    elif "button_5" in request.form:
        return redirect(url_for("set"))

    return render_template("options.html", root = root)

@app.route("/move", methods=["POST", "GET"])
def move():
    if "root" in session:
        root = session["root"]
    else:
        return redirect(url_for("set"))

    if "move" in request.form:
        root = root + '/' + request.form["subfolder"]
        if os.path.exists(root) and os.path.isdir(root):
            session["root"] = root
            return redirect(url_for("options"))
        else:
            text = "It is no a valid path to directory, try again."
            return render_template("subfolder.html", msg=text)

    elif "return" in request.form:
        return redirect(url_for("options"))

    return render_template("subfolder.html")


@app.route("/whole_list", methods=["POST", "GET"])
def whole_list():
    if "root" in session:
        root = session["root"]
    else:
        return redirect(url_for("set"))

    if "return" in request.form:
        return redirect(url_for("options"))

    text = functions.get_whole_list(root)
    return render_template("whole_list.html", content = text)


@app.route("/info", methods=["POST", "GET"])
def info():
    if "root" in session:
        root = session["root"]
    else:
        return redirect(url_for("set"))

    if "show_me" in request.form:
        fullpath = root + '/' + request.form["file"]
        text = functions.get_info(fullpath)
        return render_template("info.html", content = text)

    elif "return0" in request.form:
        return redirect(url_for("options"))

    return render_template("info.html")


@app.route("/delete", methods=["POST", "GET"])
def delete_file():
    if "root" in session:
        root = session["root"]
    else:
        return redirect(url_for("set"))

    if "delete" in request.form:
        fullpath = root + '/' + request.form["file"]
        text = functions.delete_by_path(fullpath)
        return render_template("delete_file.html", content = text)

    elif "return" in request.form:
        return redirect(url_for("options"))

    return render_template("delete_file.html")


@app.route("/create", methods=["POST", "GET"])
def create_file():
    if "root" in session:
        root = session["root"]
    else:
        return redirect(url_for("set"))

    if "create" in request.form:
        fullpath = root + '/' + request.form["file"]
        text = functions.create_file_by_path(fullpath)
        return render_template("create_file.html", content = text)

    elif "return" in request.form:
        return redirect(url_for("options"))

    return render_template("create_file.html")

if __name__ == '__main__':
    app.run(debug=True)
