import sys, os
import CORBA, Fortune, Fortune__POA

class CookieServer_i(Fortune__POA.CookieServer):
    def get_cookie(self):
        msg = "Testando comunicação com OmniORBpy\n"
        return msg

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = CookieServer_i()
#ativa o objeto do serve com a poa raiz
poa.activate_object(servant)
print orb.object_to_string(servant._this())

#POA ativa
poa._get_the_POAManager().activate()
orb.run()
