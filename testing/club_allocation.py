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

#this data is also extracted from csv
number_of_students = 0
number_of_clubs = 0


#this code does the magic!!
def correct_club_alloc( club_number , club_capacity , priority ) :

    curr_list = result_matrix[club_number]
    selected_students = []
    end_index = 0 

    #Updating capacity to restrict size
    club_capacity -= len(curr_list)

    for indx , row in enumerate(priority_matrix):
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

#get input file from Command line
if( len(sys.argv) != 2 ) :
    print "Please provide args "
    print "python club_allocation.py <filename>"
    sys.exit(0)

#Input Processing
with open(sys.argv[1]) as csvfile:
    csvData =  csv.reader(csvfile,delimiter=',')

    #save all data to memory
    for row in csvData:
        priority_matrix.append(row[2:])
        student_name.append(row[1])
    
    #All club names as list
    club_name = priority_matrix[0]
    
    #Remove all Club Names from matrix
    priority_matrix = priority_matrix[ 1: ]

    
    number_of_students = len(priority_matrix)
    number_of_clubs = len(priority_matrix[0])
    
    club_cap = number_of_students / number_of_clubs
    
    #Initialize Using csv data
    available = [True] * number_of_students
    result_matrix = [list()] * number_of_clubs

    #To give different size to every club change code here
    club_capacity = [club_cap] * number_of_clubs
    


#Process Input
for p in range(1 , number_of_clubs+1) :
    for c_n in range(0 ,  number_of_clubs):
        result_matrix[c_n] = correct_club_alloc( c_n , club_capacity[c_n] , p )

#Write file
for indx ,row in enumerate(result_matrix):

    with open( folder_name + '/' + club_name[indx]+".csv" , 'wb' ) as myfile :

        wr = csv.writer(myfile)
        wr.writerow( ["Name"] )   
        for r in row:
            wr.writerow( [student_name[r+1]] )         


print "Please Check  ",folder_name , " folder "