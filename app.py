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
        members = obtenirMembres(group)
        
        return render_template("viewGroup.html",**locals())

@app.route('/viewUser',methods = ['GET'])
def userForm():
        user = request.args.get('iduser')
        grups=obtenirUsers(user)
        
        return render_template("viewUser.html",**locals())
@app.route('/groupUpdate',methods = ['GET'])
def groupUpdate():
        group = request.args.get('idgroup')
        members = obtenirMembres(group)
        
        return render_template("groupUpdate.html",**locals())

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
       # cmd = ["/usr/bin/grupspy.sh"]
        cmd = ["cut", "-d:","-f1", "/etc/group", "| sort "]
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        grups, error = p.communicate()
        return grups

def delcharuser(user):
        return user[1:]
@app.route('/readuser')

def readusers():
        users=executaruser()
        return render_template("readuser.html",**locals())

def executaruser():
       # cmd = ["/usr/bin/grupspy.sh"]
        cmd = ["cut", "-d:","-f1", "/etc/passwd", "|", "sort"]
        #p1 = subprocess.Popen(["cut", "-d:","-f1", "/etc/passwd"], stdout=subprocess.PIPE)
        #p2 = subprocess.Popen(["sort"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        users, error = p.communicate()
        read=str(users).strip("\\n'").strip("b'")
        users = read.split("\\")
        users[0]='n'+users[0]
        users=map(delcharuser,users)
        return users

def obtenirMembres(group):
        cmd = ["members", group]
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        members, error = p.communicate()
        return members

def obtenirUsers(user):
        cmd = ["getent", "group", user, "|", "cut", "-d:", "-f4"]
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        groupsin, error = p.communicate()
        return groupsin

#Form functions, data reception only
#@app.route('/managUser', methods=['POST'])
#def managUser():


#@app.route('/managGroup', methods=['POST'])
#def managGroup():