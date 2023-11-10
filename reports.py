import datetime


def display_school_summary(num_schools, num_courses, num_students, school_list, school_averages_dict,
                           school_minimums_dict, school_maximums_dict):
    """ Displays a summary of the student grade data
    :param num_schools: Number of unique schools in the data
    :param num_courses: Number of unique courses in the data
    :param num_students: Number of unique students in the data """

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
    # Sending print statements to
    newfile = open('summary.txt', 'w')
    print("Report:          %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=newfile)
    print("Number Schools:  %d" % num_schools, file=newfile)
    school_list_string = ','.join(school_list)
    print("Schools:         %s" % school_list_string, file=newfile)

    print("Number Courses:  %d" % num_courses, file=newfile)
    print("Number Students: %d" % num_students, file=newfile)
    # School averages
    print("School Averages:",file=newfile)
    for school in school_averages_dict:
        print("                 %s" % school + ": %.1f%%" % school_averages_dict[school], file=newfile)
    # School Minimums
    print("School Minimums:",file=newfile)
    for school in school_minimums_dict:
        print("                 %s" % school + ": %.1f%%" % school_minimums_dict[school], file=newfile)
    # School Maximums
    print("School Maximums:",file=newfile)
    for school in school_maximums_dict:
        print("                 %s" % school + ": %.1f%%" % school_maximums_dict[school], file=newfile)
    newfile.close()

def display_school_statistics(school_name, school_exists, num_courses,  courses,  num_students,
                              average_grade, median_grade, min_grade, max_grade):
    """ Displays the statistics for the specified student
    :param school_name: Name of the school for the report
    :param school_exists: Indicates if the school actually exists
    :param num_courses: Number of courses the school
    :param average_grade: Average grade of the students in the school
    :param median_grade: Median grade of the students in the school
    :param lowest_grade: Lowest grade for the school
    :param highest_grade: Highest grade for the school """
    if school_exists:
        print("Report:          %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("School:          %s" % school_name)
        print("Number Courses:  %d" % num_courses)
        course_list_string = ','.join(courses)
        print("Schools:         %s" % course_list_string)
        print("Number Students: %d" % num_students)
        print("Average Grade:   %.1f%%" % average_grade)
        print("Median Grade:    %.1f%%" % median_grade)
        print("Lowest Grade :   %.1f%%" % min_grade)
        print("Highest Grade:   %.1f%%" % max_grade)
    else:
        print("School %s does NOT exist!" % school_name)
