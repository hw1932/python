# coding=utf-8
import csv

def save():
    output_file = open("address_book.data", 'w')
    write = csv.writer(output_file)
    #p = pickle.Pickler(output_file)
    write.writerows(all_person)
    print(type(all_person))
    p.dump(all_person)
    output_file.close()
    print('save sucess!')

save()