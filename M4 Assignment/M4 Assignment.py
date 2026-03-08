#Matthew Williams
#CSCI3025


FREEZING_POINT_F = 32 #global variable usable anywhere

def cToF(c):
  '''
    Returns a conversion of celsius into fahrenheit

        Parameters:
            c: temperature in celsius                 

        Returns:
             string from weatherAdvice()
  '''
  try:
    f = (c * 9/5) + FREEZING_POINT_F #f is a local variable, as it only exists in this function
    return f
  except TypeError: #no longer triggers
    print("Invalid input")

def fToC(f):
  '''
    Returns a conversion of fahrenheit into celsius

        Parameters:
            f: temperature in fahrenheit                 

        Returns:
             string from weatherAdvice()
  '''
  try:
     c = (f - FREEZING_POINT_F) * 5/9  #c is a local variable, as it only exists in this function
     return c
  except TypeError: #no longer triggers
     print("Invalid input")

def weatherAdvice(temp, unit='f'):  
  '''
    Returns a string 

        Parameters:
            temp: temperature
            unit: celcius or fahrenheit                 

        Returns:
             string 
  '''
  unit = unit.upper()
  
  if unit == 'F':    
      des = "No advisory in effect."
      if temp >= 105:
        des = "Extreme heat warning!"
      elif 94 < temp < 105:
        des = "Heat advisory!"
      elif 32 < temp < 37:
        des = "Frost advisory!"
      elif temp <= 32:
        des = "Extreme cold warning!"
  
  if unit == 'C':    
      des = "No advisory in effect."
      if temp >= fToC(105):
        des = "Extreme heat warning!"
      elif fToC(94) < temp < fToC(105):
        des = "Heat advisory!"
      elif fToC(32) < temp < fToC(37):
        des = "Frost advisory!"
      elif temp <= fToC(32):
        des = "Extreme cold warning!"
  temp = round(temp, 1)
  return f"{temp}°{unit} {des}"

def validateData(temp, unit):
    '''
        checks temp to validate it is a valur that isn't below absolute zero

        Parameters:
            temp: temperature
            unit: temperature unit         

        Returns:
             true if data is valid
  '''
  
    if temp <= -273.15 and unit.upper() == 'C':
        raise ValueError       
    elif temp <= -459.67 and unit.upper() == 'F':
        raise ValueError        
    else:
       return True


#run program 
print("Temperature conversion app.Type 'exit' at anytime to exit\n")
validTemp = False
while not validTemp:
    try:    
        unit = input("Is your temperature in C or F?\n")      
        if unit == 'exit':
            print("exiting program")
            exit()

        temp = input("Enter Temperature: \n")
        if temp == 'exit':
            print("exiting program")
            exit()             
        temp = float(temp) #float() invalidated exception handling in fToC() and cToF()
       
        validTemp = validateData(temp, unit)
        
        if unit.upper() == 'C':
           print(weatherAdvice(cToF(temp), "f"))
        elif unit.upper() == 'F':
           print(weatherAdvice(fToC(temp), "c"))
           
    except ValueError:
       print("Invalid information, please try again.")