class Address:

#    def __int__(self):
        # self.name = name
        # self.number = number
        # self.age = age


    all_person = []

    def add(self):
        name = input('name:')
        number = input('number:')
        age = input('age:')
        self.all_person.append({'name':name,'number':number,'age':age})
        self.display()

    def display(self):
        print(self.all_person)

def menu():
    p = Address()
    while True:
        print('1.Add a person')
        print('2.Delet a person')
        print('3.Modify a person')
        print('4.Display all person')
        print('5.Exit')
        oper_numer = int(input('input the number to option'))
        if oper_numer == 1:
            p.add()
        elif oper_numer == 2:
            p.delete()
        elif oper_numer == 3:
            p.modify()
        elif oper_numer == 4:
            p.display()
        elif oper_numer == 5:
            break
        else:
            print('Wrong input,please try again')

if __name__ == '__main__':
    menu()