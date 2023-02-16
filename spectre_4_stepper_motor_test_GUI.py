import tkinter as tk
from tkinter import *
import tkinter.font as tkfont
import serial
import time
import serial.tools.list_ports

# function to grab the serial port that the arduino is connected to
def get_ports():
    ports = serial.tools.list_ports.comports() 
    return ports

def findArduino(portsFound):
    commPort = 'None'
    numConnection = len(portsFound)
    for i in range(0,numConnection):
        port = portsFound[i]
        strPort = str(port)
        if 'USB Serial Port' in strPort: #'USB Serial Port' is set for the AZ Delivery Arduino boards and may be different for different makes
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
    return commPort                    
foundPorts = get_ports()        
connectPort = findArduino(foundPorts)

if connectPort != 'None':
    ser = serial.Serial(connectPort,baudrate = 9600, timeout=1) ## IF THERE ARE CONNECTION ISSUES COPY THIS LINE TO THE FIRST INDENT AND CHANGE
    print('Connected to ' + connectPort)						## connectPort TO THE NAME OF THE PORT THAT THE ARDUINO IS CONNECTED TO eg.'COM6'
else:
    print('Connection Issue!')
print('DONE')



#parameters of the main window to load
window= tk.Tk()
window.geometry("540x720")
window.configure(bg = "#A7A7A7")
window.title("Spectre Test Device")
window.resizable(False,False)

scale_label_direction = {0: "CCW",1: "CW",}
scale_label_power = {0: "OFF",1: "ON",}

#direction label functions for slider text
def scale_labels_direction1A(value):
	m1A_direction.config(label=scale_label_direction[int(value)])

def scale_labels_direction1B(value):
	m1B_direction.config(label=scale_label_direction[int(value)])

def scale_labels_direction2A(value):
	m2A_direction.config(label=scale_label_direction[int(value)])

def scale_labels_direction2B(value):
	m2B_direction.config(label=scale_label_direction[int(value)])

#power label functions for slider text
def scale_labels_power1A(value):
	m1A_power.config(label=scale_label_power[int(value)])

def scale_labels_power1B(value):	
	m1B_power.config(label=scale_label_power[int(value)])

def scale_labels_power2A(value):	
	m2A_power.config(label=scale_label_power[int(value)])

def scale_labels_power2B(value):	
	m2B_power.config(label=scale_label_power[int(value)])

#start button function which takes data from all inputs and transmits to the serial
def serial_data_send():
	#power status data
	m1Apowersend = str(m1A_power.get())
	m1Bpowersend = str(m1B_power.get())
	m2Apowersend = str(m2A_power.get())
	m2Bpowersend = str(m2B_power.get())
	#direction status data
	m1Adirectionsend = str(m1A_direction.get())
	m1Bdirectionsend = str(m1B_direction.get())
	m2Adirectionsend = str(m2A_direction.get())
	m2Bdirectionsend = str(m2B_direction.get())
	#speed status data
	m1Aspeedsend = str(motor1A_speed_entry.get())
	m1Bspeedsend = str(motor1B_speed_entry.get())
	m2Aspeedsend = str(motor2A_speed_entry.get())
	m2Bspeedsend = str(motor2B_speed_entry.get())
	#motor movement data
	m1Amovements = str(movements_entry1A.get())
	m1Bmovements = str(movements_entry1B.get())
	m2Amovements = str(movements_entry2A.get())
	m2Bmovements = str(movements_entry2B.get())
	#MUST HAVE <> AS END MARKERS TO BE READ PROPERLY BY THE ARDUINO
	data = ('<' +
	 m1Apowersend + m1Bpowersend + m2Apowersend + m2Bpowersend + 
	 m1Adirectionsend + m1Bdirectionsend + m2Adirectionsend + m2Bdirectionsend + 
	 m1Aspeedsend[0] + m1Aspeedsend[1] + m1Aspeedsend[2]+
	 m1Bspeedsend[0] + m1Bspeedsend[1] + m1Bspeedsend[2]+ 
	 m2Aspeedsend[0] + m2Aspeedsend[1] + m2Aspeedsend[2]+ 
	 m2Bspeedsend[0] + m2Bspeedsend[1] + m2Bspeedsend[2]+
	 m1Amovements[0] + m1Amovements[1] + m1Amovements[2] + m1Amovements[3] + m1Amovements[4] + 
	 m1Bmovements[0] + m1Bmovements[1] + m1Bmovements[2] + m1Bmovements[3] + m1Bmovements[4] +
	 m2Amovements[0] + m2Amovements[1] + m2Amovements[2] + m2Amovements[3] + m2Amovements[4] +
	 m2Bmovements[0] + m2Bmovements[1] + m2Bmovements[2] + m2Bmovements[3] + m2Bmovements[4] + 
	 '0' +
	 '>') 
	ser.write(bytes(data, 'utf-8'))
	time.sleep(1)
	print(data)
	print(len(data))

