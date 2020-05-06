def run():

	imsi = int(input('Введите первый номер IMSI: '))
	iccid = int(input('Введите первый номер ICCID: '))
	count = int(input('Введите количество count: '))
	filename = input('Введите имя файла с расширением .txt: ')

	for i in range(count):
		f = open(filename, 'a')
		f.write(f'{imsi}\t {iccid}\n')
		imsi += 1
		iccid += 1
	f.close()


def help():
	
	print('Получает на вход первое значение IMSI, первое значение ICCID,\n'
    'количество строк count, имя результирующего файла в формате txt.\n'
    'Создает на выходе текстовый файл, содержащий столбцы IMSI и ICCID.\n'
    'Первая строка содержит стартовые значения, вторая - значения,\n'
    'увеличенные на 1, и т.п., всего count строк.')
