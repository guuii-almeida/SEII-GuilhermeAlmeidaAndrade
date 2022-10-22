import os
from datetime import datetime

print(os.getcwd())

os.chdir('print')

#print(os.getcwd())

#print(os.listdir())

#'OS-Demo-2'

#os.mkdir('OS-Demo-2/Sub-Dir-1')  nao vai funcionar
#os.makedirs('OS-Demo-2/Sub-Dir-1')

#os.rmdir('OS-Demo-2')
#os.removedirs('OS-Demo-2/Sub-Dir-1')

#os.rename('test.txt', 'demo.txt')

#print(os.stat('demo.txt').st_size)

#print(os.stat('demo.txt').st_mtime

#mod_time = os.stat('demo.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))

#print(os.listdir())

#for dirpath, dirnames, filenames in os.walk('print')
#    print('Current Path:', dirpath)
#    print('Directories: ', dirnames)
#    print('Files:', filenames)
#    print()

#print(os.environ.get('HOME'))
#file_path = os.environ.get('HOME'), 'test.txt')
#print(file_path)

#print(os.path.isfile('/tmp/fgdfgdf.txt'))
#print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))
