#
# This file is part of libgreat
#

"""
Module containing the definitions necessary to communicate with libgreat
devices via WinUSB.
"""

from __future__ import absolute_import
from future import utils as future_utils

import time
import errno
import struct
import platform

from ..comms import CommsBackend
from ..errors import DeviceNotFoundError


class WinUSBCommsBackend(CommsBackend):
    """
    Class representing an abstract communications channel used to connect with a libgreat board.
    """

    def __init__(self, **device_identifiers):
        """
        Instanciates a new comms connection to a libgreat device; by default connects
        to the first available board.
        """
        try:
            self.device = winusb.init_winusb_device(device_identifiers['idVendor'], device_identifiers['idProduct'])
        except:
            pass
