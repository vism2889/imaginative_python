# Author: Morgan Visnesky
# Date: November 10 2019
# Application: Nintendo Switch Game Controller Listener

# To get started use OS bluetooth menu to connect controller.
# Reads events from a bluetooth game controller.
# I used a switch for this and it worked just fine.
# This was made for raspberry pi but should work on
# any linux machine with bluetooth.


from evdev import InputDevice, categorize, ecodes
import socket
UDP_IP_ADDRESS = "192.168.1.153"
UDP_PORT_NO = 5500


gamepad = InputDevice('/dev/input/event0')

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# button codes
lBtn = 308
zlBtn = 310
rBtn = 309
zrBtn = 311
xBtn = 307
yBtn = 306
aBtn = 305
bBtn = 304

# home buttons
minusBtn = 312
plusBtn = 313
homeBtn = 316
squareBtn = 317

# control pad
arrowUp_down = 17
arrowLeft_right = 16

# LR joysticks
up_down_LJ = 1
left_right_LJ = 0
up_down_RJ = 4
left_right_RJ = 3


print(gamepad)
message = ''
for event in gamepad.read_loop():
	if event.type == ecodes.EV_KEY:
		# EV_KEY events are button and trigger events
		if event.value == 1:
			if event.code == lBtn:
				print('L')
				message = 'L'
			elif event.code == zlBtn:
				print('ZL')
				message = 'ZL'
			elif event.code == rBtn:
				print('R')
				message = 'R'
			elif event.code == zrBtn:
				print('ZR')
				message = 'ZR'
			elif event.code == aBtn:
				print('A')
				message = 'A'
			elif event.code == bBtn:
				print('B')
				message = 'B'
			elif event.code == xBtn:
				print('X')
				message = 'X'
			elif event.code == yBtn:
				print('Y')
				message = 'Y'
			elif event.code == minusBtn:
				print('minus')
				message = 'minus'
			elif event.code == plusBtn:
				print('plus')
				message = 'plus'
			elif event.code == homeBtn:
				print('home')
				message = 'home'
			elif event.code == squareBtn:
				print('square')
				message = 'square'
			clientSock.sendto(message, (UDP_IP_ADDRESS,UDP_PORT_NO))
	elif event.type == ecodes.EV_ABS:
		# EV_ABS events are from joysticks
		if event.code == arrowUp_down:
			if event.value = 1:
				print('up arrow')
				message = 'up arrow'
			elif event.value = -1:
				print ('down arrow')
				message = 'down arrow'
		elif event.code == arrowLeft_right:
			if event.value = 1:
				print('right arrow')
				message = 'right arrow'
			elif event.value = -1:
				print ('left arrow')
				message = 'left arrow'
		elif event.code == 1:
			print ('LEFT JOYSTICK Y: ' + event.value)
			message = ('LEFT JOYSTICK Y: ' + event.value)
		elif event.code == 0:
			print ('LEFT JOYSTICK X: ' + event.value)
			message = ('LEFT JOYSTICK X: ' + event.value)
		elif event.code == 4:
			print ('RIGHT JOYSTICK Y: ' + event.value)
			message = ('RIGHT JOYSTICK Y: ' + event.value)
		elif event.code == 3:
			print ('RIGHT JOYSTICK X: ' + event.value)
			message = ('RIGHT JOYSTICK X: ' + event.value)
		clientSock.sendto(message, (UDP_IP_ADDRESS,UDP_PORT_NO))
