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


for item in subjects:
    print("Subject: "+ item + "\tLessons: "+ str(subjects[item]))