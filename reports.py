import datetime


def display_school_summary(num_schools, num_courses, num_students, school_list):
    """ Displays a summary of the student grade data
    :param num_schools: Number of unique schools in the data
    :param num_courses: Number of unique courses in the data
    :param num_students: Number of unique students in the data """

    # Your code here
    print("Report:          %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Number Schools:  %d" % num_schools)
    school_list_string = ','.join(school_list)
    print("Schools:         %s" % school_list_string)

    print("Number Courses:  %d" % num_courses)
    print("Number Students: %d" % num_students)


def display_school_statistics(school_name, school_exists, num_courses, num_students,
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
        print("Number Students: %d" % num_students)
        print("Average Grade:   %.1f%%" % average_grade)
        print("Median Grade:    %.1f%%" % median_grade)
        print("Lowest Grade :   %.1f%%" % min_grade)
        print("Highest Grade:   %.1f%%" % max_grade)
    else:
        print("School %s does NOT exist!" % school_name)
