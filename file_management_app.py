import os

# For Creating Files
def create_file(filename):
    try:
        with open(filename,'x') as file:
            print(f"File {filename} created.")
    except FileExistsError:
        print(f"File {filename} already exists!")  
    except Exception as e:
        print(f"An Error Occured!")      

# For viewing all files
def view_all_files():
    files=os.listdir()
    if not files:
        print("No File Found!")
    else:
        print("Files in Directory!")    
        for file in files:
            print(file)
 
# For deleting any file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!") 
    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print("An error occured!")            

# For reading files      
def read_file(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
            print(f"Content of {filename} : {content}")
    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print("An error occured!")            

# For editing files
def edit_file(filename):
    try:
        with open(filename,'w') as file:
            content=input("Enter data to add : ")
            file.write(content)
            print(f"Content added to {filename} successfully!")
    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print("An error occured!")

def main():
    while True:
        print("1: Create File")
        print("2: View All Files")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit")

        choice = int(input("Enter Your Choice (1-6) = "))   # For choosing operation you want to perform

        if choice==1:
            filename=input("Enter File Name to Create : ")
            create_file(filename)

        elif choice==2:
            view_all_files()

        elif choice==3:
            filename=input('Enter the file name to delete : ')   
            delete_file(filename) 

        elif choice==4:
            filename=input("Enter file name to read : ") 
            read_file(filename) 

        elif choice==5:
            filename=input("Enter file name to edit : ")  
            edit_file(filename) 

        elif choice==6:
            print("Closing the program")   
            break
        
        else:
            print("Invalid Input.") 

if __name__== "__main__":
    main()        

