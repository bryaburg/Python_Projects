with open(r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\K45791_01_17_2024_Comments.CSV') as comments:
    with open(r'C:\Users\bburgess\Desktop\Python_Projects\logix500to5000tags\converted.csv', 'w') as w:
        line = comments.readline()

        curr = -1

        while line != "":
            
            if not line.startswith('I') and not line.startswith('O'):
                line = comments.readline()  
                continue
            
            lineLst = line[:-1].split(',')
            
            if '/' not in lineLst[0]:
                line = comments.readline()
                continue
            
            if (name := lineLst[0].split('/')[0]) != curr:
                curr = name  
                tmp = name.split(':')
                
                w.write('TAG,,Local:{slot}:"C","","AB:1756_D{addr}:"C":1","","(ExternalAccess := Read/Write)"\n'.format(slot=tmp[1], addr=tmp[0]))
                w.write('TAG,,Local:{slot}:{addr},"","AB:1756_D{addr}:{addr}:0","","(ExternalAccess := Read/Write)"\n'.format(slot=tmp[1], addr=tmp[0]))
            
            tmp, terminal = lineLst[0].split('/')
            addr, slot = tmp.split(':')
            desc = lineLst[3]
            
            w.write('COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"\n'.format(slot=slot, addr=addr, terminal=terminal, description=desc))
            
            line = comments.readline()
