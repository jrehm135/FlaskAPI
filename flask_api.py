#!flask/bin/python
import json
import datetime

from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import socket
import os
#Try catch necessary to avoid os.uname failure on windows
try:
    #we still need to verify it is a pi, this will do good enough
    if os.uname()[4][:3] == 'arm':
        import rpi_gpio
        print('RPI')
except AttributeError:
    print('Windows Machine')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

startTime = 0
ip_address = socket.gethostbyname(socket.gethostname())

class Servo():
    pass

@app.route('/')
def index():
    data = {'ip_address': ip_address}
    return render_template("arm_page.html", data=data)

@app.route('/move_arm', methods=['POST'])
@cross_origin()
def moveArm():
    print('moving arm')
    servoVal = 0
    timeElapsed = 0

    data = request.get_data()
    payload = json.loads(request.data.decode('UTF-8'))
    servoName = payload["servo"]
    mServo = Servo()

    if servoName == "open_claw":
        mServo.servoVal = 1
        mServo.dutyCycle = 10
    elif servoName == "close_claw":
        mServo.servoVal = 1
        mServo.dutyCycle = 5
    elif servoName == "rotate_left":
        mServo.servoVal = 8
        mServo.dutyCycle = 10
    elif servoName == "rotate_right":
        mServo.servoVal = 8
        mServo.dutyCycle = 5
    elif servoName == "up_icon":
        mServo.servoVal = 2
        mServo.dutyCycle = 10
    elif servoName == "down_icon":
        mServo.servoVal = 2
        mServo.dutyCycle = 5

    startEvent = payload["startEvent"]

    global startTime
    if startEvent:
        startTime = datetime.datetime.now()
    else:
        timeElapsed = datetime.datetime.now() - startTime
        requestTime = str(timeElapsed.seconds) + ':' + str(timeElapsed.microseconds)
        print(requestTime)

    mServo.servoNum = rpi_gpio.select_servos(mServo.servoVal)
    rpi_gpio.pwm_move(mServo)
    return "Moved arm!"

if __name__ == '__main__':
    app.run(debug=True)
