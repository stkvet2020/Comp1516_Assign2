import datetime


def display_school_summary(num_schools, num_courses, num_students, school_list, school_averages_dict,
                           school_minimums_dict, school_maximums_dict):
    """ Displays a summary of the student grade data
    :param num_schools: Number of unique schools in the data
    :param num_courses: Number of unique courses in the data
    :param num_students: Number of unique students in the data
    :param school_list : Is the list of schools that then gets converted to a string
    :param school_averages_dict: A dictionary containing the name of the school name as the key and value of grades average
    :param school_minimums_dict: A dictionary containing the name of the school as the key and value of minimum grades
    :param school_maximums_dict : A dictionary containing the name of the school as the key and the value of maximum grades """

    # School averages

    print("Report:          %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Number Schools:  %d" % num_schools)
    school_list_string = ','.join(school_list)
    print("Schools:         %s" % school_list_string)

    print("Number Courses:  %d" % num_courses)
    print("Number Students: %d" % num_students)
    # School averages
    print("School Averages:")
    for school in school_averages_dict:
        print("                 %s" % school + ": %.1f%%" % school_averages_dict[school])
    # School Minimums
    print("School Minimums:")
    for school in school_minimums_dict:
        print("                 %s" % school + ": %.1f%%" % school_minimums_dict[school])
    # School Maximums
    print("School Maximums:")
    for school in school_maximums_dict:
        print("                 %s" % school + ": %.1f%%" % school_maximums_dict[school])
    # Sending print statements to a file called 'summary.txt'
    newfile = open('summary.txt', 'w')
    print("Report:          %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=newfile)
    print("Number Schools:  %d" % num_schools, file=newfile)
    school_list_string = ','.join(school_list)
    print("Schools:         %s" % school_list_string, file=newfile)

    print("Number Courses:  %d" % num_courses, file=newfile)
    print("Number Students: %d" % num_students, file=newfile)
    # School averages
    print("School Averages:", file=newfile)
    for school in school_averages_dict:
        print("                 %s" % school + ": %.1f%%" % school_averages_dict[school], file=newfile)
    # School Minimums
    print("School Minimums:", file=newfile)
    for school in school_minimums_dict:
        print("                 %s" % school + ": %.1f%%" % school_minimums_dict[school], file=newfile)
    # School Maximums
    print("School Maximums:", file=newfile)
    for school in school_maximums_dict:
        print("                 %s" % school + ": %.1f%%" % school_maximums_dict[school], file=newfile)
    newfile.close()


def display_school_statistics(school_name, school_exists, num_courses, courses, num_students, average_grade,
                              median_grade, top_student, top_grade, bottom_student, bottom_grade):
    """ Displays the statistics for the specified student
    :param school_name: Name of the school for the report
    :param school_exists: Indicates if the school actually exists
    :param num_courses: Number of courses in the data of  the school
    :param courses: a list of courses taken by students of a specific university
    :param num_students:Number of students in the data of the school
    :param average_grade: Average grade of the students in the school
    :param median_grade: Median grade of the students in the school
    :param top_student: Student with the highest average of all three courses
    :param top_grade: The grade obtained by the top student
    :param bottom_student: Student with the lowest average of all three courses
    :param bottom_grade: The grade obtained by that bottom student"""
    if school_exists:
        print("Report:          %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("School:          %s" % school_name)
        print("Number Courses:  %d" % num_courses)
        courses.sort()
        course_list_string = ','.join(courses)
        print("Courses:         %s" % course_list_string)
        print("Number Students: %d" % num_students)
        print("Average Grade:   %.1f%%" % average_grade)
        print("Median Grade:    %.1f%%" % median_grade)
        print("Top Student:     %s" % top_student)
        print("Top Grade:       %.1f%%" % top_grade)
        print("Bottom Student:  %s" % bottom_student)
        print("Bottom Grade:    %.1f%%" % bottom_grade)
        # Sending print statements to a text-file named after the school name
        file_name = ( school_name.lower() + ".txt")
        newfile = open(file_name, 'w')
        print("Report:          %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=newfile)
        print("School:          %s" % school_name, file=newfile)
        print("Number Courses:  %d" % num_courses, file=newfile)
        course_list_string = ','.join(courses)
        print("Courses:         %s" % course_list_string, file=newfile)
        print("Number Students: %d" % num_students, file=newfile)
        print("Average Grade:   %.1f%%" % average_grade, file=newfile)
        print("Median Grade:    %.1f%%" % median_grade, file=newfile)
        print("Top Student:     %s" % top_student, file=newfile)
        print("Top Grade:       %.1f%%" % top_grade, file=newfile)
        print("Bottom Student:  %s" % bottom_student, file=newfile)
        print("Bottom Grade:    %.1f%%" % bottom_grade, file=newfile)
        newfile.close()
    else:
        print("School %s does NOT exist!" % school_name)
