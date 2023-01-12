#Sets a default value for all motors
#Default value is the mid point at 127mm
global A1, A2, A3, A4, B1, B2, B3, B4
A1, A2, A3, A4, B1, B2, B3, B4 = 127, 127, 127, 127, 127, 127, 127, 127

def query():
  query = str(input("What would you like to do?P "))
  query = query.lower()
  
  if (query == "move motor"):
    motorControl()
  elif (query == "print motor positions"):
    print(f'A1: {A1}\nA2: {A2}\nA3: {A3}\nA4: {A4}\nB1: {B1}\nB2: {B2}\nB3: {B3}\nB4: {B4}')
  else:
    print("command not recognized")

def motorControl():
  global A1, A2, A3, A4, B1, B2, B3, B4
  #queries to select arm, motor, and distance to move
  motorFinal = A1
  arm = str(input("Select an arm to access(A,B): "))
  motor = str(input("Select a motor to access(1,2,3,4): "))
  selectedMotor = str(f'{arm}{motor}')
  distance = float(input(f'Motor {selectedMotor} is at {motorFinal}mm, how far would you like to move it?(in increments of 25.4mm): '))
  distance = distance*25.4
  
  #sets the distance to move in increments of 25.4 mm



  #checks which arm and motor is selected and moves motor to the selected position
  if arm == "A":
    if motor == "1":
      motorFinal = A1
      if (A1 - distance >= 0 and A1-distance <= 254):
        A1 = (A1 - distance)
        print(f'Motor {selectedMotor} is at {A1}')
      elif (A1 - distance < 0):
        A1 = 0
        print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {A1}')
      elif (A1 - distance > 254):
          A1 = 254
          print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {A1}')
    elif motor == "2":
      motorFinal = A2
      if (A2 - distance >= 0 and A2-distance <= 254):
        A2 = (A2 - distance)
        print(f'Motor {selectedMotor} is at {A2}')
      elif (A2 - distance < 0):
        A2 = 0
        print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {A2}')
      elif (A2 - distance > 254):
        A2 = 254
        print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {A2}')
    elif motor == "3":
      motorFinal = A3
      if (A3 - distance >= 0 and A3-distance <= 254):
        A3 = (A3 - distance)
        print(f'Motor {selectedMotor} is at {A3}')
      elif (A3 - distance < 0):
        A3 = 0
        print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {A3}')
      elif (A3 - distance > 254):
        A3 = 254
        print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {A3}')
    elif motor == "4":
      motorFinal = A4
      if (A4 - distance >= 0 and A4-distance <= 254):
        A4 = (A4 - distance)
        print(f'Motor {selectedMotor} is at {A4}')
      elif (A4 - distance < 0):
        A4 = 0
        print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {A4}')
      elif (A4 - distance > 254):
        A4 = 254
        print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {A4}')
    else:
      motorFinal = "N/A"
  elif arm == "B":
    if motor == "1":
        motorFinal = B1
        if (B1 - distance >= 0 and B1-distance <= 254):
          B1 = (B1 - distance)
          print(f'Motor {selectedMotor} is at {B1}')
        elif (B1 - distance < 0):
          B1 = 0
          print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {B1}')
        elif (B1 - distance > 254):
          B1 = 254
          print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {B1}')
    elif motor == "2":
        motorFinal = B2
        if (B2 - distance >= 0 and B2-distance <= 254):
          B2 = (B2 - distance)
          print(f'Motor {selectedMotor} is at {B2}')
        elif (B2 - distance < 0):
          B2 = 0
          print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {B2}')
        elif (B2 - distance > 254):
          B2 = 254
          print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {B2}')
    elif motor == "3":
        motorFinal = B3
        if (B3 - distance >= 0 and B3-distance <= 254):
          B3 = (B3 - distance)
          print(f'Motor {selectedMotor} is at {B3}')
        elif (B3 - distance < 0):
          B3 = 0
          print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {B3}')
        elif (B3 - distance > 254):
          B3 = 254
          print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {B3}')
    elif motor == "4":
        motorFinal = B4
        if (B4 - distance >= 0 and B4-distance <= 254):
          B4 = (B4 - distance)
          print(f'Motor {selectedMotor} is at {B4}')
        elif (B4 - distance < 0):
          B4 = 0
          print(f'Value limited to floor of 0. Motor {selectedMotor} is now at {B4}')
        elif (B4 - distance > 254):
          B4 = 254
          print(f'Value limited to ceiling of 254. Motor {selectedMotor} is now at {B4}')
    else:
        motorFinal = "N/A"
  else:
      motorFinal = "N/A"

while True:
  query()

