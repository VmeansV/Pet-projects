from zipfile import ZipFile   
from datetime import datetime                                      

with ZipFile('workbook.zip') as zip_file:                   #Выявление общего количества файлов
    cntr = 0
    res = zip_file.infolist()   
    for s in res:
        if s.is_dir():
            pass
        else:
            cntr += 1
     
print(cntr)


with ZipFile('workbook.zip') as zip_file:                   #Вычисление общего исходного и сжатого размера
    cntr_size = 0
    cntr_compressed_size = 0
    res = zip_file.infolist()
    for row in res:
        cntr_size += row.file_size
        cntr_compressed_size += row.compress_size
    print(f'Объем исходных файлов: {cntr_size} байт(а)')
    print(f'Объем сжатых файлов: {cntr_compressed_size} байт(а)')


with ZipFile('workbook.zip') as zip_file:                   #Поиск файла, коэффициент сжатия которого найбольший
    res = zip_file.infolist()
    cntr = 0
    for row in res:
        if row.file_size == 0:
            continue
        size = 100 - ((row.compress_size / row.file_size) * 100)
        if size > cntr:
            cntr = size
            right_name = row.filename
    print(right_name.split("/")[1])


with ZipFile('workbook.zip') as zip_file:                   #Поиск файлов, которые были созданы/изменены позже определённой даты
    rows = zip_file.infolist()
    true_date = datetime.fromisoformat('2021-11-30 14:22:00') # or true_date = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
    mylist = []
    for row in rows:
        date = datetime(*row.date_time)
        if date > true_date:
            mylist.append(row.filename.split('/')[-1])
    for row in sorted(mylist):
        if len(row) != 0:
            print(row)


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    my_dict = {}
    for row in info:
        if not row.is_dir():
            name = row.filename.split('/')[-1]
            full_size = row.file_size
            file_date = datetime(*row.date_time)
            compressed_size = row.compress_size
            my_dict.setdefault(name, [])
            my_dict[name].append(file_date)
            my_dict[name].append(full_size)
            my_dict[name].append(compressed_size)
    for key, value in sorted(my_dict.items()):
        print(key)
        print(f'  Дата модификации файла: {value[0]}')
        print(f'  Объем исходного файла: {value[1]} байт(а)')
        print(f'  Объем сжатого файла: {value[2]} байт(а)')
        print()