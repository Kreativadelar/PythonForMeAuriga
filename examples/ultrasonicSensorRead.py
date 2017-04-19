from meauriga import *

def onRead(v):
	print "distance:"+str(v)+" cm";

if __name__ == '__main__':
	bot = MeAuriga("/dev/ttyUSB0")
	bot.start()
	while 1:
		sleep(0.1);
		bot.ultrasonicSensorRead(9,onRead);