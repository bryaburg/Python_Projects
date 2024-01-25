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
