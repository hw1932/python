def modify():
    name = input('Enter the name:')
    has_person = False

    for i in range(0, len(all_person)):
        if all_person[i][0] == name:
            all_person[i][1] = input('Enter the age:')
            all_person[i][2] = input('Enter the number:')
            has_person = True
            break

    if not has_person:
        print('�������������ͨѶ¼�в����ڡ�')
    display()