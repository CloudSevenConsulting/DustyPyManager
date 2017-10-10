"""
The Install tests here are simply to check that your installation worked,
these unit test DO NOT rely on the the DustyPyManager package itself.
"""

import unittest

from SmartMeshSDK.IpMgrConnectorSerial import IpMgrConnectorSerial
from SmartMeshSDK.ApiException import ConnectionError, CommandTimeoutError

from DustyPyManager import configure

def main():
    unittest.main()

class TestWsnInstall(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super(TestWsnInstall, self).__init__(*args, **kwargs)

        self.conn_conf = configure.get_config_resource('wsn', 'connection.ini')

    def test_TU_NM_WSNHandshake_APIConnSerialNoMux_Op(self):
        """
        Test that the installation of the NM works without Serial Mux
        """

        DC2274AA_Port_CLI = int(self.conn_conf['default']['port_cli'])

        connector = IpMgrConnectorSerial.IpMgrConnectorSerial()

        try:
            connector.connect({
                                'port': DC2274AA_Port_CLI,
                            })
        except ConnectionError as err:
            print err
            self.assertTrue(False)#Failed

        try:
            print connector.dn_getNetworkInfo()
        except (ConnectionError,CommandTimeoutError) as err:
            print "Could not send data, err={0}".format(err)
            self.assertTrue(False)#Failed

if __name__ == '__main__':
    main()