# import statistics library
import statistics
import data


# school_grades = {  'UBC' : {99,5, 34.5 , 23.4 , .....} ,
#                     'SFU' : {89,5 , ...} ,...}
# school_averages = { 'UBC' : 78.6 , 'SFU' : 89.7 , 'BCIT' : 78.9 }


def calculate_summary_stats(student_grades):
    """ Calculates statistics that summarize all schools
    :param student_grades: a list of strings containing student grade information
    :return A tuple with the summary statistics """
    # Your code here
    num_records = int(len(student_grades))

    index = 0
    university_list = []
    course_list = []
    student_list = []
    record_list = []
    # Split the strings
    while index < num_records:
        tokens = student_grades[index].split(",")
        record_list.append(tokens)
        university_list.append(tokens[0])
        course_list.append(str(tokens[1]))
        student_list.append(str(tokens[2]))
        index += 1

    # Create new lists based on conditionals to determine uniqueness
    index = 0
    unique_university_list = []
    unique_course_list = []
    unique_student_list = []
    school_list = []

    while index < len(university_list):
        if university_list[index] not in unique_university_list:
            unique_university_list.append(university_list[index])
        if course_list[index] not in unique_course_list:
            unique_course_list.append(course_list[index])
        if student_list[index] not in unique_student_list:
            unique_student_list.append(student_list[index])
        index += 1

    num_schools = len(unique_university_list)
    num_courses = len(unique_course_list)
    num_students = len(unique_student_list)
    unique_university_list.sort()
    school_list = unique_university_list

    # Functionality to obtain summary stats on school grades

    grades_list = []
    school_grades = {}
    # Code below creates a dictionary called school_grades
    index = 0
    while index < len(school_list):
        grades_list = []
        for record in record_list:
            if school_list[index].lower() == record[0].lower():
                grades_list.append(float(record[3]))

        if school_list[index] not in school_grades:
            school_grades[school_list[index]] = grades_list
        index += 1

    # calculating school averages, school minimums and school maximums
    school_averages_dict = {}
    school_minimums_dict = {}
    school_maximums_dict = {}
    for key in school_grades:

        school_average = statistics.mean(school_grades[key])
        school_minimum = min(school_grades[key])
        school_maximum = max(school_grades[key])
        if key not in school_averages_dict:
            school_averages_dict[key] = school_average
            school_minimums_dict[key] = school_minimum
            school_maximums_dict[key] = school_maximum

    return num_schools, num_courses, num_students, school_list, school_averages_dict, school_minimums_dict, school_maximums_dict


# {"A000001": {99.8, 45.6 , 78.5}, "A000002": {85.5 , .....}
def calculate_school_stats(school_name, student_grades):
    """ Calculates statistics that summarize all schools
    :param school_name: Name of the school for which to get the statistics
    :param student_grades: CSV list of student grade information
    :return A tuple with the summary statistics """

    # Your code here
    num_records = int(len(student_grades))

    # Setting up a list of lists containing the student data
    index = 0
    record_list = []

    while index < num_records:
        record = student_grades[index].split(",")
        record_list.append(record)

        index += 1

    # Get University list
    index = 0
    university_list = []
    while index < len(record_list):
        university_list.append(record_list[index][0])
        index += 1

    # Get unique University list so that we can see if school_name exists
    # to avoid hard coding the school_name
    index_2 = 0
    unique_university_list = []
    while index_2 < len(university_list):
        if university_list[index_2] not in unique_university_list:
            unique_university_list.append(university_list[index_2])
        index_2 += 1

    # select records based on user input of 'school'
    index_3 = 0
    selected_university_records = []

    if school_name in unique_university_list:

        school_exists = True
        while index_3 < len(record_list):

            if school_name.lower() == record_list[index_3][0].lower():
                selected_record = record_list[index_3]
                selected_university_records.append(selected_record)

            index_3 += 1
    else:

        print(f"School {school_name} does NOT exist!")
        exit(0)

    # Using records from selected school to calculate stats
    course_list = []
    student_list = []
    grade_list = []
    index = 0
    while index < len(selected_university_records):
        filtered_course = selected_university_records[index][1]
        filtered_student = selected_university_records[index][2]
        filtered_grade = float(selected_university_records[index][3])
        # create filtered lists
        course_list.append(str(filtered_course))
        student_list.append(str(filtered_student))
        grade_list.append(filtered_grade)
        index += 1
    # work with the selected university records to determine number of unique courses and students
    index = 0
    unique_course_list = []
    unique_student_list = []
    while index < len(selected_university_records):

        if course_list[index] not in unique_course_list:
            unique_course_list.append(course_list[index])
        if student_list[index] not in unique_student_list:
            unique_student_list.append(student_list[index])
        index += 1

    # Creating a dictionary of student grades.
    # {"A000001": {99.8, 45.6 , 78.5}, "A000002": {85.5 , .....}
    # Needs to go through the students (identified by student id) and append the grades

    # Code below creates a dictionary called school_grades
    individual_school_grades = {}
    index = 0
    while index < len(unique_student_list):
        grades_list = []
        for record in selected_university_records:
            if unique_student_list[index].lower() == record[2].lower():
                grades_list.append(float(record[3]))

        if unique_student_list[index] not in individual_school_grades:
            individual_school_grades[unique_student_list[index]] = grades_list
        index += 1
    print(individual_school_grades)
    num_courses = len(unique_course_list)
    courses = unique_course_list
    num_students = len(unique_student_list)
    # using statistics package
    average_grade = statistics.mean(grade_list)
    median_grade = statistics.median(grade_list)
    min_grade = min(grade_list)
    max_grade = max(grade_list)

    return school_exists, num_courses, courses, num_students, average_grade, median_grade, min_grade, max_grade


#calculate_summary_stats(data.get_student_grades())
school_name=input("Please enter school name")
calculate_school_stats(school_name,data.get_student_grades())
