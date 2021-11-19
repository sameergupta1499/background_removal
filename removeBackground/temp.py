s = '12 sameer'
total_lines = [i for i in s.split() if i.isdigit()][0]
s=s.replace(total_lines,'')
s=s.replace(' ','_')
print(s)

# file_name = test_string.split()
print(type(total_lines))
# print(file_name)