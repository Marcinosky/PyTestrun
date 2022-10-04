from CollisUL.CollisULCardServer import collisULCardServer
from LatteLiteEngine_BaseClass import RemoveChip, atClient_init

class ExceptionForced(Exception):
    Collis = collisULCardServer
    #RemoveChip(atClient)
    Collis.handleCollisStopProbe()
    pass
