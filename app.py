import time
import requests
from fake_useragent import UserAgent
from datetime import date, datetime, timedelta
from flask import Flask, render_template, request
from pymongo import MongoClient
import subprocess as sp
import os

mongo_server="mongodb://127.0.0.1:27017"
client = MongoClient(mongo_server)

app = Flask("cowin_app")
port = 1111
hostname = "192.168.0.107"

db = "cowin"
collection = "flask"

@app.route('/', methods=['GET', 'POST'])
def home():

    file = open("names.yml" , "r+")
    file.truncate(0)
    file.close()

    file = open("emails.yml" , "r+")
    file.truncate(0)
    file.close()

    file = open("availables.yml" , "r+")
    file.truncate(0)
    file.close()

    return render_template("index.html")

@app.route('/form.html', methods=['GET', 'POST'])
def form():
    name=request.args.get("name")
    email=request.args.get("email")
    # print(name,email)
    client[db][collection].insert_one({"name": name, "email": email})

    f = open("names.yml" ,"a")
    f.write("name: ")
    f.write(name)
    f.close()

    f = open("emails.yml" ,"a")
    f.write("email: ")
    f.write(email)
    f.close()

    os.system("ansible-playbook mail.yml --vault-password-file=password.txt")

    return render_template("form.html")

@app.route('/availability.html', methods=['GET', 'POST'])
def avai():
    #name=request.args.get("name")
    age = int(request.args.get("age"))
    
    pinCodes = [ ]
    pincodes = request.args.get("pincode")
    pinCodes.append(pincodes) 

    print_flag = 'Y'
    num_days = int(request.args.get("days"))

    actual = datetime.today()

    list_format = [actual + timedelta(days=i) for i in range(num_days)]

    actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

    while True:
        #counter = 0   
        for pincode in pinCodes:   
            for given_date in actual_dates:
                user_agent = UserAgent()
                headers = {'User-Agent': user_agent.random}
                URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, given_date)
            result = requests.get(URL, headers=headers)
            #print(result.text)

            if result.ok:
                response_json = result.json()
                #flag = False
                if response_json["centers"]:
                    if(print_flag.lower() =='y'):
                        for center in response_json["centers"]:
                            #print(center)

                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :

                                    f = open("availables.yml" ,"a")

                                    f.write("Pincode: ")
                                    f.write(pincode)
                                    f.write("\n")

                                    f.write("Date: ")
                                    f.write(format(given_date))
                                    f.write("\n")

                                    f.write("Center Name: ")
                                    f.write(center["name"])
                                    f.write("\n")

                                    f.write("Block Name: ")
                                    f.write(center["block_name"])
                                    f.write("\n")

                                    f.write("Price: ")
                                    f.write(center["fee_type"])
                                    f.write("\n")

                                    f.write("Availablity: ")
                                    f.write(str(session["available_capacity"]))
                                    f.write("\n")

                                    f.write("Vaccine Type: ")
                                    if(session["vaccine"] != ''):
                                        f.write(session["vaccine"])
                                    f.write("\n")
                                    f.write("\n")

                                    f.close()

                        print("Vaccine is available")

                        os.system("ansible-playbook avaimail.yml --vault-password-file=password.txt")

                else:
                    print('No Vaccine found !!')
                    os.system("ansible-playbook notavaimail.yml --vault-password-file=password.txt")

        return render_template("availability.html")

@app.route('/notify.html', methods=['GET', 'POST'])
def notify():
    return render_template("notify.html")

app.run(debug=True, port=port, host=hostname)