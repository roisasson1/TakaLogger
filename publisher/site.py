from enum import Enum

from pymodbus.client import ModbusTcpClient


class PLCVar:
    regType = Enum('M', 'Q', 'I', 'VW', 'AI', 'AQ', 'Modbus_Int', 'Modbus_Bit')
    address = 0
    bit = 0


class PLC:
    client = ModbusTcpClient()
    comPort = ""
    baudRate = 0
    type = ""
    ip = ""
    port = 0
    interval = 50
    name = ""


class Register:
    PLC = ""
    var = PLCVar()
    name = ""
    value = ""
    multi_state = {"num": 0, "name": "bla"}
    normal = 0
    notified = False
    validated = 0


class RegisterGroup:
    registers = []
    trigger = Register()
    name = ""


class Site:
    name = ""
    autoReg = Register()
    emergency_Reg = Register()
    alive_Interval = 20
    alive_Enable = True
    validation_Count = 1
    alive_Recipient = "parkomat.monitor@gmail.com"
    timer_Interval = 5000
    email_Addresses = []
    user_num_reg = Register()
    site_code = ""
    site_number = ""
    debug_trigger = Register()
    debug_regs = []
    debug_interval = 0

