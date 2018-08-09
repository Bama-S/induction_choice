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
club_name = []
club_capacity = []
club_allocate_capacity = []

#this data is also extracted from csv
number_of_students , number_of_clubs , number_of_students_allocated , pm_start  = 0 , 0 , 0 , 0

######################### Healper Code Starts #########################

#this code does the magic!!
def correct_club_alloc( club_number , club_capacity , priority ) :

    curr_list = result_matrix[club_number]
    selected_students = []
    end_index = 0 

    #Updating capacity to restrict size
    club_capacity -= len(curr_list)

    for indx , row in enumerate(priority_matrix):
        if row[club_number] == None :
            print "There is Improper value in line ", indx+1
            sys.exit(0)

        # int() because csv reads everything as char
        if int(row[club_number]) == int(priority) and available[indx] == True :
            selected_students.append(indx)

    #Sometimes eligible students may be less than capacity
    end_index = min( club_capacity , len(selected_students) ) 

    random.shuffle(selected_students)

    #Blocking students from appearing next time
    for indx in selected_students[:end_index]:
        available[indx] = False
    
    #old students + new students
    return curr_list + selected_students[:end_index]

def club_name_to_number(target_club_name  ) :
    return club_name.index(target_club_name)


def convert_to_priority_matrix(priority_matrix) :

    new_pm =[] 
    for s_no , student in enumerate(priority_matrix) :
        
        temp = [None]*number_of_clubs
        
        for priority , club_name in enumerate(student,1) :
            club_num = club_name_to_number(club_name )
            temp[club_num] = priority
 
        new_pm.append(temp)

    return new_pm
             


#get input file from Command line
if( len(sys.argv) != 4 ) :
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
        student_name.append(row[1])
    
    #Remove all Club Names from priority_matrix
    priority_matrix = priority_matrix[ 1: ]

    #All club names as list
#    for row in priority_matrix:
#        club_name += row[2:] 

    #remove duplicate names
    #club_name = list( set(club_name) )
    
    number_of_students = len(priority_matrix)
    number_of_clubs = len(club_name)
    
    club_cap = number_of_students / number_of_clubs
    
    #Initialize Using csv data
    available = [True] * number_of_students
    result_matrix = [list()] * number_of_clubs

    #To give different size to every club change code here
    #club_capacity = [club_cap] * number_of_clubs


priority_matrix = convert_to_priority_matrix(priority_matrix)


#Process Input
for p in range(1 , number_of_clubs+1) :
    for c_n in range(0 ,  number_of_clubs):
        result_matrix[c_n] = correct_club_alloc( c_n , club_capacity[c_n] , p )

#count allocated
for row in result_matrix :  
    club_allocate_capacity.append(len(row))
    number_of_students_allocated += len(row)

#Write file
for indx ,row in enumerate(result_matrix):

    with open( folder_name + '/' + club_name[indx]+".csv" , 'wb' ) as myfile :

        wr = csv.writer(myfile)
        wr.writerow( ["Name"] )   
        for r in row:
            wr.writerow( [student_name[r+1]] )         


print "================== SUMMARY =================="
print "Total students " ,number_of_students
print "Total Clubs " , number_of_clubs
print "Names of Clubs " ,club_name
print "Club Capacity ", club_capacity
print "Actual Capacity ",club_allocate_capacity
print "Allocated Students " ,number_of_students_allocated

print "Please Check  ",folder_name , " folder "