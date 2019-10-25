import CORBA, Fortune

orb = CORBA.ORB_init()
print "Insira o IOR:"
testVar = raw_input()
o = orb.string_to_object(testVar)
o = o._narrow(Fortune.CookieServer)
print o.get_cookie()
