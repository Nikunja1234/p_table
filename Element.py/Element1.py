
Element1 = {
    1  : "Hydrogen",
    2  : "Helium",
    3  : "Lithium",
    4  : "Beryllium",
    5  : "Boron",
    6  : "Carbon",
    7  : "Nitrogen",
    8  : "Oxygen",
    9  : "Fluorine",
    10 : "Neon",
    11 : "Sodium",
    12 : "Magnesium",
    13 : "Aluminium",
    14 : "Silicon",
    15 : "Phosphorus",
    16 : "Sulphur",
    17 : "Chlorine",
    18 : "Argon",
    19 : "Potassium",
    20 : "Calcium"
}

choice = int(input('1: Get Atomic Number \n2. Get Element Name \n'))


def get_element_name():
    index = int(input('Please Enter Atomic Number : '))
    if index<20:
        print (Element1[index])
        return
    print ("Please enter number between 1 to 20!")

def get_atomic_number():
    val = input('Please Enter Element Name : ')
    for key, value in Element1.items():
         if val == value:
             print(key)
             return
            
    print ("key doesn't exist")


if choice==1:
    get_atomic_number()
elif choice==2:
    get_element_name()
