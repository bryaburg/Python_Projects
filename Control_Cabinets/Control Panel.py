from imp import get_tag
from pylogix import PLC

PLCIP = input("PLC IP Address", )


def simple_read_tag():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        Tag_Name = input("HMI_Start")
        ret = comm.Read(Tag_Name)
    print(ret.TagName, ret.Value, ret.Status)

def simple_write_tag():
    with PLC() as comm:
        ret = comm.Write("COMMAND_FREQ", 7500)
    print(ret.TagName, ret.Value, ret.Status)
    
def get_controller_tag_list():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        tags = comm.GetTagList(False)
    for t in tags.Value:
        print(t.TagName)
        
def get_program_tag_list():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        tags = comm.GetProgramTagList('Program:MiscHMI')
    for t in tags.Value:
        print(t.TagName)

def device_discovery():
    with PLC() as comm:
        devices = comm.Discover()
    for device in devices.Value:
        print(device.IPAddress)
        print('  Product Code: ' + device.ProductName + ' ' + str(device.ProductCode))
        print('  Vendor/Device ID:' + device.Vendor + ' ' + str(device.DeviceID))
        print('  Revision/Serial:' +  device.Revision + ' '  + device.SerialNumber)
        print('')

def save_tag_list():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        tags = comm.GetTagList()

    with open('tag_list.txt', 'w') as f:
        for t in tags.Value:
            f.write('%s %d \n'.format(t.TagName, t.DataType))
            print(t.TagName)

def get_module_properties():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        prop = comm.GetModuleProperties(0)
        print(prop.Value.ProductName, prop.Value.Revision)

simple_write_tag()
