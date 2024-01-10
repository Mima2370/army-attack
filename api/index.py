from flask import Flask, render_template, redirect
import scratchattach as scratch3
import os
app = Flask(__name__)

session = scratch3.login(os.environ.get('Username'),os.environ.get('Password'))

@app.route('/')
def hello():
    project = session.connect_project(project_id=764742970)
    print(project.project_token)
    return redirect("https://turbowarp.org/764742970?cloud_host=wss://cpwscloudserver-dev--cpwscratch.repl.co/&size=640x360&clones=Infinity&fps=60&hqpen&token=" + project.project_token, code=302)


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
