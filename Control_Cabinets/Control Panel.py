from imp import get_tag
from pylogix import PLC

PLCIP = input("PLC IP Address", )


def simple_read_tag():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        Tag_Name = input("Tag Name", )
        ret = comm.Read(Tag_Name)
    print(ret.Value)

def simple_write_tag():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        Tag_Name = input("Tag Name", )
        comm.Write(Tag_Name, 10)


def get_tag_list():
    with PLC() as comm:
        comm.IPAddress = PLCIP
        tags = comm.GetTagList(False)
    
    for t in tags.Value:
        print(t.TagName, t.DataType)

