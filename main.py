#Skripts teksta faila apstrādei:

file_to_read = open('data_in.txt','r')
file_to_write = open('data_out.txt','w')
data = file_to_read.read()
data_lines = data.split('\n')[:-1]
for line in data_lines[:-1]:
    #print(line.split('|'))
    fields = line.split('|')
    file_to_write.write("(\'")
    for field in fields[:-1]:
        file_to_write.write(field)
        file_to_write.write("\',\'")
    file_to_write.write(fields[-1])
    file_to_write.write("\'),\n")
fields = data_lines[-1].split('|')
file_to_write.write("(\'")
for field in fields[:-1]:
    file_to_write.write(field)
    file_to_write.write("\',\'")
file_to_write.write(fields[-1])
file_to_write.write("\');\n")
file_to_read.close()
file_to_write.close()