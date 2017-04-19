# Import code from src folder
import sys
sys.path.append("../src")

from meauriga import *

if __name__ == '__main__':
	bot = MeAuriga()
	bot.start("/dev/ttyUSB0")
	j = 0.0;
	f = 0.0;
	k = 0.0;
	port = 0;
	slot = 1;
	while True:
		for i in range(16):
			red = 32*(1.0+math.sin(((i/2.0)+(j/4.0))));
			green = 32*(1.0+math.sin(((i/1.0)+(f/9.0)+2.1)));
			blue = 32*(1.0+math.sin(((i/3.0)+(k/14.0)+4.2)));
			bot.rgbledDisplay(port,slot,i,red,green,blue);
  		j += random.random();
  		f += random.random();
  		k += random.random();
  		bot.rgbledShow(port,slot);
		sleep(0.02);
