from PySpice.Spice.NgSpice.Shared import NgSpiceShared
import os

dir_path = os.path.dirname(os.path.realpath(__name__))

CRcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitCR.net"
RCcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitRC.net"
LRcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitLR.net"
RLcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitRL.net"

ngspice = NgSpiceShared.new_instance()

class CRcircuit:
    def __init__(self):
        ngspice.exec_command(CRcircuitResultPath)
        ngspice.run()
        ngspice.exec_command('plot n1 n0 v1#branch')
        ngspice.exec_command('hardcopy ' + dir_path + '/circuitSimulations/circuitResults/CRcircuit.ps n0 n1 v1#branch')
        

class RCcircuit:
    def __init__(self):
        ngspice.exec_command(RCcircuitResultPath)
        ngspice.run()
        ngspice.exec_command('plot n1 n0 v1#branch')
        ngspice.exec_command('hardcopy ' + dir_path + '/circuitSimulations/circuitResults/RCcircuit.ps n0 n1 v1#branch')

class LRcircuit:
    def __init__(self):
        ngspice.exec_command(LRcircuitResultPath)
        ngspice.run()
        ngspice.exec_command('plot n1 n0 v1#branch')
        ngspice.exec_command('hardcopy ' + dir_path + '/circuitSimulations/circuitResults/LRcircuit.ps n0 n1 v1#branch')

class RLcircuit:
    def __init__(self):
        ngspice.exec_command(RLcircuitResultPath)
        ngspice.run()
        ngspice.exec_command('plot n1 n0 v1#branch')
        ngspice.exec_command('hardcopy ' + dir_path + '/circuitSimulations/circuitResults/RLcircuit.ps n0 n1 v1#branch')