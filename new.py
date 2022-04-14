"""
  Restful webservice for simple calculator
"""
from flask import Flask, redirect, url_for, request, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello():
     retval  = "<b> Hello ENTD320, Welcome to my Restful webservices calculator </b></br> "
     retval += "Example; <br>"
     retval += " to add  two number  /mycalc/add/7/5/ <br> "
     retval += " to subtract two number  /mycalc/sub/14/7/ <br>"
     retval += " to multiply two number  /mycalc/mul/4/5/ <br> "
     retval += " to divide two number  /mycalc/div/14/7/ <br>"
     retval += " to allInOneDict two number  /mycalc/allInOneDict/6/3/ <br> "
     retval += " to allinOneList two number  /mycalc/allinOneList/14/7/ <br>"
     retval += " to get the form /form <br>"
     return retval

@app.route("/form")
def form():
     return render_template("w3.html")

@app.route('/mycalc/add/<fnum>/<snum>/', methods=['GET', 'POST'])
def add(fnum, snum):
    return "adding " + str(float(fnum)+float(snum))

@app.route('/mycalc/sub/<fnum>/<snum>/', methods=['GET', 'POST'])
def sub(fnum, snum):
    return "subtracting " + str(float(fnum)-float(snum))

@app.route('/mycalc/mul/<fnum>/<snum>/', methods=['GET', 'POST'])
def mul(fnum, snum):
    return "multiplying " + str(float(fnum)*float(snum))

@app.route('/mycalc/div/<fnum>/<snum>/', methods=['GET', 'POST'])
def div(fnum, snum):
    return "dividing " + str(float(fnum)/float(snum))

@app.route('/mycalc/allInOneDict/<fnum>/<snum>/', methods=['GET', 'POST'])
def allInOneDict(fnum,snum):
    arithmaticDict={}
    arithmaticDict["add"]=add(fnum,snum)
    arithmaticDict["sub"]=sub(fnum,snum)
    arithmaticDict["mul"]=mul(fnum,snum)
    arithmaticDict["div"]=div(fnum,snum)
    return "allInOneDict " + json.dumps(arithmaticDict)

@app.route('/mycalc/allinOneList/<fnum>/<snum>/', methods=['GET', 'POST'])
def allinOneList(fnum,snum):
    arithmeticList=[]
    arithmeticList.append(add(fnum,snum))
    arithmeticList.append(sub(fnum,snum))
    arithmeticList.append(mul(fnum,snum))
    arithmeticList.append(div(fnum,snum))
    return "allinOneList " + json.dumps(arithmeticList)

if __name__ == '__main__':
    app.run(port=5200, debug=True)
