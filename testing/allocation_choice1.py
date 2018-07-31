import csv
from random import sample


def allocatefirsta(row,coursea):    
    #print row[2]
    if row[2] == "a":
        coursea = coursea.append(row[1])
def allocatefirstb(row,courseb):    
    #print row[2]
    if row[2] == "b":
        courseb = courseb.append(row[1])
def allocatefirstc(row,coursec):    
    #print row[2]
    if row[2] == "c":
        coursec = coursec.append(row[1])
def allocatefirstd(row,coursed):    
    #print row[2]
    if row[2] == "d":
        coursed = coursed.append(row[1])
def allocatefirste(row,coursee):    
    #print row[2]
    if row[2] == "e":
        coursee = coursee.append(row[1])
def allocatefirstf(row,coursef):    
    #print row[2]
    if row[2] == "f":
        coursef = coursef.append(row[1])
    
with open('choice.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    course = ["a","b","c","d","e","f"]
    coursea = []
    courseb = []
    coursec = []
    coursed = []
    coursee= []
    coursef = []
    for row in readCSV:
        allocatefirsta(row,coursea)
        allocatefirstb(row,courseb)
        allocatefirstc(row,coursec)
        allocatefirstd(row,coursed)
        allocatefirste(row,coursee)
        allocatefirstf(row,coursef)
#print "A"
#print "---"
#print coursea      
#print "B"
#print "---"
#print courseb
#print "C"
#print "---"
#print coursec
#print "D"
#print "---"
#print coursed
#print "E"
#print "---"
#print coursee
#print "F"
#print "---"
#print coursef


        
#write to csv file

with open("courseA.csv", "w") as output:
    courseA = csv.writer(output, lineterminator = '\n')
    for value in coursea:
        courseA.writerow([value])
        
with open("courseB.csv", "w") as output:
    courseB = csv.writer(output, lineterminator = '\n')
    for value in courseb:
        courseB.writerow([value])
        
with open("courseC.csv", "w") as output:
    courseC = csv.writer(output, lineterminator = '\n')
    for value in coursec:
        courseC.writerow([value])

with open("courseD.csv", "w") as output:
    courseD = csv.writer(output, lineterminator = '\n')
    for value in coursed:
        courseD.writerow([value])
    
with open("courseE.csv", "w") as output:
    courseE = csv.writer(output, lineterminator = '\n')
    for value in coursee:
        courseE.writerow([value])
        
with open("courseF.csv", "w") as output:
    courseF = csv.writer(output, lineterminator = '\n')
    for value in coursef:
        courseF.writerow([value])
    
    #courseB = csv.writer(output, lineterminator = '\n')
    #courseC = csv.writer(output, lineterminator = '\n')
    #courseD = csv.writer(output, lineterminator = '\n')
    #courseE = csv.writer(output, lineterminator = '\n')
    #courseF = csv.writer(output, lineterminator = '\n')

print coursea
print "-------------------------"
print len(coursea)
print "After shuffling"
coursea = (sample(coursea,len(coursea)))
print coursea
print len(coursea)

    

