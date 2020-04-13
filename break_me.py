def NameErr():
    newval = oldval

def AttErr():
    g = 7
    g.split()

def SynErr():
    import BadStuff

def TypeErr():
    t = "this is a string"
    u = "this is too"
    print(t/u)

try:

    #NameErr()
    #AttErr()
    SynErr()
    #TypeErr()

except NameError:
    print("Caused a Name Error")
except AttributeError:
    print("Cuased an Attribute Error")
except SyntaxError:
    print('Caused a Syntax Error')
except TypeError:
    print("Caused a Type Error")