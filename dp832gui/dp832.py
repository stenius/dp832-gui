import vxi11

class DP832(object):
    def __init__(self):
        pass

    def conn(self, address="10.8.10.104"):
        """Attempt to connect to instrument"""
        self.instra = vxi11.Instrument(address)

    def identify(self):
        """Return identify string which has serial number"""
        return self.instra.ask("*IDN?")

    def readings(self, channel="CH1"):
        """Read voltage/current/power from CH1/CH2/CH3"""       
        resp = self.instra.ask("MEAS:ALL? %s"%channel)
        resp = resp.split(',')
        dr = {"v":float(resp[0]), "i":float(resp[1]), "p":float(resp[2])}
        return dr

    def dis(self):
        del self.instra

    def writing(self, command=""):
        print 'not implemented'
        #self.inst.write(command)
        
if __name__ == '__main__':
    test = DP832()

    # Insert your scopes address here
    test.conn()
    
    print test.readings()
