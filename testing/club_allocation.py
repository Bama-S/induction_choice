import csv 

priority_matrix = [] 
available = []
#number_of_students = 0

with open('choice_1.csv') as csvfile:
    csvData =  csv.reader(csvfile,delimiter=',')
    priority_matrix = csvData[1:][2:]

#    for row in csvData:
#        priority_matrix.append(row[2:])


#for row in priority_matrix:
#    print row