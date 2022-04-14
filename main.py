list_of_problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


def arithmetic_arranger(problems):
    for i in problems:
        
    message = ""
    if len(problems) > 5:
        message = "Error: Too many problems."
        return message

    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {"-", "+"} and len(set(operations)) != 2:
        message = "Error: Operator must be '+' or '-'."
        return message

    numbers = []
    for i in problems:
        p = i.split()
        numbers.extend(p[0], p[2])

    if not all(map(lambda x: x.isdigit(), numbers)):
        message = "Error: Numbers must only contain digits."
        return message

    if not all(map(lambda x: len(numbers) <= 4, numbers)):
        message = "Error: Numbers cannot be more than four digits."

    else:
        message = "okay"
        return message


problem = input("Please enter a list of problems")
arithmetic_arranger(problem)
