import studentManager as ST

quit = True
while quit:
    print("-"*25,"Student Management System","-"*25)
    print("Welcome, To SMS")
    print("1 : Add Student")
    print("2 : Delete Student")
    print("3 : Update Student")
    print("4 : Search By CmsID Student")
    print("5 : View Students")
    print("6 : Quit")

    ans = int(input("Press any number from above : "))

    if(ans==1):
        print("-"*25,"Add Student","-"*25)
        cms_id = input("Enter Student Cms_id : ")
        name = input("Enter Student Name : ")
        dept = input("Enter Student department : ")
        cgpa = input("Enter Student Cgpa : ")
        s = {
            "cms_id":cms_id,
            "name":name,
            "dept":dept,
            "cgpa":cgpa
        }
        ST.add_student(s)
    elif(ans==2):
        print("-"*25,"Delete Student","-"*25)    
        cms_id=input("Enter cms_id of student : ")
        ST.delete_student(cms_id) 
    elif(ans==3):
        print("-"*25,"Update Student","-"*25)    
        cms_id=input("Enter cms_id of student : ")
        if(cms_id):
            name = input("Enter Student Updated Name : ")
            dept = input("Enter Student Updated department : ")
            cgpa = input("Enter Student Updated Cgpa : ")                   
            s = {
            "cms_id":cms_id,
            "name":name,
            "dept":dept,
            "cgpa":cgpa
            }
            ST.update_student(s)
    elif(ans==4):
        print("-"*25,"Search By CmsID Student","-"*25)
        cms_id=input("Enter cms_id of student : ")
        ST.searchBYCms_id(cms_id)
    elif(ans==5):
        ST.display_students()
    elif(ans==6):
        quit=False
        break            
    print("-"*25,"Student Management System","-"*25)

print("-"*25,"Thank You For Visiting Student Management System","-"*25)
