#!/usr/bin/env python
from sys import argv
import time
filename = "/sys/class/leds/smc::kbd_backlight/brightness"
value = argv[1]
mode = str(argv[2])
#interval = argv[3]

def print_usage():
	print("\n\n========Usage=========")
	print("./script.py [value] [static/pulse] [interval]")


def main():
	
	if mode == "static":
		print "Running in Static mode..\n\n"
		targetfile = open(filename,'w')
		print "Setting Brightness for macbook keyboard: ", value
		try:
			targetfile.write(value)
		except e:
			print(e)

		for i in range(5):
			print (".")
			time.sleep(0.05)

		targetfile.close()
		print("Bye")

	elif mode == "pulse":
		print "Pulsing...\n\n"
		i=20
		reached_top = 0
		while 1:
			targetfile = open(filename,'w')
			try:
				targetfile.write(str(i))
				targetfile.close()
			except :
				break
			time.sleep(0.05);
			# targetfile.close()
			if (reached_top != 1):
				if(i<=(int)(str(value))):
					i+=1
				else:
					reached_top = 1
			else:
				reached_top = 1
				i -=1
				if (i==20):
					reached_top = 0

		targetfile.close()
	else:
		print_usage()

if __name__ == "__main__":
	main()