def emergency_stop():
	#power status data
	m1Apowersend = str(m1A_power.get())
	m1Bpowersend = str(m1B_power.get())
	m2Apowersend = str(m2A_power.get())
	m2Bpowersend = str(m2B_power.get())
	#direction status data
	m1Adirectionsend = str(m1A_direction.get())
	m1Bdirectionsend = str(m1B_direction.get())
	m2Adirectionsend = str(m2A_direction.get())
	m2Bdirectionsend = str(m2B_direction.get())
	#speed status data
	m1Aspeedsend = str(motor1A_speed_entry.get())
	m1Bspeedsend = str(motor1B_speed_entry.get())
	m2Aspeedsend = str(motor2A_speed_entry.get())
	m2Bspeedsend = str(motor2B_speed_entry.get())
	#motor movement data
	m1Amovements = str(movements_entry1A.get())
	m1Bmovements = str(movements_entry1B.get())
	m2Amovements = str(movements_entry2A.get())
	m2Bmovements = str(movements_entry2B.get())
	#MUST HAVE <> AS END MARKERS TO BE READ PROPERLY BY THE ARDUINO
	data = ('<' +
	 m1Apowersend + m1Bpowersend + m2Apowersend + m2Bpowersend + 
	 m1Adirectionsend + m1Bdirectionsend + m2Adirectionsend + m2Bdirectionsend + 
	 m1Aspeedsend[0] + m1Aspeedsend[1] + m1Aspeedsend[2]+
	 m1Bspeedsend[0] + m1Bspeedsend[1] + m1Bspeedsend[2]+ 
	 m2Aspeedsend[0] + m2Aspeedsend[1] + m2Aspeedsend[2]+ 
	 m2Bspeedsend[0] + m2Bspeedsend[1] + m2Bspeedsend[2]+
	 m1Amovements[0] + m1Amovements[1] + m1Amovements[2] + m1Amovements[3] + m1Amovements[4] + 
	 m1Bmovements[0] + m1Bmovements[1] + m1Bmovements[2] + m1Bmovements[3] + m1Bmovements[4] +
	 m2Amovements[0] + m2Amovements[1] + m2Amovements[2] + m2Amovements[3] + m2Amovements[4] +
	 m2Bmovements[0] + m2Bmovements[1] + m2Bmovements[2] + m2Bmovements[3] + m2Bmovements[4] + 
	 '1' +
	 '>') 
	ser.write(bytes(data, 'utf-8'))
	time.sleep(1)
	print(data)
	print(len(data))

#button to send data to serial
data_send_button = tk.Button(
	text="Run",
	bg='#D2F6D0',
	fg='#013A65',
	font=("arial", 20),
	command=serial_data_send,
	width = 12,
	height = 2,
	)

emergency_stop_button = tk.Button(
	text="STOP",
	bg='#F14C4C',
	fg='white',
	font=("arial", 20),
	command=emergency_stop,
	width = 12,
	height = 2,
	)


#sliders for power selection
m1A_power = tk.Scale(
	window,
	from_=min(scale_label_power), 
	to = max(scale_label_power),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_power1A,
	sliderlength = 100,
	length  = 130,
	label = False
	)

m1B_power = tk.Scale(
	window,
	from_=min(scale_label_power), 
	to = max(scale_label_power),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_power1B,
	sliderlength = 100,
	length  = 130,
	label = False
	)

m2A_power = tk.Scale(
	window,
	from_=min(scale_label_power), 
	to = max(scale_label_power),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_power2A,
	sliderlength = 100,
	length  = 130,
	label = False
	)

