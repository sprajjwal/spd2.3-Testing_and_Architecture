import math
def print_banner(grade_mean, sd):
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", grade_mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

def get_grades(n_student):
    return [int(input('Enter a number: '))]

def get_sqr_sum(grade_list, grade_mean):
    sqr_sum = 0
    for grade in grade_list:
        sqr_sum += (grade - grade_mean) ** 2
    return sqr_sum

def stat():
    n_student = 5
    grade_list = get_grades(n_student)

    grade_sum = sum(grade_list)
    grade_mean = sum / len(grade_list)

    sqr_sum = get_sqr_sum(grade_list, grade_mean)
    sd = math.sqrt(sqr_sum/len(grade_list))

    print_banner(grade_mean, sd)