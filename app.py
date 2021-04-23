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
@app.route('/grupdel')
def grupdel():
        
        return render_template("GrupDel.html",**locals())
@app.route('/viewGroup',methods = ['GET'])
def groupForm():
        group = request.args.get('idgroup')
        return render_template("groupForm.html",**locals())

@app.route('/userupdate')
def updateusers():
        
        return render_template("userUpdate.html",**locals())

def delchar(grup):
        return grup[1:]
@app.route('/readgroup')

def readgroup():
        read=str(executar()).strip("\\n'").strip("b'")
        grups = read.split("\\")
        grups[0]='n'+grups[0]
        grups=map(delchar,grups)
        return render_template("readgroup.html",**locals())

def executar():
        cmd = ["/usr/bin/grupspy.sh"]
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        grups, error = p.communicate()
        return grups

#Form functions, data reception only
#@app.route('/managUser', methods=['POST'])
#def managUser():


#@app.route('/managGroup', methods=['POST'])
#def managGroup():