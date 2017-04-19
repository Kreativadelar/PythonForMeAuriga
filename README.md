# Python For Me Auriga

This is a port of the PythonForMegaPi Python librari to work with Me Auriga

### OBS! The future developing is done in https://github.com/Kreativadelar/PythonForMeAuriga repo ###

## How To Use
### Prepare for Arduino
 * Download the Arduino library for Makeblock https://github.com/Makeblock-official/Makeblock-Libraries/archive/master.zip
 * Copy the makeblock folder to your arduino default library. Your Arduino library folder should now look like this 
   * (on Windows): ```[x:\Users\XXX\Documents]\Arduino\libraries\makeblock\src```
   * (on Mac OSX): ```[\Users\XXX\Documents]\Arduino\libraries\makeblock\src```
 * Open Arduino IDE, choose the firmware from <em>File&gt;Examples</em>.
 ** Use the Firmware_For_Auriga
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/firmware.jpg)
 * Compile and upload firmware according to your board type.

### Prepare for Raspberry Pi
 * On your Raspberry Pi, disable the login prompt from Desktop->Menu->Preferences->Raspberry Pi Configuration.

![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/serial.jpg)
 * install python library for Makeblock
 ```
 sudo pip install megapi
 ```
 * the initial code for python.
```
 from megapi import *
 bot = MegaPi()
 bot.start() #if using usb cable, need to call bot.start('/dev/ttyACM0')
 ```
 * python your code

### Wiring

* Using USB Cable for MeAuriga as shown for the Orion board
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/baseboard-usb-cable.jpg)

## Python API
 * Start
 	* **MeAuriga**()
 	* **start**()
 	
 * GPIO
 	* **digitalWrite**( pin, level )
 	* **pwmWrite**( pin, pwm )
 	* **digitalRead**( pin, **def** onResult )
 	* **analogRead**( pin, **def** onResult )
 	
 * Motion
	* DC Motor
	  * **motorRun**( port, speed )
	  * **motorMove**( leftspeed, rightspeed )
	* Servo Motor
	  * **servoRun**( port, slot, angle )
	* Encoder Motor
	  * **encoderMotorRun**( port, speed )
	  * **encoderMotorMove**( port, speed, distance, **def** onFinish )
	  * **encoderMotorMoveTo**( port, speed, position, **def** onFinish )
	* Stepper Motor
	  * **stepperMotorSetting**( port, microsteps, acceleration )
	  * **stepperMotorRun**( port, speed )
	  * **stepperMotorMove**( port, speed, distance, **def** onFinish )
	  * **stepperMotorMoveTo**( port, speed, position, **def** onFinish )
	  
 * Sensors
 	* Ultrasonic Sensor
 	  * **ultrasonicSensorRead** ( port, **def** onResult ) 
 	* LineFollow Sensor
 	  * **lineFollowerRead** ( port, **def** onResult ) 
 	* Light Sensor
 	  * **lightSensorRead** ( port, **def** onResult ) 
 	* Sound Sensor
 	  * **soundSensorRead** ( port, **def** onResult ) 
 	* Temperature Sensor
 	  * **temperatureRead** ( port, **def** onResult ) 
 	* PIR Motion Sensor
 	  * **pirMotionSensorRead** ( port, **def** onResult ) 
 	* Touch Sensor
 	  * **touchSensorRead** ( port, **def** onResult ) 
 	* LimitSwitch
 	  * **limitSwitchRead** ( port, slot, **def** onResult ) 
 	* Humiture Sensor
 	  * **humitureSensorRead** ( port, type, **def** onResult ) 
 	* Gas Sensor
 	  * **gasSensorRead** ( port, **def** onResult )
 	* Flame Sensor
 	  * **flameSensorRead** ( port, **def** onResult ) 
 	* Button
 	  * **buttonRead** ( port, **def** onResult ) 
 	* Potentiometer
 	  * **potentiometerRead** ( port, **def** onResult )
 	* Joystick
 	  * **joystickRead** ( port, axis, **def** onResult )
 	* 3-Axis Accelerometer and Gyro Sensor
 	  * **gyroRead** ( axis, **def** onResult )
 	* Compass
 	  * **compassRead** ( **def** onResult )
 	* Pressure Sensor for BMP085 and BMP180
 	  * **pressureSensorBegin** ( ) 
 	  * **pressureSensorRead** ( type, **def** onResult ) #1:Pressure #2:Temperature #3:Altitude #4:Real altitude #5:Sealevel Pressure
 	
 * Display
 	* RGB Led
 	  * **rgbLedSetColor** ( port, slot, index, r, g, b )
 	  * **rgbLedShow** ( port, slot )
 	  * **rgbLedDisplay** ( port, slot, index, r, g, b )
 	* 7-segment Display
 	  * **sevenSegmentDisplay** ( port, value )
 	* Led Matrix Display
 	  * **ledMatrixDisplayMessage** ( port, x, y, msg )
 	  * **ledMatrixDisplayRaw** ( port, buffer )
 	* Serial LCD Display
 	  * **lcdDisplay** ( string )
 	  
 * Others
 	* DSLR Shutter
	  * **shutterOn** ( port )
	  * **shutterOff** ( port )
	  * **focusOn** ( port )
	  * **focusOff** ( port )

###Learn more from Makeblock official website: www.makeblock.com
