import csv
import allocation_choice
global max

max = 33
def left_len(left):
    print " Length of left out students"
    for std in left:
        print len(std), std
        
def allocate(student,coursea,courseb,coursec,coursed,coursee,coursef,second,third,fourth,fifth,pending):
    if (second == "b") and (len(courseb) <33):
        courseb = courseb.append(student)
    elif (second == "a") and (len(coursea)<33):
        coursea = coursea.append(student)
    elif (second == "c") and (len(coursec) <33):
        coursec = coursec.append(student)
    elif (second == "d") and (len(coursed) <33):
        coursed = coursed.append(student)
    elif (second == "e") and (len(coursee) <33):
        coursee = coursee.append(student)
    elif (second == "f") and (len(coursee) <33):
        coursef = coursef.append(student)
    elif (third == "a") and (len(coursea)<33):
        coursea = coursea.append(student)
    elif (third == "b") and (len(coursec) <33):
        coursec = coursec.append(student)
    elif (third == "c") and (len(coursed) <33):
        coursed = coursed.append(student)
    elif (third == "d") and (len(coursee) <33):
        coursee = coursee.append(student)
    elif (third == "e") and (len(coursed) <33):
        coursed = coursed.append(student)
    elif (third == "f") and (len(coursee) <33):
        coursee = coursee.append(student)
    elif (fourth == "a") and (len(coursea)<33):
        coursea = coursea.append(student)
    elif (fourth == "b") and (len(coursea)<33):
        courseb = courseb.append(student)
    elif (fourth == "c") and (len(coursea)<33):
        coursec = coursec.append(student)
    elif (fourth == "d") and (len(coursea)<33):
        coursed = coursed.append(student)
    elif (fourth == "e") and (len(coursea)<33):
        coursee = coursee.append(student)
    elif (fourth == "f") and (len(coursea)<33):
        coursef = coursef.append(student)
    elif (fifth == "a") and (len(coursea)<33):
        coursea = coursea.append(student)
    elif (fifth == "b") and (len(coursea)<33):
        courseb = courseb.append(student)
    elif (fifth == "c") and (len(coursea)<33):
        coursec = coursec.append(student)
    elif (fifth == "d") and (len(coursea)<33):
        coursed = coursed.append(student)
    elif (fifth == "e") and (len(coursea)<33):
        coursee = coursee.append(student)
    elif (fifth == "f") and (len(coursea)<33):
        coursef = coursef.append(student)
    else:
        pending.append(student)
    
def after_allocate(student,coursea,courseb,coursec,coursed,coursee,coursef,second,third,fourth,fifth,pending):
    if student in coursea:
        print student, "in coursea"
    elif student in courseb:
        print student, "in courseb"
    elif student in coursec:
        print student, "in coursec"
    elif student in coursed:
        print student, "in coursed"
    elif student in coursee:
        print student, "in coursee"
    elif student in coursef:
        print student, "in coursef"
    elif student in pending:
        print student, "in pending"
    

              

coursea = allocation_choice.coursea
courseb = allocation_choice.courseb
coursec = allocation_choice.coursec
coursed = allocation_choice.coursed
coursee = allocation_choice.coursee
coursef = allocation_choice.coursef

print "CourseA",len(coursea)
print "CourseB",len(courseb)
print "CourseC",len(coursec)
print "CourseD",len(coursed)
print "CourseE",len(coursee)
print "CourseF",len(coursef)



if len(coursea)>34:    
    leftA = coursea[34:]   
    coursea = coursea[0:33]
else:
    leftA = []
if len(courseb)>34:
    leftB = courseb[34:]
    courseb = courseb[0:33]
else:
    leftB=[]
if len(coursec)>34:
    leftC = coursec[34:]
    coursec = coursec[0:33]
    
else:
    leftC = []
if len(coursed)>34:    
    leftD = coursed[34:]
    coursed = coursed[0:33]
else:
    leftD = []
if len(coursee)>34:
    leftE = coursee[34:]
    coursee = coursee[0:33]
else:
    leftE = []
if len(coursef)>34:
    leftF = coursef[34:]
    coursef = coursef[0:33]
else:
    leftF = []


#print leftout students 
left = [leftA,leftB,leftC,leftD,leftE,leftF]
left_len(left)
print "--------------------------------------------"

pending = []

with open('choice.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    entire_details = readCSV
    for row in entire_details:
        for student in leftA:
            if student == row[1]:
                print row
                second = row[3]
                third = row[4]
                fourth = row[5]
                fifth = row[6]
                allocate(student,coursea,courseb,coursec,coursed,coursee,coursef,second,third,fourth,fifth,pending)
                after_allocate(student,coursea,courseb,coursec,coursed,coursee,coursef,second,third,fourth,fifth,pending)
                
print len(coursea)
print len(courseb)
print "c",len(coursec),coursec
print "d",len(coursed),coursed
print "e",len(coursee),coursee
print "f",len(coursef),coursef
print len(pending), pending




