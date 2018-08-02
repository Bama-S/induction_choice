import csv , random , os

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

    club_capacity -= len(curr_list)

    for indx , row in enumerate(priority_matrix):

        if int(row[club_number]) == int(priority) and available[indx] == True :
            selected_students.append(indx)


    end_index = min( club_capacity , len(selected_students) ) 

    random.shuffle(selected_students)

    for indx in selected_students[:end_index]:
        available[indx] = False

    return curr_list + selected_students[:end_index]


with open('choice_2.csv') as csvfile:
    csvData =  csv.reader(csvfile,delimiter=',')

    for row in csvData:
        priority_matrix.append(row[2:])
        student_name.append(row[1])

    club_name = priority_matrix[0]
    priority_matrix = priority_matrix[ 1: ]

    number_of_students = len(priority_matrix)
    number_of_clubs = len(priority_matrix[0])
    
    club_cap = number_of_students / number_of_clubs
    
    available = [True] * number_of_students
    result_matrix = [list()] * number_of_clubs
    club_capacity = [club_cap] * number_of_clubs
    


for p in range(1 , number_of_clubs+1) :
    for c_n in range(0 ,  number_of_clubs):
        result_matrix[c_n] = correct_club_alloc( c_n , club_capacity[c_n] , p )


for indx ,row in enumerate(result_matrix):

    with open( folder_name + '/' + club_name[indx]+".csv" , 'wb' ) as myfile :

        wr = csv.writer(myfile)
        wr.writerow( ["Name"] )   
        for r in row:
            wr.writerow( [student_name[r+1]] )         

print "Please Check  ",folder_name , " folder "