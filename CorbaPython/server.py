import sys, os
import CORBA, Fortune, Fortune__POA

class CookieServer_i(Fortune__POA.CookieServer):
    def get_cookie(self):
        msg = "Hello World\n"
        return msg

#inicia o orb do corba
orb = CORBA.ORB_init(sys.argv)
#POA raiz servidor -> cliente
poa = orb.resolve_initial_references("RootPOA")

#instancia o server
servant = CookieServer_i()
#ativa o objeto do serve com a poa raiz
poa.activate_object(servant)

#print na tela
print orb.object_to_string(servant._this())

#Referencia a POA ativa
poa._get_the_POAManager().activate()
orb.run()
