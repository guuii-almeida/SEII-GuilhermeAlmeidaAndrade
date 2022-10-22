import csv
 
html_output = ''
names = []
 
with open('patrpms.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)
    
    for item in csv_data:
        print(item)
    
    #we dont want headres or fiest line of bad data
    #next(csv_data)
    next(csv_data)
    
    #print(list(csv_data))
    for line in csv_data:
        if line[0] == 'No reword':
            break
            print(line)
        names.append(f"{line['FirstName']} {line['LastName']}")
            
#for name in names:
#    print(name)
html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'
html_output += '\n<ul>'
for name in names:
    html_output += '\n\t<li>{name}<\li>'
html_output += '\n</ul<'

print(html_output)
