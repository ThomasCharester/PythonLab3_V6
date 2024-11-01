subjects = dict()

f = open('Students.txt', 'r')

for line in f:
    subjectName = ''
    step = False
    subjectTime = 0
    charTime = ''

    for ch in line:
        if ch == ' ':
            if(step):
                subjectTime += int(charTime)
                charTime = '';
            step = True
            continue
        if not step:
            subjectName += ch
        else: 
            charTime += ch

    subjects.update({subjectName : subjectTime})


print("More than 6: ")
for item in subjects:
    if subjects[item]/5 > 6 : print(item)