m2B_power = tk.Scale(
	window,
	from_=min(scale_label_power), 
	to = max(scale_label_power),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_power2B,
	sliderlength = 100,
	length  = 130,
	label = False
	)

#sliders for direction
m1A_direction = tk.Scale(
	window,
	from_=min(scale_label_direction), 
	to = max(scale_label_direction),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_direction1A,
	sliderlength = 100,
	length  = 130,
	label = False
	)

m1B_direction = tk.Scale(
	window,
	from_=min(scale_label_direction), 
	to = max(scale_label_direction),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_direction1B,
	sliderlength = 100,
	length  = 130,
	label = False
	)

m2A_direction = tk.Scale(
	window,
	from_=min(scale_label_direction), 
	to = max(scale_label_direction),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_direction2A,
	sliderlength = 100,
	length  = 130,
	label = False
	)

m2B_direction = tk.Scale(
	window,
	from_=min(scale_label_direction), 
	to = max(scale_label_direction),
	orient=tk.HORIZONTAL,
	showvalue = False,
	command = scale_labels_direction2B,
	sliderlength = 100,
	length  = 130,
	label = False
	)


#entry boxes for number of movements of each motor
#initial box to contain all the entry boxes for each motor
movement_counter = tk.Canvas(
	window,
	height=350,
	width=200)

#title for the movements counter
movement_title1 = tk.Label(
	window,
	text= "Motor Movements"
	)

movement_title1.config(font=("arial", 12))

movement_counter.create_window(
	100,
	20, 
	window = movement_title1
	)

#motor 1A movements counter and label
#motor 1A label
movements_title1A = tk.Label(
	window,
	text= "Motor 1A"
	)

movements_title1A.config(font=("arial", 10))

movement_counter.create_window(
	50,
	50, 
	window = movements_title1A
	)

#motor 1A entry
movements_entry1A = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	50,
	75, 
	window=movements_entry1A,
	width=55,
	height=20)

#autofill for 1A entry
movements_entry1A.insert(0,'00020')

#motor 1B movements counter and label
#motor 1B label
movements_title1B = tk.Label(
	window,
	text= "Motor 1B"
	)

movements_title1B.config(font=("arial", 10))

movement_counter.create_window(
	50,
	100, 
	window = movements_title1B
	)

#motor 1B entry
movements_entry1B = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	50,
	125, 
	window=movements_entry1B,
	width=55,
	height=20)

#autofill for 1B entry
movements_entry1B.insert(0,'00020')

#motor 2A movements counter and label
#motor 2A label
movements_title2A = tk.Label(
	window,
	text= "Motor 2A"
	)

movements_title2A.config(font=("arial", 10))

movement_counter.create_window(
	150,
	50, 
	window = movements_title2A
	)

#motor 2A entry
movements_entry2A = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	150,
	75, 
	window=movements_entry2A,
	width=55,
	height=20)

#autofill for 2A entry
movements_entry2A.insert(0,'02000')

#motor 2B movements counter and label
#motor 2B label
movements_title2B = tk.Label(
	window,
	text= "Motor 2B"
	)

movements_title2B.config(font=("arial", 10))

movement_counter.create_window(
	150,
	100, 
	window = movements_title2B
	)

#motor 2B entry
movements_entry2B = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	150,
	125, 
	window=movements_entry2B,
	width=55,
	height=20)

#autofill for 2B entry
movements_entry2B.insert(0,'02000')

#motor 1A speed label and entry box
#motor 1A speed label
motor1A_speed_title = tk.Label(
	window,
	text= "Motor 1A Speed (ms)"
	)

motor1A_speed_title.config(font=("arial", 10))

movement_counter.create_window(
	70,
	160, 
	window = motor1A_speed_title
	)

#motor 1A speed entry
motor1A_speed_entry = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	40,
	185, 
	window=motor1A_speed_entry,
	width=35,
	height=20)

#autofill for motor 1A speed entry
motor1A_speed_entry.insert(0,'200')

#motor_1B speed label and entry box
#motor_1B speed label
motor_1B_speed_title = tk.Label(
	window,
	text= "Motor 1B Speed (ms)"
	)

motor_1B_speed_title.config(font=("arial", 10))

movement_counter.create_window(
	70,
	205, 
	window = motor_1B_speed_title
	)

