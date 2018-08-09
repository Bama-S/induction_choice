import csv  ,sys , os ,random

club_name = []
fill_data = []

folder_name = "./output"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

#Read Club data file
with open(sys.argv[1]) as csvfile:
    csvData = csv.reader(csvfile,delimiter=',')

    for row in csvData:
        club_name.append(row)


num_of_clubs = len(club_name[0][4:])


for i in range(1,660+1) :
    temp = [ str(i)  , str("20162020"+str(i)) , "20172020"+str(i) ,"MyName"  ]
    random_prior =  list(range(1,num_of_clubs+1)) 
    random.shuffle( random_prior )
    temp += random_prior
    fill_data.append(temp)

for row in fill_data:
    print row
   

with open( './' + "test_data.csv" , 'wb' ) as myfile :
    wr = csv.writer(myfile)
    wr.writerow( club_name[0] )   
    for r in fill_data:
        wr.writerow( r )    
    