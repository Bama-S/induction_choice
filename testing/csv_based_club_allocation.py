import csv , random , os , sys

'''
How it works ?
Algorithm tries to allocate the closest possible choice of student

CASE 1 : If vacancies == demand
            allocate ( perfect fit )
CASE 2 : If vacancies > demand 
            allocate ( vacancies still exist )
CASE 3 : if vacancies < demand
            allocate ( there will not be vacancies after allocation )

CASE 1 : Ideal case , no handling required
CASE 2 : Allocate to all students 
CASE 3 : Shuffle students and allocate to top students



Input file format

Choice1 Choice2 Choice3
club1   club2   club3
club2   club1   club3

'''


#create output directory
folder_name = "./output"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

#get all data from csv
priority_matrix = [] 
available = []
result_matrix = []
student_name = []
student_data = []
club_name = []
club_capacity = []
club_allocate_capacity = []
priority_stats = []

#this data is also extracted from csv
number_of_students , number_of_clubs , number_of_students_allocated , pm_start , alloc_this_loop = 0 , 0 , 0 , 0 , 0

######################### Healper Code Starts #########################

#this code does the magic!!
def correct_club_alloc( club_number , club_capacity , priority ) :
    global alloc_this_loop
    curr_list = result_matrix[club_number]
    selected_students = []
    end_index = 0 

    #Updating capacity to restrict size
    club_capacity -= len(curr_list)

 
    for indx , row in enumerate(priority_matrix):
        if row[club_number] == None or row[club_number] == "" :
            #print "There is Improper value in line ", indx+1
            continue

        # int() because csv reads everything as char
        if int(row[club_number]) == int(priority) and available[indx] == True :
            selected_students.append(indx)

    #Sometimes eligible students may be less than capacity
    end_index = min( club_capacity , len(selected_students) ) 

    random.shuffle(selected_students)

    #Blocking students from appearing next time
    for indx in selected_students[:end_index]:
        available[indx] = False
        student_data[indx].append(priority)
    
    alloc_this_loop += end_index


    
    #old students + new students
    return curr_list + selected_students[:end_index]


#get input file from Command line
if( len(sys.argv) != 5 ) :
    print "Please provide args "
    print "python csv_based_club_allocation.py <student_data_file> <club_data_file> <start_of_choices>"

    print "--------- EXAMPLE --------- "
    print "python csv_based_club_allocation.py choice_1.csv  club_data.csv 2"
    print "Here choice_1.csv is file where my data is"
    print "club_data.csv is file where clubname and club capacity is present"
    print "start_of_choices means in choice_1.csv which column indicates start of choices here its column 2"
    sys.exit(0)


######################### Healper Code Ends #########################

#Main Routine

pm_start = int(sys.argv[3])
batch = sys.argv[4]

#Read Club data file
with open(sys.argv[2]) as csvfile:
    csvData = csv.reader(csvfile,delimiter=',')
    for row in csvData:
        club_name.append(row[0])
        club_capacity.append(int(row[1]) )



#Input Processing
with open(sys.argv[1]) as csvfile:
    csvData =  csv.reader(csvfile,delimiter=',')

    #save all data to memory
    for row in csvData:
        priority_matrix.append(row[pm_start:])
        student_name.append(row[0])
        student_data.append(row[0:pm_start])
    
    #Remove all Club Names from priority_matrix
    priority_matrix = priority_matrix[ 1: ]
    student_data = student_data[1:]    

    number_of_students = len(priority_matrix)
    number_of_clubs = len(club_name)
    
    club_cap = number_of_students / number_of_clubs
    
    #Initialize Using csv data
    available = [True] * number_of_students
    result_matrix = [list()] * number_of_clubs

#print student_data

#Process Input
for p in range(1 , number_of_clubs+1) :
    

    for c_n in range(0 ,  number_of_clubs):
        result_matrix[c_n] = correct_club_alloc( c_n , club_capacity[c_n] , p )
        
    
    priority_stats.append(alloc_this_loop)
    alloc_this_loop = 0

#count allocated
for indx ,row in enumerate(result_matrix) :
    club_allocate_capacity.append(len(row))
    number_of_students_allocated += len(row)

#Write file
for indx ,row in enumerate(result_matrix):

    with open( folder_name + '/' + club_name[indx]+"_"+batch+""+".csv" , 'wb' ) as myfile :

        wr = csv.writer(myfile)

        for r in row:
            wr.writerow( student_data[r]+[club_name[indx]+"_"+batch] )         


print "================== SUMMARY =================="
print "Total students " ,number_of_students
print "Total Clubs " , number_of_clubs

count = 0
for i in range(0 , number_of_clubs ):
    print club_capacity[i] , "\t" , club_allocate_capacity[i] , "\t" , club_name[i]
    count += club_allocate_capacity[i]

print "Priority Stats "
for indx , p in enumerate(priority_stats,1):
    print indx ,p
#print "Names of Clubs " ,club_name
#print "Club Capacity ", club_capacity
#print "Actual Capacity ",club_allocate_capacity

print "Allocated Students " ,count

print "Please Check  ",folder_name , " folder "


print "================ First Three ================"

for indx , c_n in enumerate(club_name) :
    print c_n
    count = 0 
    for p in range(1,4):
        
        for i in range(0 , number_of_students):
            if priority_matrix[i][indx] == None or priority_matrix[i][indx] == "":
                continue 

            if int(priority_matrix[i][indx]) == p :
                count += 1
 
        print count


<<<<<<< HEAD
    
=======
    
>>>>>>> 06eb7e37ce1e782e2ec8d233e3b5738ac172e08e
