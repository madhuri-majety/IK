"""
Lets exist a spreadsheet with list of students and their notes

Id | First Name | Last Name | Notes   |
1  | Noah       | Red       | A,A,B,B |
2  | Liam       | Orange    | A,A,C,D |
3  | Mason      | Yellow    | A,A,B,B |
4  | Jacob      | Green     | A,A,C,D |
5  | William    | Cyan      | A,A,B,B |
6  | Ethan      | Blue      | A,A,C,D |
7  | James      | Indigo    | A,A,B,B |
8  | Alexander  | Violet    | A,A,C,D |

Parsed as an Array of hashes: student_list = [{id: 1, fiirst_name: 'Noah', last_name: 'Red', notes: [A,A,B,B] },{}....]

1. Sort this array by first name

2. Find notes of student with first name 'Ethan' and last name 'Blue'

3. verify if student with first name 'William' is in the list

"""
import re

def parse_spreadsheet(inp_file):
    result = []
    with open(inp_file, 'r') as fh:
        data = fh.readlines()

    print("*** Data: {}".format(data))

    for num, line in enumerate(data):
        print("Line parsing is : {}".format(line))
        student_dict = {}

        if num != 0:
            fields = line.strip('\n').split('|')
            print(fields)
            final = []
            for i, item in enumerate(fields):
                if item.strip():
                    final.append(item.strip())
            print("Fields are {}".format(final))
            if len(final) == 4:
                student_dict['id'] = final[0]
                student_dict['first'] = final[1]
                student_dict['last'] = final[2]
                student_dict['notes'] = final[3]

            result.append(student_dict)
    print("Parse Spreadsheet : {}".format(result))
    return result

def main():
    inp_file = 'spreadsheet.txt'
    student_list = parse_spreadsheet(inp_file)

    # Sort the list by first name
    student_list.sort(key = lambda hash : hash['first'])

    print("After sorting the list: {}".format(student_list))

    # Find the Student with first name and last name

    for student in student_list:
        first = False
        last = False
        for key, value in student.items():
            if key == 'first' and value.lower() == 'Ethan'.lower():
                first = True
            if key == 'last' and value.lower() == 'Blue'.lower():
                last = True

        if first and last:
            print("Found the student - {}".format(student))
    #print("Student Not Found")

    # Find if the student first name is in the list
    for student in student_list:
        for key, value in student.items():
            if key == 'first' and value.lower() == 'william'.lower():
                print("First name found")
                print(student)



if __name__ == '__main__':
    main()







