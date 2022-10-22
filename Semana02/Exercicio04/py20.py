import exceptions

try:
    f=open('currupt_file.txt')
    #if f.name == 'currput_file.txt':
    #   raise Exception
    #f = open('testfile.txt')
    #var = bad_var
    #print(f.read())
    #f.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    #pass
    print('Executing Finally...')
    