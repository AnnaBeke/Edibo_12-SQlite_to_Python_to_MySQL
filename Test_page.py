file_to_read = open('data_in_genres.txt', 'r')
file_to_write = open('data_out_test.sql', 'w')
data = file_to_read.read()
print("Result before - file_to_read_albums.read():")
print(type(data))
print(data)

data_lines = data.split('\n')[:-1]
print("Result after - data.split(\'\n\')[:-1]:")
print(type(data_lines))
print(data_lines)

for line in data_lines[:-1]:
    print(line.split('|'))
    fields = line.split('|')
    file_to_write.write("(\'")
    i = 0
    for field in fields:
        fields[i] = field.replace("'", "\\'")
        i += 1
    for field in fields[:-1]:
        file_to_write.write(field)
        file_to_write.write("\',\'")
    file_to_write.write(fields[-1])
    file_to_write.write("\'),")
    file_to_write.write('\n')

fields = data_lines[-1].split('|')
file_to_write.write("(\'")
j = 0
for field in fields:
    fields[j] = field.replace("'", "\\'")
    j += 1
for field in fields[:-1]:
    file_to_write.write(field)
    file_to_write.write("\',\'")
file_to_write.write(fields[-1])
file_to_write.write("\');\n")
file_to_write.write('\n')