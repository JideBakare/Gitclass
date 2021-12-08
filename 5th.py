file = input('enter file name: ')
content = open(file)
for lines in content:
    output= lines.rstrip()
    print(output.upper())

print ('done!!!')

#end
