from flask import Flask, render_template, url_for, request
import subprocess
import urllib
import csv
app = Flask(__name__)

#Shell functions


#Functions redirections
@app.route('/')
def main():
        
        return render_template("index.html",**locals())

@app.route('/groups')
def maingrups():
        
        return render_template("groupForm.html",**locals())

@app.route('/users')
def mainusuaris():
        
        return render_template("userForm.html",**locals())

@app.route('/userdel')
def delusers():
        
        return render_template("userDel.html",**locals())


#Form functions, data reception only
#@app.route('/managUser', methods=['POST'])
#def managUser():


#@app.route('/managGroup', methods=['POST'])
#def managGroup():