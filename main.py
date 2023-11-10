# Stephan Knappstein AO1208242
# In Class Lab due   10-08-2023
# Comp 1516


import grade_stats
import data
import reports
import sys


def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("Invalid number of arguments.")
        exit(0)

    report_type = sys.argv[1].strip()

    if len(sys.argv) == 2 and sys.argv[1].lower() == 'school':
        print("Not enough arguments for the School Report.")
        exit(0)

    if sys.argv[1].lower() != "summary" and sys.argv[1].lower() != "school":
        print("Invalid report type. Must be summary or school.")
        exit(0)

    if sys.argv[1].lower() == "summary" and len(sys.argv) == 2:
        get_summary = grade_stats.calculate_summary_stats(data.get_student_grades())
        num_schools = get_summary[0]
        num_courses = get_summary[1]
        num_students = get_summary[2]
        school_list = get_summary[3]
        school_averages_dict = get_summary[4]
        school_minimums_dict = get_summary[5]
        school_maximums_dict = get_summary[6]
        reports.display_school_summary(num_schools, num_courses, num_students, school_list, school_averages_dict, school_minimums_dict, school_maximums_dict  )
        exit(0)

    school_name = sys.argv[2].strip()




    if report_type.lower() == "school" and  len(sys.argv) == 3:
        # get the tuple
        get_school_stats = grade_stats.calculate_school_stats(school_name, data.get_student_grades())
        school_exists = get_school_stats[0]
        num_courses = get_school_stats[1]
        num_students = get_school_stats[2]
        average_grade = get_school_stats[3]
        median_grade = get_school_stats[4]
        min_grade = get_school_stats[5]
        max_grade = get_school_stats[6]
        reports.display_school_statistics(school_name, school_exists, num_courses, num_students,
                                          average_grade, median_grade, min_grade, max_grade)
    elif report_type.lower() == "summary" and len(sys.argv) == 3:
        print(f"Too many arguments for the summary report.")

        exit(0)


if __name__ == "__main__":
    main()