#Brandi Fletcher 3/28/24

#Random School Selection for Scheduling Priority Due to Cancellation

def main():
    import random

#school list
#list contains schools left to assign on 4/14/24

    schools = ["Athens", "Danville", "Decatur", "Hazel Green", "Mae Jeminson", "New Hope", "James Clemens"]


#create loop to randomly select school
    while True:
        i = input("Press 'c' to randomly select a school or 'quit' to exit: ")
        if i == 'quit':    
            break
        elif i!= 'c':
            print("Invalid input")
            continue
        school_selection = random.choice(schools)
        print(school_selection)
    print("Done")
__name__ == '__main__'
main()

	
