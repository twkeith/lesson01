def sleep_in(weekday, vacation):
  if vacation:
    return True
  else:
    return not weekday

print("Sleep In========")
print(sleep_in(True,True))
print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
  return True
  else:
  return False

print("Monkeys==========")
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

def sum_double(a, b):
  if a == b:
  print(4*a)
  else:
  print(a + b)

print("Double")
sum_double(1, 2)
sum_double(3, 2)
sum_double(2, 2)

def diff21(n):
if n > 21:
print(2*(n-21))
else:
print(21-n)

print("21 Difference")
diff21(19)
diff21(10)
diff21(21)

def parrot_trouble(talking, hour):
  if hour > 20 or hour < 7:
  print(talking)
  else:
  print(False)


print("parrot")
parrot_trouble(True, 6)
parrot_trouble(True, 7)
parrot_trouble(False, 6)

def makes10(a, b):
  if a + b == 10 or a == 10 or b == 10:
    print(True)
  else:
    print(False)

print("Tens")
makes10(9, 10)
makes10(9, 9)
makes10(1, 9)

def near_hundred(n):
  if abs(n-100) <= 10 or abs(n-200) <= 10:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if a*b < 0:
      return True
    else:
      return False

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  howlong = len(str)
  if howlong > 1:
    return str[howlong-1] + str[1:howlong-1] + str[0]
  else:
    return str

def front3(str):
  if len(str) < 3:
    return 3*str
  else:
    return 3*str[:3]

def string_times(str, n):
  return n*str

def front_times(str, n):
  if len(str) < 3:
    return n*str
  else:
    return n*str[:3]

def string_bits(str):
  howlong = len(str)
  newstring = ""
  i = 0
  while (i < howlong):
    newstring = newstring + str[i]
    i = i + 2
  return newstring

def string_splosion(str):
  howlong = len(str)
  newstring = ""
  for i in range(howlong+1):
    newstring = newstring + str[:i]
  return newstring

#doesn't work yet
def last2(str):
  howlong = len(str)
  endtwo = str[2:]
  count = 0
  for i in range(howlong-2):
    if str[i:i+2] == endtwo:
      count = count + 1
  return count
