# Import code from src folder
import sys
sys.path.append("../src")

from meauriga import *

def onRead(v):
	print "distance:"+str(v)+" cm";

if __name__ == '__main__':
	bot = MeAuriga()
	bot.start("/dev/ttyUSB0")
	while 1:
		sleep(0.1);
		bot.ultrasonicSensorRead(9,onRead);
