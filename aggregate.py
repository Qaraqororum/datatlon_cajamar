import sys

file1 = open(sys.argv[1], 'r')


iden_pre = ""
curr_delta = 0
curr_reading = 0

for i, line in enumerate(file1.readlines()):
    if i != 0:
        iden, content  = line.split()
        content = content.split('|')
        
        if '' in content: content = ['0' if c == '' else c for c in content]

        if iden != iden_pre and i!= 1:

            print(iden_pre+'|'+ str(curr_reading)+'|'+str(curr_delta))
            curr_delta = 0


        

        curr_reading = int(content[1])*100 + int(content[2])*(10**(2-len(content[2])))

        curr_delta += int(content[3])*100 + int(content[4])*(10**(2-len(content[2])))
        # if (iden.split('|'))[0] == '999': print(content, curr_delta)
        
        iden_pre = iden

    else:
        print('ID|SAMPLETIME|READING|DELTA')

