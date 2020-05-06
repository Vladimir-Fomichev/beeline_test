def run():

    import sys
    imsi = int(input('Введите номер IMSI: '))
    iccid = int(input('Введите номер ICCID: '))
    
    if (str(imsi)[:6] != '25099' and len(str(imsi)) != 15) or (str(iccid)[:8] != '8970199' and len(str(iccid)) != 18):
        print('Вы ввели неправильный номер. Программа остановлена.')
        sys.exit()

    vals = ['imsi', 'iccid', imsi, iccid]
    for i in range(2):   
        f = open(vals[i] + '.sql', 'w')
        f.write(f'create temporary table if not exists vw ({vals[i]} bigint);\n'
        f'insert into vw values({vals[i + 2]});\n'
        'delete from vw\n'
        f'where {vals[i]} in (select {vals[i]} from {vals[i]});\n'
        f'insert into {vals[i]} select * from vw')
        f.close()

    
def help():
    
    print('Получает на вход значение IMSI и ICCID.\n'
    'Проверяет общую валидность IMSI и ICCID (префиксы, количество цифр).\n'
    'Если значение невалидно, работа останавливается, выводится сообщение об ошибке.\n\n'
    'Создает два текстовых файла, в которых содержится текст SQL-запросов\n'
    'для каждого типа значения:\n'
    'проверка отсутствия значения в соответствующей таблице БД,\n'
    'вставка полученного значения в соответствующую таблицу БД.\n\n'
    'Допустимые значения:\n'
    'IMSI длина 15 цифр, диапазон 25099хххххххххх.\n'
    'ICCID длина 18 цифр, диапазон 8970199ххххххххххx.')
