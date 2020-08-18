import numpy

a = [[0 for j in range(33)] for i in range(37)]

print (a)

preffile = open("Z:\EAproject\preferences.txt")
a = [k.strip().split() for k in preffile]

print ('\n\n',a)

for i in range(a):

    if i == 1 :
        i=4;

    
print ('\n\n',a)


#numpy.savetxt("Z:\EAproject\preferences.txt",numpy.array(a),fmt='%1.1d',delimiter = ' ',newline = '\n')
