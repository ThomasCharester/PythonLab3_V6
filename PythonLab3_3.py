subjects = dict()

f = open('Flowers.txt', 'r')

for line in f:
    subjectName = ''
    step = False
    subjectLessons = ''

    for ch in line:
        if ch == ' ' or ch == '\n':
            if step:
                subjects[subjectName] += int(subjectLessons)
            else:
                subjects[subjectName] = 0
                step = True
            continue
        if not step:
            subjectName += ch
        else: 
            subjectLessons += ch


for item in subjects:
    print("Subject: "+ item + "\tlessons: "+ str(subjects[item]))