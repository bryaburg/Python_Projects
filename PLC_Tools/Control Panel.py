from pylogix import PLC
import subprocess
import platform

def ping_ip(ip_address):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', ip_address]
    return subprocess.call(command) == 0

def main_menu():
    print("\nSelect an option:")
    print("1. Read a Tag")
    print("2. Write a Tag")
    print("3. Get Controller Tag List")
    print("4. Get Program Tag List")
    print("5. Discover Devices")
    print("6. Save Tag List")
    print("7. Get Module Properties")
    print("8. Perform Network Audit")
    print("0. Exit")
    return input("Enter your choice: ")

def simple_read_tag():
    PLCIP = input("Enter PLC IP Address: ")
    if not ping_ip(PLCIP):
        print("Cannot reach the IP address. Please re-enter.")
        return
    Tag_Name = input("Enter the Tag Name to read: ")
    with PLC() as comm:
        comm.IPAddress = PLCIP
        ret = comm.Read(Tag_Name)
    print(f"Read {ret.TagName}: Value={ret.Value}, Status={ret.Status}")

def simple_write_tag():
    PLCIP = input("Enter PLC IP Address: ")
    if not ping_ip(PLCIP):
        print("Cannot reach the IP address. Please re-enter.")
        return
    Tag_Name = input("Enter the Tag Name to write to: ")
    mode = input("Select mode: (1) Write once, (2) Write continuously until a count: ")

    if mode == '1':
        Tag_Value = input(f"Enter the value to write to {Tag_Name}: ")
        with PLC() as comm:
            comm.IPAddress = PLCIP
            ret = comm.Write(Tag_Name, Tag_Value)
        print(f"Write to {ret.TagName}: Value={ret.Value}, Status={ret.Status}")

    elif mode == '2':
        count = int(input("Enter the number of times to write: "))
        for i in range(count):
            Tag_Value = input(f"Enter value #{i+1} to write to {Tag_Name}: ")
            with PLC() as comm:
                comm.IPAddress = PLCIP
                ret = comm.Write(Tag_Name, Tag_Value)
            print(f"Write #{i+1} to {ret.TagName}: Value={ret.Value}, Status={ret.Status}")

    else:
        print("Invalid mode selected.")

def get_controller_tag_list():
    PLCIP = input("Enter PLC IP Address: ")
    with PLC() as comm:
        comm.IPAddress = PLCIP
        tags = comm.GetTagList(False)
    for t in tags.Value:
        print(t.TagName)

def get_program_tag_list():
    PLCIP = input("Enter PLC IP Address: ")
    program_name = input("Enter the program name to get tags from: ")
    with PLC() as comm:
        comm.IPAddress = PLCIP
        tags = comm.GetProgramTagList(f'Program:{program_name}')
    for t in tags.Value:
        print(t.TagName, t.DataType)

def device_discovery():
    with PLC() as comm:
        devices = comm.Discover()
    if devices.Value:
        for device in devices.Value:
            print(f"IP Address: {device.IPAddress}")
            print(f"  Product Code: {device.ProductName} {device.ProductCode}")
            print(f"  Vendor/Device ID: {device.Vendor} {device.DeviceID}")
            print(f"  Revision/Serial: {device.Revision} {device.SerialNumber}")
            print('')
    else:
        print("No devices discovered on the network.")

def save_tag_list():
    PLCIP = input("Enter PLC IP Address: ")
    with PLC() as comm:
        comm.IPAddress = PLCIP
        tags = comm.GetTagList()

    with open('tag_list.txt', 'w') as f:
        for t in tags.Value:
            f.write('{} {}\n'.format(t.TagName, t.DataType))
            print(t.TagName)

def get_module_properties():
    PLCIP = input("Enter PLC IP Address: ")
    with PLC() as comm:
        comm.IPAddress = PLCIP
        prop = comm.GetModuleProperties(0)
        print(prop.Value.ProductName, prop.Value.Revision)

class audit_network:

    known_plc_types = {
        14: "ControlLogix",
        # Add other known DeviceIDs and their types here
    }

    @staticmethod
    def is_plc(device):
        return device.DeviceID in audit_network.known_plc_types

    @staticmethod
    def get_max_slots(device_type):
        if device_type == "ControlLogix":
            return 17
        return 10

    @staticmethod
    def get_devices():
        with PLC() as comm:
            return comm.Discover()

    @staticmethod
    def audit_controllers():
        devices = audit_network.get_devices()
        with open('network_audit.txt', 'w') as f:
            for d in devices.Value:
                if audit_network.is_plc(d):
                    device_type = audit_network.known_plc_types.get(d.DeviceID, "Unknown")
                    audit_network.audit_rack(d, f, device_type)
                else:
                    f.write(f'{d.ProductName} {d.Revision}\n')

    @staticmethod
    def audit_rack(plc, f, device_type):
        max_slots = audit_network.get_max_slots(device_type)
        with PLC() as c:
            c.IPAddress = plc.IPAddress
            f.write(f'{plc.IPAddress} - {plc.ProductName}\n')
            for i in range(max_slots):
                x = c.GetModuleProperties(i)
                if x.ProductName:
                    f.write(f'\tSlot {i}:{x.ProductName}  rev:{x.Revision}\n')
            f.write('')

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            simple_read_tag()
        elif choice == '2':
            simple_write_tag()
        elif choice == '3':
            get_controller_tag_list()
        elif choice == '4':
            get_program_tag_list()
        elif choice == '5':
            device_discovery()
        elif choice == '6':
            save_tag_list()
        elif choice == '7':
            get_module_properties()
        elif choice == '8':
            audit_network.audit_controllers()
            print("Network audit completed. Check network_audit.txt file.")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
