with open('K45791_01_17_2024_Comments.CSV') as comments:
    with open('converted.csv', 'w') as w:
        line = comments.readline()

        # declare the curr for the current tag in a broader scope for later
        curr = -1

        while line != "":
            # don't bother parsing lines we don't care about
            if not line.startswith('I') and not line.startswith('O'):
                line = comments.readline()  # have to move to the next line or infinite loop
                continue

            # split the contents of the line into a list we can use to make the right data
            lineLst = line[:-1].split(',')

            # if not using a / then drop it out of the thing
            if '/' not in lineLst[0]:
                line = comments.readline()
                continue

            # check to see if we've moved to a new tag or not
            if (name := lineLst[0].split('/')[0]) != curr:
                curr = name  # update the current tag we are within

                tmp = name.split(':')

                # write the tag line for the new tag we just found
                w.write('TAG,,Local:{slot}:{addr},"","AB:1756_D{addr}:{addr}:0","","(ExternalAccess := Read/Write)"\n'.format(slot=tmp[1], addr=tmp[0]))

            # build vars for the next format
            tmp, terminal = lineLst[0].split('/')
            addr, slot = tmp.split(':')
            desc = lineLst[3]

            # write the comment lines for it
            w.write('COMMENT,,Local:{slot}:{addr},"{description}",,"Local:{slot}:{addr}.DATA.{terminal}"\n'.format(slot=slot, addr=addr, terminal=terminal, description=desc))

            # move to the next line
            line = comments.readline()
