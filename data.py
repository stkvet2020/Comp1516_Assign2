

def get_student_grades():
    """ Read from data.csv and return a list of strings"""
    student_grades=[]
    fh=open("data.csv","r")
    csv_data= fh.readlines()
    fh.close()

    for item in csv_data:
        item = item.strip()
        student_grades.append(item)

    return student_grades


