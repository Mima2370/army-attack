from flask import Flask, render_template, request, redirect, session, send_from_directory
import os
from pathlib import Path
app = Flask(__name__, template_folder=os.path.join(Path(__file__).parents[1], "armyattack"))
app.secret_key = 'ARMYSECRET123'

STYLES_DIR = os.path.join(Path(__file__).parents[1], "armyattack", "styles")
MODS_DIR = os.path.join(Path(__file__).parents[1], "mods")

available_mods = ["colossal", "truecrimson", "crimson", "hardmode", "swapped", "swapped2"]

@app.route('/')
def homepage():
    # Adding a homepage here one day
    return redirect("./play")

@app.route('/play')
def play():
    
    if request.args.get('mod'):
        mod = request.args.get('mod')
        if mod in available_mods:
            session["mod"] = mod
        else:
            return "Unknown mod. Please check your URL for spelling mistakes."
    else:
        session["mod"] = "none"
    return render_template("index.html")

@app.route('/styles/<path:path>')
def styles(path):
    print(path)
    return send_from_directory(STYLES_DIR, path)

@app.route('/assets/<path:path>')
def assets(path):
    if not session["mod"]:
        session["mod"] = "none"
    return send_from_directory(os.path.join(MODS_DIR, session["mod"], "assets"), path)

@app.route('/config/<path:path>')
def config(path):
    if not session["mod"]:
        session["mod"] = "none"
    return send_from_directory(os.path.join(MODS_DIR, session["mod"], "config"), path)

@app.route('/data/<path:path>')
def data(path):
    if not session["mod"]:
        session["mod"] = "none"
    return send_from_directory(os.path.join(MODS_DIR, session["mod"], "data"), path)