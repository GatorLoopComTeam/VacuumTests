import picamera
import time

camera = picamera.PiCamera()
camera.vflip = True
camera.start_preview()

i = 0
while True:
	camera.capture('images/image' + str(i) + '.jpg')
	i = i + 1
	print(str(i) + " pictures taken")
	time.sleep(1)

camera.stop_preview()
