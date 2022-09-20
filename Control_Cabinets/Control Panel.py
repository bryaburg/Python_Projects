from pylogix import PLC

PLCIP = input("PLC IP Address", )

with PLC(PLCIP) as comm:
    comm.IPAddress = '10.8.236.183'
    tags = comm.GetTagList(False)
    
    for t in tags.Value:
        print(t.TagName, t.DataType)