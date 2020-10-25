
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('about.html')

@app.route('/videopage/')
def videopage():
    return render_template('videopage.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/pasttournaments')
def pasttournaments():
    return render_template("pasttournaments.html")

@app.route('/pictures')
def pictures():
    return render_template("pictures.html")

@app.route('/bio/')
def bio():
    return render_template("bio.html")


#beginning of twillio
from twilio.twiml.messaging_response import MessagingResponse


dictt = {' ': '0', 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8',
         'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17',
         'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}


def get_key(val):
    for key, value in dictt.items():
        if val == value:
            return key
        else:
            return 'cannot find'


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    global dictt
    final_letter = 0
    numbers = []
    arraytwo = []
    msg = request.form['Body']
    message_body = msg.lower()
    print(message_body)
    if message_body[0] not in dictt.keys():
        array = message_body.split(" ")
        print("array is : " + str(array))
        for val in array:
            if val == " " or val == "" or val == "  ":
                array.remove(val)
        print("array without spaces is : " + str(array))
        for x in array:
            a = x[3:8]
            print(a)
            arraytwo.append(a)
        print("array is now: " + str(arraytwo))
        for a in arraytwo:
            thirtytwo = 0
            sixteen = 0
            eight = 0
            four = 0
            two = 0
            one = 0
            if a[0] == "1":
                sixteen = 1
                print(sixteen)
            else:
                sixteen = 0
                print(sixteen)
            if a[1] == "1":
                eight = 1
                print(eight)
            else:
                eight = 0
                print(eight)
            if a[2] == "1":
                four = 1
                print(four)
            else:
                four = 0
                print(four)
            if a[3] == "1":
                two = 1
                print(two)
            else:
                two = 0
                print(two)
            if a[4] == "1":
                one = 1
                print(one)
            else:
                one = 0
                print(one)
            number = int((sixteen * 16) + (eight * 8) + (four * 4) + (two * 2) + (one*1))
            print(number)
            def get_key(val):
                for key, value in dictt.items():
                    if val == value:
                        return key
            final_letter = get_key(str(number))
            print(final_letter)
            numbers.append(str(final_letter))
        resp = MessagingResponse()
        data = ("".join(map(str, numbers)))
        resp.message(data)
    else:
        array = ([message_body[i:i + 1] for i in range(0, len(message_body), 1)])
        for x in array:
            thirtytwo = 0
            sixteen = 0
            eight = 0
            four = 0
            two = 0
            one = 0
            letter_number = int(dictt[x])
            if letter_number - 16 > -1:
                sixteen = 1
                letter_number -= 16
            if letter_number - 8 > -1:
                eight = 1
                letter_number -= 8
            if letter_number - 4 > -1:
                four = 1
                letter_number -= 4
            if letter_number - 2 > -1:
                two = 1
                letter_number -= 2
            if letter_number - 1 > -1:
                one = 1
                letter_number -= 1

            if thirtytwo == 0 and sixteen == 0 and eight == 0 and four == 0 and two == 0 and one == 0:
                numbers.append("00100000")
            else:
                numbers.append(("011" + str(sixteen) + str(eight) + str(four) + str(two) + str(one) + " "))
                print(("011" + str(sixteen) + str(eight) + str(four) + str(two) + str(one) + " "))


        resp = MessagingResponse()
        data = (' '.join(map(str, numbers)))
        resp.message(data)

    return str(resp)


"""
import gspread
import operator
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('team training-0d0c79f0bfeb.json', scope)
client = gspread.authorize(creds)

spreadsheetName = "Team Training Challenge"
sheetName = "LEADERBOARD"  # <--- please set the sheet name here.
spreadsheet = client.open(spreadsheetName)
sheet = spreadsheet.worksheet(sheetName)
@app.route("/tt", methods=['GET', 'POST'])
def tt_reply():
    scores = []
    print("hello")
    alexarmy = int(sheet.cell(9, 2).value)
    saftb = int(sheet.cell(18, 2).value)
    sexylexy = int(sheet.cell(27, 2).value)
    quarinteam = int(sheet.cell(36, 2).value)
    mghsl = int(sheet.cell(9, 4).value)
    saltines = int(sheet.cell(18, 4).value)
    sixpax = int(sheet.cell(27, 4).value)
    cc = int(sheet.cell(9, 6).value)
    team8 = int(sheet.cell(18, 6).value)
    orangecrushers = int(sheet.cell(27, 6).value)

    points = {"Alex's army": alexarmy, "SAFTB": saftb, "SexyLexy": sexylexy, "MGHSL 2020 Champs": mghsl, "Saltines": saltines,
              "6Pax": sixpax, "CC": cc, "team8": team8, "Orange Crushers": orangecrushers, "The Quarinteam": quarinteam}
    print(points)
    winner = max(points, key=points.get)  # Just use 'min' instead of 'max' for minimum.
    print(winner, points[winner])
    for k, v in sorted(points.items(), key=lambda x: x[1], reverse=True):
        print(str(k) + ": " + str(v))
        scores.append(str(k) + ": " + str(v))
    data = ("Currently the winning team is: " + str(winner) + ", with " + str(points.get(winner)) + " points."+ "\n" + "\n"+ '\n'.join(scores))
    resp = MessagingResponse()
    from operator import itemgetter
    data = ("hello")
    resp.message(data)
    return str(resp)
"""
if __name__ == "__main__":
    app.run("68.183.135.1")


#0oarg55f3VVMPRpYw4x6
#QcYukGl77_HsWielK4d2zIoDjlNMUqKvT0ONkqE0
#login 00nRSZc8SFZACLJRVRKXpIIbKt9RG4pn0MGwWwvY0a
