#f = open('test.txt', 'w')
#f = open('test.txt', 'r+')
#with open('test.txt', 'r') as f:
    #pass
    #f_contents = f.read()
#    f_contents = f.readlines()
#    print(f_contents, end ='')
#    f_contests = f.readline()
#    print(f_contests, end ='')
#    for line in f:
#    print(line, end='')
#    f_contents = f.read(100)
#    print(f_contents, end='')
    #size_to_read = 100
    #f_contents = f.read(size_to_read)
    #print(f_contents, end='*')
    
    #f.seek(0)
    
    #f_contents = f.read(size_to_read)
    #print(f_contents, end='*')
    
    #print(f.tell())
    
    #while len(f_contents) > 0:
    #       print(f_contents, end='*')
    #       f_contents = f.read(size_to_read)
with open('teste2.txt', 'w') as f:
    pass
#   f.write('Oi Thiago')
#   f.seek(0)
#   f.write('Oi Thiago')
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
#        for line in rf:
#            wf.write(line)
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
    
    

#f = open('test.txt', 'r')
#print(f.name)
#print(f.closed)
#f.close()
