# -*- coding: utf-8 -*-
from config import *

import re
import time
import sys
import os

from httpHelpers import *

from datetime import timedelta, datetime

startDateTime = datetime(2016, 1, 11)
endDateTime = datetime(2016, 1, 19)
dailyStartHour = 07
dailyEndHour = 17


timeStep = timedelta(minutes = 5)

currentDateTime = startDateTime


while currentDateTime < endDateTime:
	print(currentDateTime)
	try:
		if currentDateTime.hour >= dailyStartHour and currentDateTime.hour < dailyEndHour:
			url = BASEURL + STREAMID + "/" + currentDateTime.strftime("%Y/%m/%d/%H%M.jpg")
			print ("...Getting " + url)
			image = None
			try:
				image = openUrl(url, data = None, headers = None)	
			except:
				print ("......Problem getting URL")

			if image:
				outputFile = OUTPUTDIR + "/" + currentDateTime.strftime("%Y%m%d%H%M_" + STREAMID + ".jpg")
				print ("......Opening " + outputFile)
				imageFile = None
				try:
					imageFile = open(outputFile, "wb")
				except:
					print (".........Problem opening file")

				if imageFile:
					print("......Writing file")
					try:
						buf = image.read()	
						imageFile.write(buf)
						imageFile.close()
					except:
						print(".........Problem writing and closing file")
					finally:
						imageFile.close()
		else:
			print("...Not in time window")
	finally:
		print("...Moving On")
		currentDateTime = currentDateTime + timeStep
		sys.stdout.flush()

