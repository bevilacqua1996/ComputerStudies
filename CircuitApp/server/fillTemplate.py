import os

dir_path = os.path.dirname(os.path.realpath(__name__))

CRcircuitTemplatePath=dir_path + "/circuitSimulations/circuitTemplates/circuitCR.net"
CRcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitCR.net"

RCcircuitTemplatePath=dir_path + "/circuitSimulations/circuitTemplates/circuitRC.net"
RCcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitRC.net"

LRcircuitTemplatePath=dir_path + "/circuitSimulations/circuitTemplates/circuitLR.net"
LRcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitLR.net"

RLcircuitTemplatePath=dir_path + "/circuitSimulations/circuitTemplates/circuitRL.net"
RLcircuitResultPath=dir_path + "/circuitSimulations/circuitResults/circuitRL.net"

class CRcircuit:
    def __init__(self, peakVoltage, frequency, resistor, capacitor):
        #input file
        fin = open(CRcircuitTemplatePath, "rt")
        #output file to write the result to
        fout = open(CRcircuitResultPath, "wt")
        #for each line in the input file
        for line in fin:
            #read replace the string and write to output file
            if '{capacitorValue}' in line:
                fout.write(line.replace('{capacitorValue}', capacitor))
            elif '{resistorValue}' in line:
                fout.write(line.replace('{resistorValue}', resistor))
            elif '{voltageValue}' in line:
                fout.write(line.replace('{voltageValue}', peakVoltage).replace('{frequencyValue}', frequency))
            else:
                fout.write(line)
        #close input and output files
        fin.close()
        fout.close()

class RCcircuit:
    def __init__(self, peakVoltage, frequency, resistor, capacitor):
        #input file
        fin = open(RCcircuitTemplatePath, "rt")
        #output file to write the result to
        fout = open(RCcircuitResultPath, "wt")
        #for each line in the input file
        for line in fin:
            #read replace the string and write to output file
            if '{capacitorValue}' in line:
                fout.write(line.replace('{capacitorValue}', capacitor))
            elif '{resistorValue}' in line:
                fout.write(line.replace('{resistorValue}', resistor))
            elif '{voltageValue}' in line:
                fout.write(line.replace('{voltageValue}', peakVoltage).replace('{frequencyValue}', frequency))
            else:
                fout.write(line)
        #close input and output files
        fin.close()
        fout.close()

class LRcircuit:
    def __init__(self, peakVoltage, frequency, resistor, inductor):
        #input file
        fin = open(LRcircuitTemplatePath, "rt")
        #output file to write the result to
        fout = open(LRcircuitResultPath, "wt")
        #for each line in the input file
        for line in fin:
            #read replace the string and write to output file
            if '{inductorValue}' in line:
                fout.write(line.replace('{inductorValue}', inductor))
            elif '{resistorValue}' in line:
                fout.write(line.replace('{resistorValue}', resistor))
            elif '{voltageValue}' in line:
                fout.write(line.replace('{voltageValue}', peakVoltage).replace('{frequencyValue}', frequency))
            else:
                fout.write(line)
        #close input and output files
        fin.close()
        fout.close()

class RLcircuit:
    def __init__(self, peakVoltage, frequency, resistor, inductor):
        #input file
        fin = open(RLcircuitTemplatePath, "rt")
        #output file to write the result to
        fout = open(RLcircuitResultPath, "wt")
        #for each line in the input file
        for line in fin:
            #read replace the string and write to output file
            if '{inductorValue}' in line:
                fout.write(line.replace('{inductorValue}', inductor))
            elif '{resistorValue}' in line:
                fout.write(line.replace('{resistorValue}', resistor))
            elif '{voltageValue}' in line:
                fout.write(line.replace('{voltageValue}', peakVoltage).replace('{frequencyValue}', frequency))
            else:
                fout.write(line)
        #close input and output files
        fin.close()
        fout.close()

