import csv
import allocation_choice
global max

max = 33
coursea = allocation_choice.coursea
courseb = allocation_choice.courseb
coursec = allocation_choice.coursec
coursed = allocation_choice.coursed
coursee = allocation_choice.coursee
coursef = allocation_choice.coursef

lefta =[]
leftb = []
leftc = []
leftd = []
lefte = []
leftf = []

course_students = [coursea,courseb,coursec,coursed,coursee,coursef]
#print "testing", course_students[2]
course_contents = ["a","b","c","d","e","f"]
leftout = [lefta,leftb,leftc,leftd,lefte,leftf]
print "--------------------------------------------------"
#truncate the list of students in each class to 33
for num in range(len(course_students)):
    if len(course_students[num])>max:
        leftout[num] = course_students[num][max:]
        course_students[num] = course_students[num][:max]
        
print "---------------------------------------------------"   

print "Number of students in each course after truncating to maximum"
print "--------------------------------------------------------------"     
for i in range (len(course_students)):
    print "course ",  course_contents[i], ":", len(course_students[i])
print "Number of students left out after choice 1"
print "-------------------------------------------"
for i in range(len(leftout)):
    print "course ",i+1,":", len(leftout[i])
    #----------------------------------------------------------

print "testing", len(course_students[2])

print leftout[0],len(leftout[0])
with open('choice.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    entire_details = readCSV
    for row in entire_details:
        for student in leftout[0]:
            if ((student in leftout[0]) and (student not in course_students[0])):                
                if student == row[1]:
                    second = row[3]
                    third = row[4]
                    fourth = row[5]
                    fifth = row[6]
                    print row
                    #print len(course_students[0])
                    for j in range (len(course_contents)): 
                        print "j value", j,len(course_students[j])                      
                        if ((second == course_contents[j]) and (len(course_students[j])<max)):
                            #print "hello", course_contents[j]
                            #print "hello", len(course_students[j])
                            course_students[j] = course_students[j].append(student)                             
                            print student, "in course", course_contents[j]          
                            print course_students[j]
                            break           
                        elif ((third == course_contents[j]) and (len(course_students[j])<max)):                            
                            course_students[j] = course_students[j].append(student) 
                            print student, "in course", course_contents[j]
                            break
                        #print "testing2", len(course_students[2])
                        
                        
                    #print second,third,fourth,fifth