#motor_1B speed entry
motor1B_speed_entry = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	40,
	230, 
	window=motor1B_speed_entry,
	width=35,
	height=20)

#autofill for motor_1B speed entry
motor1B_speed_entry.insert(0,'300')

#motor 2A speed label and entry box
#motor 2A speed label
motor2A_speed_title = tk.Label(
	window,
	text= "Motor 2A Speed (ms)"
	)

motor2A_speed_title.config(font=("arial", 10))

movement_counter.create_window(
	70,
	250, 
	window = motor2A_speed_title
	)

#motor 2A speed entry
motor2A_speed_entry = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	40,
	275, 
	window=motor2A_speed_entry,
	width=35,
	height=20)

#autofill for motor 2A speed entry
motor2A_speed_entry.insert(0,'000')

#motor 2B speed label and entry box
#motor 2B speed label
motor2B_speed_title = tk.Label(
	window,
	text= "Motor 2B Speed (ms)"
	)

motor2B_speed_title.config(font=("arial", 10))

movement_counter.create_window(
	70,
	295, 
	window = motor2B_speed_title
	)

#motor 2B speed entry
motor2B_speed_entry = tk.Entry(movement_counter, font = 20)

movement_counter.create_window(
	40,
	320, 
	window=motor2B_speed_entry,
	width=35,
	height=20)

#autofill for motor 2B speed entry
motor2B_speed_entry.insert(0,'000')

#Labels for the motor control switch groups
#motor 1a labels
motor1A_main_label = tk.Label(
	window,
	text= "Motor 1A",
	font = ("arial", 14),
	bg = "#A7A7A7",
	)

motor1A_power_label = tk.Label(
	window,
	text= "Motor 1A Power",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)

motor1A_direction_label = tk.Label(
	window,
	text= "Motor 1A Direction",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)

#motor 1B labels
motor1B_main_label = tk.Label(
	window,
	text= "Motor 1B",
	font = ("arial", 14),
	bg = "#A7A7A7",
	)

motor1B_power_label = tk.Label(
	window,
	text= "Motor 1B Power",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)

motor1B_direction_label = tk.Label(
	window,
	text= "Motor 1B Direction",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)

#motor 2a labels
motor2A_main_label = tk.Label(
	window,
	text= "Motor 2A",
	font = ("arial", 14),
	bg = "#A7A7A7",
	)

motor2A_power_label = tk.Label(
	window,
	text= "Motor 2A Power",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)

motor2A_direction_label = tk.Label(
	window,
	text= "Motor 2A Direction",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)

#motor 2b labels
motor2B_main_label = tk.Label(
	window,
	text= "Motor 2B",
	font = ("arial", 14),
	bg = "#A7A7A7",
	)

motor2B_power_label = tk.Label(
	window,
	text= "Motor 2B Power",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)

motor2B_direction_label = tk.Label(
	window,
	text= "Motor 2B Direction",
	font = ("arial", 8),
	bg = "#A7A7A7",
	)


#power slider placement
m1A_power.place(x=10, y=75)
m1B_power.place(x=10, y=250)
m2A_power.place(x=10, y=425)
m2B_power.place(x=10, y=600)

#direction slider placement
m1A_direction.place(x=150, y=75)
m1B_direction.place(x=150, y=250)
m2A_direction.place(x=150, y=425)
m2B_direction.place(x=150, y=600)

#label placement for motor groups
#motor 1a labels
motor1A_main_label.place(x=10, y=25)
motor1A_power_label.place(x=10, y=55)
motor1A_direction_label.place(x=150, y=55)

#motor 1b labels
motor1B_main_label.place(x=10, y=200)
motor1B_power_label.place(x=10, y=230)
motor1B_direction_label.place(x=150, y=230)

#motor 2a labels
motor2A_main_label.place(x=10, y=375)
motor2A_power_label.place(x=10, y=405)
motor2A_direction_label.place(x=150, y=405)

#motor 2B labels
motor2B_main_label.place(x=10, y=550)
motor2B_power_label.place(x=10, y=580)
motor2B_direction_label.place(x=150, y=580)

#placement of the step counter box
movement_counter.place(x=325, y=55)

#placement of the data send button
data_send_button.place(x=325, y=500)

#placement of the emergency stop button
emergency_stop_button.place(x=325, y=600)

window.mainloop()