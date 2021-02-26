# -*- coding: utf-8 -*- не редачьте код пж (/'∕.)/
# Для лучшего представления разверните окно на полный экран.
# Так. Я добавил везде комментарии, чтобы Вам было проще.
# Если есть какие-то идеи, ошибки или недоработки - отправьте
# мне письмо на kolodchuk_av_0919@1511.ru

# Рекомендуется установить шрифты из архива: mr_AfrinkG и Subdex.
# Без них программа работать, конечно, будет. Но с ними покрасивше.

try:
	from winsound import *
	from turtle import *
	from math import *
	from time import sleep
	import _tkinter
	import random
	import sys
	import _thread
except ModuleNotFoundError:
	print("Ошибка: модули не установились. Проверьте их наличие в кортеже установленных:"+sys.builtin_module_names)

# Определяем функцию side, вычисляющую длину стороны по заданным
# координатам двух точек. Так удобнее!
def side(x1, y1, x2, y2):
	side = float(sqrt(float((x2-x1)**2+(y2-y1)**2)))
	return side

# Определяем функцию get. Здесь будет работа с файлами .txt, поэтому это важно.
# Функция get выдаёт для определённого ключа значение из файла, считывая его.
def get(key_ch):
	
	# Здесь везде используется кодировка UTF-16-LE, потому что только с ней
	# Можно получить большое разнообразие символов и не получить ошибку.
	f = open(file='preferences.txt', encoding='utf-16-le', mode='r')

	# Считываем все строки и разделяем их на отдельные элементы в списке.
	onstring = f.read().split("\n")
	#print(onstring)

	# Создаём словарь, и для каждого ключа вписываем его и все его значения (через " : ")
	prefs = dict()
	for item in onstring:
		key = item.split(" : ")[0]
		value = item.split(" : ")[1:]
		prefs[key] = value
	#print(prefs)
	f.close()

	# Получаем все значения, записанные в словаре с этим ключом и возвращаем их.
	value_ch = prefs[key_ch]
	return value_ch

# Функция change очень сложна. Вообще она меняет значение какой-то переменной на другой.
# Но для этого нужно открывать, закрывать файл, создавать, менять и т.п.
def change(key_ch, value_ch):

	# Пока здесь всё то же самое. Нам нужно получить тот же словарь, что и в get.
	# Комментарии, начинающиеся с print, я использовал при настройке команды. Можете
	# убрать значок решётки, чтобы посмотреть, как это работает.
	f = open(file='preferences.txt', encoding='utf-16-le')
	#print("1. Файл открыт для чтения.")
	onstring = f.read().split("\n")
	prefs = dict()
	for item in onstring:
		key = item.split(" : ")[0]
		value = item.split(" : ")[1:]
		prefs[key] = value
	#print("2. Словарь наполнен из файла.")
	f.close()

	# Здесь мы удаляем все значения и записываем новые.
	# Не забывайте, здесь у каждого ключа свой СПИСОК значений, независимо от того,
	# сколько их. Поэтому нельзя без квадратных скобок писать value_ch, потому что
	# тогда будет считывать значения ПОСИМВОЛЬНО.
	prefs[key_ch] = None
	prefs[key_ch] = value_ch
	#print("3. Значение изменено.")

	# Самое сложное - привести изменённый список к первоначальному виду,
	# чтобы программа впоследствии его прочитала.
	string = ''
	for key in prefs.keys():
		i = 0
		string += key
		for value in prefs[key]:
			if i == 0:
				string += " : "
			string += value+' : '
			i += 1
		string += "\n"
		#print("4. Значение параметра "+str(key)+" вписано - "+str(prefs[key])+".")
	strings = string.split("\n")
	#print("5. Строка создана: "+string)
	#print("6. Файловый список создан: "+str(strings))

	# Мы получили список строк, и теперь открываем файл для записи.
	prefses = open('preferences.txt', mode='w', encoding='utf-16-le')
	#print("7. Файл открыт для записи.")

	# Для каждой строки вписываем её в файл, удаляя последние 3 символа.
	# После последнего значения тоже ставится " : " (программа откуда-то
	# берёт последним значением '', я его тоже удаляю)
	for item in strings:
		if item == '# -*- coding: utf-16-le -*- ☭':
			item = item
			prefses.write(item + "\n")
		else:
			item = item[:-3]
			prefses.write(item + "\n")
		#print("8. Вписана строка в файл:"+item)
	prefses.close()

# Теперь переходим к началу.
# Здесь мы проверим, есть ли файл с настройками или нет.
# Если есть - сразу переходим к считыванию.
# Если нет - создаём, записываем значения, а потом переходим к считыванию.
try:
	f = open(file='preferences.txt', encoding='utf-16-le')
	print("Файл preferences.txt найден, загружается список параметров.")

# Да, я использовал условие try-except, чтобы при ошибке FNFE была не ошибка, а
# другое условие.
except FileNotFoundError:
	print("Файл preferences.txt не найден, создаётся новый файл параметров.")
	f = open(file='preferences.txt', encoding='utf-16-le', mode='w')
	f.write("# -*- coding: utf-16-le -*- ☭\n")
	f.write("pen_color : black\n")
	f.write("fill_color : black\n")
	f.write("width_scr : 1600\n")
	f.write("height_scr : 900\n")
	f.write("resize_mode : on\n")
	f.write("transform_mode : on\n")
	f.write("console : enable\n")
	f.write("is_filled : false\n")
	f.write("textmode : on\n")
	f.write("diag : true\n")
	f.write("speed : 8\n")
	f.write("fontr1 : Subdex\n")
	f.write("fontr2 : mr_AfronikG\n")
	f.write("fontmode : normal\n")
	f.write("size : 2\n")
	f.write("texto : Программа создана командой Хуцкеров☭™. : Все права соблюдены, смотрите титры. : Если какой-то текст идёт шрифтом Helvetica, то вы не установили шрифты из папки.\n")
	f.write("history : ")
	f.close()
f = open(file='preferences.txt', encoding='utf-16-le', mode='r')

# Создание словаря, такое же, как и в функциях.
onstring = f.read().split("\n")[:-1]
prefs = dict()
for item in onstring:
	key = item.split(" : ")[0]
	value = item.split(" : ")[1:]
	prefs[key] = value
f.close()

# Само считывание.
t = Turtle()

try:
	# Здесь я везде использовал функцию get. Представьте, сколько было бы здесь кода,
	# если бы я всё прописывал! Кстати, заметьте: везде в конце стоит [0], потому что
	# функция возвращает список. Это не нужно тексту в углу и истории, потом покажу, почему.
	t.color = (get('pen_color')[0], get('fill_color')[0])
	t.screen.setup(width=int(get('width_scr')[0]), height=int(get('height_scr')[0]))
	resize_mode = get('resize_mode')[0]
	transform_mode = get('transform_mode')[0]
	t.pensize(get('size')[0])
	console = get('console')[0]
	is_filled = get('is_filled')[0]
	textmode = get('textmode')[0]
	diag = get('diag')[0]
	speed = float(get('speed')[0])
	fontr1 = get('fontr1')[0]
	fontr2 = get('fontr2')[0]
	fontmode = get('fontmode')[0]
	size = float(get('size')[0])
	texto_c = get('texto')
	texto = ''

	# Для этого я в файле разделяю строки двоеточием. Программа считывает это как несколько
	# значений, а потом складывает их с \n.
	for text in texto_c:
		texto += text+"\n"
	history = get('history')

# А вот здесь я не смог объяснить. Если вы что-то меняете в файле .py или .txt,
# то программа считывает файл настроек как пустой. Единственный выход - удалить файл
# .txt и всё работает.  не смог найти разумного решения, поэтому оставил как киллерфичу.
# Менять значения можно только через программу :^)

# Upd: эта штука почему-то вообще не появляется. Может я гений программирования черепашек,
# но я всё же оставлю её на всякий случай.
except KeyError:
	print("\n\nЗащита от дурачка. Вы что-то изменили в файле, теперь программа не работает.")
	print("Удалите файл preferences.txt, тогда программа заработает.")
	sys.exit()

# Вот мы и подошли, наконец, к программе. Я постарался над краткостью видения.
sleep(1)
print("\nЗдравствуй, Пользователь. Добро пожаловать в Задачу на Апрель!")
sleep(0.25)
print("Список команд и помощь по оформлению можно получить, прописав help.")
sleep(0.25)

# Этот флаг нужен при turtle screen change.
flag_continue = False

# Значит, цикл.
while True:

	# Парочка переменных, определяющая экран.
	sides = None
	
	try:
		# Первым делом - прогрузка ресурсов, о которой я уже сказал.
		f = open(file='preferences.txt', encoding='utf-16-le')
		onstring = f.read().split("\n")[:-1]
		prefs = dict()
		for item in onstring:
			key = item.split(" : ")[0]
			value = item.split(" : ")[1:]
			prefs[key] = value
		f.close()
		t.color = (get('pen_color')[0], get('fill_color')[0])
		t.screen.setup(width=int(get('width_scr')[0]), height=int(get('height_scr')[0]))
		t.pensize(get('size')[0])
		resize_mode = get('resize_mode')[0]
		transform_mode = get('transform_mode')[0]
		console = get('console')[0]
		is_filled = get('is_filled')[0]
		textmode = get('textmode')[0]
		diag = get('diag')[0]
		speed = float(get('speed')[0])
		fontr1 = get('fontr1')[0]
		fontr2 = get('fontr2')[0]
		fontmode = get('fontmode')[0]
		size = float(get('size')[0])
		texto_c = get('texto')
		texto = ''
		for text in texto_c:
			texto += text+"\n"
		history = get('history')

	# Эти две ошибки могут возникнуть, если изменить или удалить файл во время программы.
	# Так, соответственно защита от дурачка и создание файла :^)
	except KeyError:
		print("\n\nЗащита от дурачка. Вы что-то изменили в файле, теперь программа не работает.")
		print("Удалите файл preferences.txt, тогда программа заработает.")
		break

	except FileNotFoundError:
		print("Файл preferences.txt не найден, создаётся новый файл параметров.")
		f = open(file='preferences.txt', encoding='utf-16-le', mode='w')
		f.write("# -*- coding: utf-16-le -*- ☭\n")
		f.write("pen_color : black\n")
		f.write("fill_color : black\n")
		f.write("width_scr : 1600\n")
		f.write("height_scr : 900\n")
		f.write("resize_mode : on\n")
		f.write("transform_mode : on\n")
		f.write("console : enable\n")
		f.write("is_filled : false\n")
		f.write("textmode : on\n")
		f.write("diag : true\n")
		f.write("speed : 8\n")
		f.write("fontr1 : Subdex\n")
		f.write("fontr2 : mr_AfronikG\n")
		f.write("fontmode : normal\n")
		f.write("size : 2\n")
		f.write("texto : Программа создана командой Хуцкеров☭™. : Все права соблюдены, смотрите титры. : Если какой-то текст идёт шрифтом Helvetica, то вы не установили шрифты из папки.\n")
		f.write("history : ")
		f.close()
		f = open(file='preferences.txt', encoding='utf-16-le', mode='r')
		onstring = f.read().split("\n")[:-1]
		prefs = dict()
		for item in onstring:
			key = item.split(" : ")[0]
			value = item.split(" : ")[1:]
			prefs[key] = value
		f.close()
		t.color = (get('pen_color')[0], get('fill_color')[0])
		t.screen.setup(width=int(get('width_scr')[0]), height=int(get('height_scr')[0]))
		t.pensize(get('size')[0])
		resize_mode = get('resize_mode')[0]
		transform_mode = get('transform_mode')[0]
		console = get('console')[0]
		is_filled = get('is_filled')[0]
		textmode = get('textmode')[0]
		diag = get('diag')[0]
		speed = float(get('speed')[0])
		fontr1 = get('fontr1')[0]
		fontr2 = get('fontr2')[0]
		fontmode = get('fontmode')[0]
		size = float(get('size')[0])
		texto_c = get('texto')
		texto = ''
		for text in texto_c:
			texto += text+"\n"
		history = get('history')
		
	except _tkinter.TclError:
		print("\nЗачем так?")
		break

	# Очистка экрана от прошлых рисунков.
	t.reset()

	# Наш любимый текст в углу экрана.
	# Сохраняются прошлые значения цвета и скорости, ненадолго они становятся
	# 100 и ('black', 'black'), перо поднимается, быстро уходит в угол и пришет там
	# сохранённый текст, быстро уходит в 0, 0 и возвращает всё как было.
	# Функцию можно отключить в настройках: text on/off. О change поговорим после.
	if textmode == 'on':
		speed_old = t.speed()
		color_old = (t.pencolor(), t.fillcolor())
		t.color = ('black', 'black')
		t.up()
		t.speed(100)
		t.goto(-740, -440)
		t.write(texto, font=(fontr1, 15, fontmode))
		t.goto(0, 0)
		t.speed(speed_old)
		t.down()

	# Применение флага continue.
	if flag_continue:
		flag_continue = False
		continue

	# Вот главный ввод, определяющий всё. Вводим координаты через запятую, и
	# программа разделяет их.
	main_input = input("\nНапишите координаты через запятую: ")
	paramss = main_input.split(', ')

	# А вот здесь начинается своеобразный язык программирования.
	# Он даже получил своё название: Гигантский Логический Англоязычный Шуточный Ассемблер [ГЛАША]!
	# Здесь считывается значение первого параметра. Каждый раздел я прокомментирую.

	if paramss[0] == '':
		continue

	# Функция quit выходит из программы. Или можно просто нажать Enter.
	if paramss[0] == 'quit':
		print("Хорошего дня!")
		t.screen.bye()
		break
	
	# Функция resize. Это функция авто-масштабирования.
	# Она автоматически вычисляет, на какое значение нужно увеличить все иксы и игреки,
	# Чтобы фигура была умеренного размера и полностью помещалась в экран.
	if paramss[0] == 'resize':
		print('[INFO] resize_mode = '+str(resize_mode))
		sleep(1)
		continue
	if paramss[0] == 'resize on':
		print('[INFO] Функция авто-масштабирования включена.')
		change('resize_mode', ['on'])
		sleep(1)
		continue
	if paramss[0] == 'resize off':
		print('[INFO] Функция авто-масштабирования выключена.')
		change('resize_mode', ['off'])
		sleep(1)
		continue

	# Функция transform. Это функция авто-перемещения.
	# Она автоматически вычисляет 4 переменные:
	# На какое значение сдвинуть x, y, и в какую сторону,
	# чтобы сделать её максимально близкой к центру.
	if paramss[0] == 'transform':
		print('[INFO] transform_mode = '+str(transform_mode))
		sleep(1)
		continue
	if paramss[0] == 'transform on':
		print('[INFO] Функция авто-перемещения включена.')
		change('transform_mode', ['on'])
		sleep(1)
		continue
	if paramss[0] == 'transform off':
		print('[INFO] Функция авто-перемещения выключена.')
		change('transform_mode', ['off'])
		sleep(1)
		continue

	# Отображение программных изменений. Функция разработчика.
	# Наверное, когда закончу программу, я по умолчанию поставлю
	# disable, потому что мне было удобно смотреть, чего и как
	# делает моя программа, я пользователю это будет резать глаза.
	# Потом сам-то ответ не найдёшь! Если что, все они начинаются
	# со слов [SYSTEM]. Так удобнее определять. Они все отображаются,
	# когда console == 'enable'.
	if paramss[0] == 'console':
		print("Текущая настройка - отображение программных изменений: "+str(console)+".")
		sleep(1)
		continue
	if paramss[0] == 'console enable':
		print("[INFO] Отображение программных изменений включено.")
		change('console', ['enable'])
		sleep(1)
		continue
	if paramss[0] == 'console disable':
		print("[INFO] Отображение программных изменений выключено.")
		change('console', ['disable'])
		sleep(1)
		continue
	if paramss[0] == 'hello world':
		print("\nHello World!")
		continue

	# История. То, походу, для чего я затеял работу с файлом.
	# Сохраняемая и перезаписываемая история.
	# История разбивается на отдельные, по 8 значений в каждой.
	# Каждая по порядку выдаётся.
	if paramss[0] == 'history':
		history = get('history')[1:]
		lenh = len(history)
		print(lenh)
		for_8 = (lenh)/8
		for_8 = int(for_8)
		for l in range(0, for_8):
			print(str(l+1)+" координаты -",history[l], ",", history[l+1], ",", history[l+2], ",", \
			history[l+3], ",", history[l+4], ",", history[l+5], ",", history[l+6], ",", history[l+7])
		sleep(1)
		continue

	# Очищение истории - просто меняю значение истории на пустой (почти) список.
	if paramss[0] == 'history clear':
		change('history', [''])
		print("История успешно очищена.")
		sleep(1)
		continue

	# Помощь - я не мог не расписать это. Каждая функция в ГЛАШЕ расписана. И классический мануал есть.
	if paramss[0] == 'help quit':
		print("quit - завершает текущую сессию.")
		sleep(1)
		continue
	if paramss[0] == 'help credits':
		print("credits - выдаёт титры к программе. Взгляните :D")
		sleep(1)
		continue
	if paramss[0] == 'help help':
		print("help [command] - выдаёт краткий мануал по ГЛАШЕ или же отдельный по определённой команде.")
		sleep(1)
		continue
	if paramss[0] == 'help resize':
		print("resize [on/off] - выдаёт значение переменной, отвечающей за автоматичекое изменение размеров фигуры,")
		print("     или изменяет её. [По умолчанию - true]")
		sleep(1)
		continue
	if paramss[0] == 'help transform':
		print("transform [on/off] - выдаёт значение переменной, отвечающей за автоматичеcкий подгон фигуры к центру")
		print("     экрана, или изменяет её. [По умолчанию - true]")
		sleep(1)
		continue
	if paramss[0] == 'help history':
		print("history [clear] - выдаёт историю текущей сессии, или очищает её.")
		sleep(1)
		continue
	if paramss[0] == 'help console':
		print("console [enable/disable] - включает или выключает отображение программных изменений, или показывает текущее")
		print("     состояние. [По умолчанию - false]")
		sleep(1)
		continue
	if paramss[0] == 'help turtle':
		print("turtle [color/speed/size/is_filled/diag] [<args>]")
		print("         color [white/black/magenta/blue/light-blue/red/yellow/orange/violet/gray/pink] - изменяет цвет черепашки,")
		print("     или показывает текущее состояние. [По умолчанию - ('black', 'black')]")
		print("         speed [change] - изменяет скорость черепашки, или показывает текущее состояние. [По умолчанию - 8]")
		print("         size [change] - изменяет толщину пера, или показывает текущее состояние. [По умолчанию - 1]")
		print("         screen [change] - изменяет высоту/ширину экрана черепашки, или показывает текущее")
		print("     состояние. [По умолчанию - width = 1500, height = 900]")
		print("         is_filled [true/false] - изменяет настройку, отвечающую за заполнение фигуры. [По умолчанию - false]")
		print("         diag [true/false] - изменяет настройку, отвечающую за прорисовку диагоналей фигуры. [По умолчанию - true]")
		sleep(1)
		continue

	# Переходим к функциям !turtle <option> [<arg1>].
	# Их, как видно выше, много. Я сделал длинную настройку, и разнообразную.
	# Можно поменять скорость, цвет, толщину, диагонали, заполнение.

	# Вот цвет. Ничего сложного, меняем pen_color и fill_color.
	if paramss[0] == 'turtle color':
		print("[INFO] Текущая настройка - цвет пера: ('"+str(t.pencolor())+"', '"+str(t.fillcolor()+"')."))
		sleep(1)
		continue
	if paramss[0] == 'turtle color white':
		print("[INFO] Color updated: white.")
		change('pen_color', ['white'])
		change('fill_color', ['white'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('white', 'white').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color black':
		print("[INFO] Pen color updated: black.")
		change('pen_color', ['black'])
		change('fill_color', ['black'])
		if console == 'enable':
			print("[SYSTEM] Value of 't.color' было обновлено: ('black', 'black').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color magenta':
		print("[INFO] Pen color updated: magenta.")
		change('pen_color', ['magenta'])
		change('fill_color', ['magenta'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('magenta', 'magenta').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color blue':
		print("[INFO] Pen color updated: blue.")
		change('pen_color', ['blue'])
		change('fill_color', ['blue'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('blue', 'blue').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color light-blue':
		print("[INFO] Pen color updated: light-blue.")
		change('pen_color', ['light-blue'])
		change('fill_color', ['light-blue'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('light-blue', 'light-blue').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color red':
		print("[INFO] Pen color updated: red.")
		change('pen_color', ['red'])
		change('fill_color', ['red'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('red', 'red').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color yellow':
		print("[INFO] Pen color updated: yellow.")
		change('pen_color', ['yellow'])
		change('fill_color', ['yellow'])
		if console == 'enable':
			print("[SYSTEM] Value of 't.color' было обновлено: ('yellow', 'yellow').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color orange':
		print("[INFO] Pen color updated: orange.")
		change('pen_color', ['orange'])
		change('fill_color', ['orange'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('orange', 'orange').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color purple':
		print("[INFO] Pen color updated: purple.")
		change('pen_color', ['purple'])
		change('fill_color', ['purple'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('purple', 'purple').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color gray':
		print("[INFO] Pen color updated: gray.")
		change('pen_color', ['gray'])
		change('fill_color', ['gray'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('gray', 'gray').")
		sleep(1)
		continue
	if paramss[0] == 'turtle color pink':
		print("[INFO] Pen color updated: pink.")
		change('pen_color', ['pink'])
		change('fill_color', ['pink'])
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.color' было обновлено: ('pink', 'pink').")
		sleep(1)
		continue
		
	# ничего
	if paramss[0] == 'lib %scr%':
		print(sys.version)
		print("")
		print(sys.path)
		print("")
		while True:
			q = input(">>> ")
			if q == 'no':
				print('yes')
			if q == 'yes':
				break
		sleep(1)
		continue

	# Теперь скорость. Прописываем просто speed - выдаёт текущую скорость,
	# прописываем speed change -> пишем скорость -> в файл записывается новое значение.
	if paramss[0] == 'turtle speed':
		print("[INFO] Текущая настройка - скорость черепашки: "+str(t.speed))
		sleep(1)
		continue
	if paramss[0] == 'turtle speed change':
		speed = input("Напишите новую скорость черепашки: ")
		change('speed', [speed])
		print("[INFO] Скорость черепашки обновлена: "+str(speed)+".")
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.speed' было обновлено: "+str(speed)+".")
		sleep(1)
		continue

	# Аналогично с size. Та же схема 8)
	if paramss[0] == 'turtle size':
		print("[INFO] Текущая настройка - размер пера: "+str(t.pensize))
		sleep(1)
		continue
	if paramss[0] == 'turtle size change':
		size = input("Напишите новый размер пера: ")
		change('size', [size])
		print("[INFO] Размер пера обновлён: "+str(size)+".")
		if console == 'enable':
			print("[SYSTEM] Значение переменной 't.pensize' было обновлено: "+str(size)+".")
		sleep(1)
		continue
		
	# Изменение размера экрана по высоте и ширине.
	if paramss[0] == 'turtle screen':
		print("Текущий размер экрана черепашки: "+str(get('width_scr')[0])+" x "+str(get('height_scr')[0]))
		sleep(1)
		continue
	if paramss[0] == 'turtle screen change':
		print("\nВы можете выбрать предустановленные значения:\n")
		print("        5 : 4                 4 : 3              3 : 2            8 : 5 (16 : 10)            5 : 3                  16 : 9              17 : 9                21 : 9")
		print(" SXGA: 1280 x 1024    QVGA: 320 x 240      HVGA: 480 x 320      CGA: 320 x 200          WVGA: 800 x 480      WVGA NTSC: 854 x 480    2K: 2048 x 1080    UWHD: 2560 x 1080")
		print(" QSXGA: 2560 x 2048   SIF: 384 x 288       3:2 1: 1152 x 768    WXGA: 1280 x 800        WXGA: 1280 x 768     PAL+: 1024 x 576        4K: 4096 x 2160    UWQHD: 3440 x 1440")
		print("                      VGA: 640 x 480       3:2 2: 1280 x 854    8:5 1: 1440 x 900                            HD: 1280 x 720")
		print("                      PAL: 768 x 576       3:2 3: 1440 x 960    WSXGA+: 1680 x 1050                          16:9 1: 1366 x 768")
		print("                      SVGA: 800 x 600                           WUXGA: 1920 x 1200                           16:9 2: 1600 x 900")
		print("                      XGA: 1024 x 768                           WQXGA: 2560 x 1600                           Full HD: 1920 x 1080")
		print("                      XGA+: 1152 x 864                                                                       WQHD: 2560 x 1440")
		print("                      4:3 1: 1280 x 960                                                                      Ultra HD: 3840 x 2160")
		print("                      SXGA+: 1400 x 1050                                                                     5K: 5120 x 2880")
		print("                      4:3 2: 1440 x 1080                                                                     8K: 7680 x 4320")
		print("                      UXGA: 1600 x 1200                                                                      16K: 15360 x 8640")
		print("                      QXGA: 2048 x 1536                                                                      32K: 30720 x 17280")
		print("                                                                                                             48K: 46080 x 25920")
		print("                                                                                                             64K: 61440 x 34560")
		print("По умолчанию стоит 16:9 2: 1600 x 900                                                                                     128K: 122880 x 69120\n")
		ch = input("Впишите название предустановленного значения, либо впишите что-нибудь другое,\n чтобы перейти к кастомному изменению: ")

		# 5 : 4
		if ch == 'SXGA':
			change('width_scr', ['1280'])
			change('height_scr', ['1024'])
			print("Размеры экрана изменены.")
		elif ch == 'QSXGA':
			change('width_scr', ['2560'])
			change('height_scr', ['2048'])
			print("Размеры экрана изменены.")

		# 4 : 3
		elif ch == 'QVGA':
			change('width_scr', ['320'])
			change('height_scr', ['240'])
			print("Размеры экрана изменены.")
		elif ch == 'SIF':
			change('width_scr', ['384'])
			change('height_scr', ['288'])
			print("Размеры экрана изменены.")
		elif ch == 'VGA':
			change('width_scr', ['640'])
			change('height_scr', ['480'])
			print("Размеры экрана изменены.")
		elif ch == 'PAL':
			change('width_scr', ['768'])
			change('height_scr', ['576'])
			print("Размеры экрана изменены.")
		elif ch == 'SVGA':
			change('width_scr', ['800'])
			change('height_scr', ['600'])
			print("Размеры экрана изменены.")
		elif ch == 'XGA':
			change('width_scr', ['1024'])
			change('height_scr', ['768'])
		elif ch == 'XGA+':
			change('width_scr', ['1152'])
			change('height_scr', ['864'])
			print("Размеры экрана изменены.")
		elif ch == '4:3 1':
			change('width_scr', ['1280'])
			change('height_scr', ['960'])
			print("Размеры экрана изменены.")
		elif ch == 'SXGA+':
			change('width_scr', ['1400'])
			change('height_scr', ['1050'])
			print("Размеры экрана изменены.")
		elif ch == '4:3 2':
			change('width_scr', ['1440'])
			change('height_scr', ['1080'])
			print("Размеры экрана изменены.")
		elif ch == 'UXGA':
			change('width_scr', ['1600'])
			change('height_scr', ['1200'])
			print("Размеры экрана изменены.")
		elif ch == 'QXGA':
			change('width_scr', ['2048'])
			change('height_scr', ['1536'])
			print("Размеры экрана изменены.")

		# 3 : 2
		elif ch == 'HVGA':
			change('width_scr', ['480'])
			change('height_scr', ['320'])
			print("Размеры экрана изменены.")
		elif ch == '3:2 1':
			change('width_scr', ['1152'])
			change('height_scr', ['768'])
			print("Размеры экрана изменены.")
		elif ch == '3:2 2':
			change('width_scr', ['1280'])
			change('height_scr', ['854'])
			print("Размеры экрана изменены.")
		elif ch == '3:2 3':
			change('width_scr', ['1440'])
			change('height_scr', ['960'])
			print("Размеры экрана изменены.")

		# 8 : 5 (16 : 10)
		elif ch == 'CGA':
			change('width_scr', ['320'])
			change('height_scr', ['200'])
			print("Размеры экрана изменены.")
		elif ch == 'WXGA':
			change('width_scr', ['1280'])
			change('height_scr', ['800'])
			print("Размеры экрана изменены.")
		elif ch == '8:5 1':
			change('width_scr', ['1440'])
			change('height_scr', ['900'])
			print("Размеры экрана изменены.")
		elif ch == 'WSXGA+':
			change('width_scr', ['1680'])
			change('height_scr', ['1050'])
			print("Размеры экрана изменены.")
		elif ch == 'WUXGA':
			change('width_scr', ['1920'])
			change('height_scr', ['1200'])
			print("Размеры экрана изменены.")
		elif ch == 'WQXGA':
			change('width_scr', ['2560'])
			change('height_scr', ['1600'])
			print("Размеры экрана изменены.")

		# 5 : 3
		elif ch == 'WVGA':
			change('width_scr', ['800'])
			change('height_scr', ['480'])
			print("Размеры экрана изменены.")
		elif ch == 'WXGA':
			change('width_scr', ['1280'])
			change('height_scr', ['768'])
			print("Размеры экрана изменены.")

		# 16 : 9
		elif ch == 'WVGA NTSC':
			change('width_scr', ['854'])
			change('height_scr', ['480'])
			print("Размеры экрана изменены.")
		elif ch == 'PAL+':
			change('width_scr', ['1024'])
			change('height_scr', ['576'])
			print("Размеры экрана изменены.")
		elif ch == 'HD':
			change('width_scr', ['1280'])
			change('height_scr', ['720'])
			print("Размеры экрана изменены.")
		elif ch == '16:9 1':
			change('width_scr', ['1366'])
			change('height_scr', ['768'])
			print("Размеры экрана изменены.")
		elif ch == '16:9 2':
			change('width_scr', ['1600'])
			change('height_scr', ['900'])
			print("Размеры экрана изменены.")
		elif ch == 'Full HD':
			change('width_scr', ['1920'])
			change('height_scr', ['1080'])
			print("Размеры экрана изменены.")
		elif ch == 'WQHD':
			change('width_scr', ['2560'])
			change('height_scr', ['1440'])
			print("Размеры экрана изменены.")
		elif ch == 'Ultra HD':
			change('width_scr', ['3840'])
			change('height_scr', ['2160'])
			print("Размеры экрана изменены.")
		elif ch == '5K':
			change('width_scr', ['5120'])
			change('height_scr', ['2880'])
			print("Размеры экрана изменены.")
		elif ch == '8K':
			change('width_scr', ['7680'])
			change('height_scr', ['4320'])
			print("Размеры экрана изменены.")
		elif ch == '16K':
			change('width_scr', ['15360'])
			change('height_scr', ['8640'])
			print("Размеры экрана изменены.")
		elif ch == '32K':
			change('width_scr', ['30720'])
			change('height_scr', ['17280'])
			print("Размеры экрана изменены.")
		elif ch == '48K':
			change('width_scr', ['46080'])
			change('height_scr', ['25920'])
			print("Размеры экрана изменены.")
		elif ch == '64K':
			change('width_scr', ['61440'])
			change('height_scr', ['34560'])
			print("Размеры экрана изменены.")
		elif ch == '128K':
			change('width_scr', ['122880'])
			change('height_scr', ['69120'])
			print("Размеры экрана изменены.")

		# 17 : 9
		elif ch == '2K':
			change('width_scr', ['2048'])
			change('height_scr', ['1080'])
			print("Размеры экрана изменены.")
		elif ch == '4K':
			change('width_scr', ['4096'])
			change('height_scr', ['2160'])
			print("Размеры экрана изменены.")

		# 21 : 9
		elif ch == 'UWHD':
			change('width_scr', ['2560'])
			change('height_scr', ['1080'])
			print("Размеры экрана изменены.")
		elif ch == 'UWQHD':
			change('width_scr', ['3440'])
			change('height_scr', ['1440'])
			print("Размеры экрана изменены.")

		else:
			try:
				new_width = int(input("\nВпишите новое значение ширины: "))
				change('width_scr', [new_width])
				print("[SYSTEM] Значение переменной 'width_scr' было обновлено: ["+str(new_width)+"].")
			except ValueError:
				print("Вы ввели не число. Попробуйте заново")
				continue
			try:
				new_height = int(input("\nВпишите новое значение высоты: "))
				change('height_scr', [new_height])
				print("[SYSTEM] Значение переменной 'height_scr' было обновлено: ["+str(new_width)+"].")
			except ValueError:
				print("Вы ввели не число. Попробуйте заново")
				continue
			print("Размеры экрана изменены.")
		flag_continue = True
		sleep(1)
		continue

	# Заполнение фигуры. Здесь только два состояния - либо 'false', либо 'true'. Оба расписаны.
	if paramss[0] == 'turtle is_filled':
		print("[INFO] Текущая настройка - заполнение: "+is_filled+".")
		continue
	if paramss[0] == 'turtle is_filled true':
		print("[INFO] Фигуры теперь заполняются.")
		change('is_filled', ['true'])
		if console == 'enable':
			print("[SYSTEM] Значение логической переменной 'is_filled' было обновлено: true.")
		sleep(1)
		continue
	if paramss[0] == 'turtle is_filled false':
		print("[INFO] Фигуры теперь не заполняются.")
		change('is_filled', ['false'])
		if console == 'enable':
			print("[SYSTEM] Значение логической переменной 'is_filled' было обновлено: false.")
		sleep(1)
		continue

	# Аналогично с прорисовкой диагоналей. Те же два состояния.
	if paramss[0] == 'turtle diag':
		print("[INFO] Текущая настройка - прорисовка диагоналей: "+diag+".")
		continue
	if paramss[0] == 'turtle diag true':
		print("[INFO] Перо теперь рисует диагонали.")
		change('diag', ['true'])
		if console == 'enable':
			print("[SYSTEM] Значение логической переменной 'diag' было обновлено: true.")
		sleep(1)
		continue
	if paramss[0] == 'turtle diag false':
		print("[INFO] Перо теперь не рисует диагонали.")
		change('diag', ['false'])
		if console == 'enable':
			print("[SYSTEM] Значение логической переменной 'diag' было обновлено: false.")
		sleep(1)
		continue

	# Я решил всё же сделать вывод всех настроек из файла. Почему бы и нет?
	if paramss[0] == 'preferences':
		f = open(file='preferences.txt', encoding='utf-16-le')
		# Создание словаря, такое же, как и в функциях.
		onstring = f.read().split("\n")[:-2]
		prefs = dict()
		for item in onstring:
			key = item.split(" : ")[0]
			value = item.split(" : ")[1:]
			prefs[key] = value
		f.close()
		print("Получен словарь параметров: ")
		sleep(0.125)
		print(prefs)
		continue

	# Это наши титры. Да, я главный инженер, потому что вот это вот всё писал,
	# 80% трок (минимум) на моих плечах. Саша Приходько - руководитель команды,
	# поэтому он - руководитель команды. Остальные также привнесли свой вклад в задачу :D
	if paramss[0] == 'credits':
		print("\n                  ЗАДАЧА НА АПРЕЛЬ\n")
		sleep(2)
		print("          Главный инженер   Алексей Колодчук\n")
		sleep(2)
		print("     Руководитель команды   Александр Приходько\n")
		sleep(2)
		print("                     Паша   Павел Карабущенко")
		sleep(2)
		print("      Дизайн-программисты   Артём Петров")
		sleep(2)
		print("                            Филипп Куликов\n")
		sleep(2)
		# Coming soon...
		continue

	# Сбрасывание всех параметров к дефолту. Не знаю, зачем. Можно же просто перезайти!
	# Тем не менее, я это сделал.
	# UPD №1: Он выдаёт ошибку KeyError, после него всегда идёт "защита от дурачка".
	# Забил на это. Хотите дефолт? Удалите файл preferences.txt, чего мучаться!
	# UPD №2: Я удалил отовсюду !default. 

	# Да, настройка текста. Либо вывод,
	if paramss[0] == 'text':
		print("Current text: \n"+str(texto))
		continue

	# Либо отключение/включение,
	if paramss[0] == 'text off':
		textmode = 'off'
		continue
	if paramss[0] == 'text on':
		textmode = 'on'
		continue

	# Либо ввод нового, (Для переноса строки используется ' : ', т.к. эта же последовательность
	# символов используется для разделения ключа и значений, и другую последовательность словарь
	# не читает.)
	if paramss[0] == 'text change':
		texto_1 = texto
		texto = input("Введите новый текст.\nДля того, чтобы сделать перенос, пишите ' : '.\nДля отмены напишите X.\n")
		f = open(file='info.txt', mode='w', encoding='utf-8')
		prefs = dict()
		for item in onstring:
			key = item.split(" : ")[0]
			value = item.split(" : ")[1:]
			prefs[key] = value
		f.close()
		prefs['texto'] = texto
		continue

	# Либо изменение шрифтов.
	if paramss[0] == 'text font':
		print("Текущие шрифты:")
		print("1. Шрифт для слов в углу экрана - "+get('fontr1')[0]+".")
		print("2. Шрифт для вывода решения - "+get('fontr2')[0]+".")
		choice = input("Какой шрифт хотите изменить: ")
		if choice == '1':
			fontr1 = input("Введите название нового шрифта.\nУчтите, если ввод произведён неправильно, то шрифт \n будет отображаться автоматически - Helvetica: ")
			change('fontr1', [fontr1])
			continue
		elif choice == '2':
			fontr2 = input("Введите название нового шрифта.\nУчтите, если ввод произведён неправильно, то шрифт \n будет отображаться автоматически - Helvetica: ")
			change('fontr2', [fontr2])
			continue
		else:
			continue
			
	if paramss[0] == 'system':
		print("\n\nНажимайте Enter, чтобы продолжить!")
		j = input("\nИнформация об операционной системе: "+sys.platform)
		j = input("\nВерсия Python: "+sys.version)
		j = input("\nВерсия API: "+str(sys.api_version))
		j = input("\nМаксимальное число бит для хранения символа Unicode: "+str(sys.maxunicode))
		j = input("\nДоступные модули: "+str(sys.builtin_module_names))
		j = input("\nЗагруженные модули: "+str(sys.modules))
		j = input("\nЛимит рекурсии: "+str(sys.getrecursionlimit()))
		j = input("\nСписок путей поиска модулей: "+str(sys.path))
		j = input("\nПапка установки интерпретатора Python: "+str(sys.prefix))
		j = input("\nКаталог установки Python: "+str(sys.exec_prefix))
		j = input("\nПуть к интерпретатору Python: "+str(sys.executable))
		print("\n\n")
		continue

	# А вот КРАТКИЙ МАНУАЛ ПО ГЛАШЕ. Читайте :D Я расписал всё!!!
	if paramss[0] == 'help':
		print("\n\nДобро пожаловать в Гигантский Логический Англоязычный Шуточный Ассемблер [ГЛАША]!")
		print("\nВот краткий мануал по командной оболочке.")
		print("У всех команд в оболочке имеется следущее представление:\n\n!commandname [option] [<arg1>, arg2, ...]\n")
		print("Команды, на данный момент зарегистрированные в оболочке:\n")
		print("turtle [color/speed/size/is_filled/diag] [<args>]")
		print("         color [white/black/magenta/blue/light-blue/red/yellow/orange/violet/gray/pink] - изменяет цвет черепашки,")
		print("     или показывает текущее состояние. [По умолчанию - ('black', 'black')]")
		print("         speed [change] - изменяет скорость черепашки, или показывает текущее состояние. [По умолчанию - 8]")
		print("         size [change] - изменяет толщину пера, или показывает текущее состояние. [По умолчанию - 2]")
		print("         screen [change] - изменяет высоту/ширину экрана черепашки, или показывает текущее")
		print("     состояние. [По умолчанию - width = 1500, height = 900]")
		print("         is_filled [true/false] - изменяет настройку, отвечающую за заполнение фигуры. [По умолчанию - false]")
		print("         diag [true/false] - изменяет настройку, отвечающую за прорисовку диагоналей фигуры. [По умолчанию - true]\n")
		print("credits - выдаёт титры к программе. Взгляните :D\n")
		print("console [enable/disable] - включает или выключает отображение программных изменений, или показывает текущее")
		print("     состояние. [По умолчанию - disable]\n")
		print("help [command] - выдаёт этот краткий мануал или же отдельный по определённой команде.")
		print("resizemode [on/off] - выдаёт значение переменной, отвечающей за автоматическое изменение размеров фигуры,")
		print("     или изменяет её. [По умолчанию - true]\n")
		print("transformmode [on/off] - выдаёт значение переменной, отвечающей за автоматичеcкий подгон фигуры к центру")
		print("     экрана, или изменяет её. [По умолчанию - true]\n")
		print("history [clear] - выдаёт историю текущей сессии, или очищает её.\n")
		print("text [off/on/change/font] - убирает или возвращает текст слева внизу, или же изменяет его. Изменение размера")
		print("     лень добавлять :^) Кстати, в версии v1.10 добавлено изменение шрифтов!\n")
		print("preferences - выдаёт список настроек из файла\n")
		print("system - выдаёт различные характеристики системы и интерпретатора\n")
		print("quit - завершает текущую сессию. Но проще просто нажать Enter (то же самое).\n")
		print("\nЕсли текст плохо читаем, увеличьте размер шрифта или растяните окно консоли до нужного размера.\n")
		continue

	# Вот, НАКОНЕЦ-ТО, мы подошли к самому главному.
	# Здесь мы считываем переменные. Если они не могут быть переделаны в числа с плавающей запятой,
	# выскочила бы ValueError, но это я предотвратил. Если их слишком много/мало, выскочила бы
	# IndexError. Но её я тоже предотвратил :)
	try:
		x1 = float(paramss[0])
		x2 = float(paramss[2])
		x3 = float(paramss[4])
		x4 = float(paramss[6])

		y1 = float(paramss[1])
		y2 = float(paramss[3])
		y3 = float(paramss[5])
		y4 = float(paramss[7])
	except ValueError:
		print("Неправильный ввод! Попробуйте ещё раз.")
		continue
	except IndexError:
		print("Слишком много/мало аргументов! Попробуйте ещё раз.")
		continue

	# Сохраняем эти же переменные. Потом старые значения нам ещё пригодятся.
	x1r = x1
	x2r = x2
	x3r = x3
	x4r = x4
	y1r = y1
	y2r = y2
	y3r = y3
	y4r = y4
	
	if x1 >= 1000000000 or x2 >= 1000000000 or x3 >= 1000000000 or x4 >= 1000000000 or y1 >= 1000000000 or y2 >= 1000000000 or y3 >= 1000000000 or y4 >= 1000000000:
		print("\nСЛИШКАМ БАЛЬШИЕ ЧИСЯЛКИ\n")
		continue

	# Запись в историю. Мы получаем список переменных, записываем в него ещё 8, и записываем
	# список в значение.
	history_old = get('history')
	history_old.append(str(x1))
	history_old.append(str(x2))
	history_old.append(str(x3))
	history_old.append(str(x4))
	history_old.append(str(y1))
	history_old.append(str(y2))
	history_old.append(str(y3))
	history_old.append(str(y4))
	change('history', history_old)
	if console == 'enable':
		print('\n[SYSTEM] History updated: '+str(history))

	if console == 'enable':
		print('\n[SYSTEM] Полученные координаты =', paramss)
	#newcor = str(x1)+" : "+str(x2)+" : "+str(x3)+" : "+str(x4)+" : "+str(y1)+" : "+str(y2)+" : "+str(y3)+" : "+str(y4)+" : "
	

	# Так как при получении точки программа зацикливается, то для неё отдельно Паша сделал
	# считывание четвертей.
	if (x1 == x2 == x3 == x4) and (y1 == y2 == y3 == y4):
		if x1 > 0 and y1 > 0:
			print("\nЭто точка, она находится в I четверти")
		elif x1 < 0 and y1 > 0:
			print("\nЭто точка, она находится в II четверти")
		elif x1 < 0 and y1 < 0:
			print("\nЭто точка, она находится в III четверти")
		elif x1 > 0 and y1 < 0:
			print("\nЭто точка, она находится в IV четверти")
		elif x1 == 0 and y1 == 0:
			print("\nЭто точка в начале координат. Не смейтесб")
		elif x1 == 0:
			print("\nЭто точка, она находится на оси x")
		elif y1 == 0:
			print("\nЭто точка, она находится на оси y")
		j = input("\nНАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ")
		continue

	# Напомню, что я говорил ранее:
	# Это функция авто-перемещения!
	# Она автоматически вычисляет 4 переменные:
	# На какое значение сдвинуть x, y, и в какую сторону,
	# чтобы сделать её максимально близкой к центру.
	if transform_mode == 'on':
		if console == 'enable':
			print("[SYSTEM] Функция авто-перемещения включена!")

		# Обозначаем, в какую сторону.
		# Флаги либо 'pl', либо 'min'.
		tanc_x = 'pl'
		tanc_y = 'pl'

		# Вычисляем самое большое и самое мальенькое значения из иксов и игреков,
		# а потом очень сложно сравниваем в разных состояниях.
		# Но работает же - значит, все ок!
		minx = min(x1, x2, x3, x4)
		maxx = max(x1, x2, x3, x4)
		miny = min(y1, y2, y3, y4)
		maxy = max(y1, y2, y3, y4)

		# Если минимальный x соответствует максимальному.
		# Если они равны, то это точка, и программа давно уже завершилась.
		# Если они противоположны, то и не надо никуда перемещать, среднее x - на нуле.
		if abs(minx) == abs(maxx):
			res_x = 0
			tanc_x = 'pl'
		# Если минимальный и максимальный x больше нуля....
		elif minx >= 0 and maxx >= 0:
			res_x = maxx-minx
			tanc_x = 'pl'
		# Два случая, если они с разными знаками.
		elif minx <= 0 and maxx >= 0 and abs(minx) > abs(maxx):
			res_x = minx-maxx
			tanc_x = 'min'
		elif minx <= 0 and maxx >= 0 and abs(maxx) > abs(minx):
			res_x = maxx-minx
			tanc_x = 'pl'
		# Если минимальный и максимальный x меньше нуля....
		elif minx <= 0 and maxx <= 0:
			res_x = maxx-minx
			tanc_x = 'min'

		if abs(miny) == abs(maxy):
			res_y = 0
			tanc_y = 'pl'
		elif miny >= 0 and maxy >= 0:
			res_y = maxy-miny
			tanc_y = 'pl'
		elif miny <= 0 and maxy >= 0 and abs(miny) > abs(maxy):
			res_y = miny-maxy
			tanc_y = 'min'
		elif minx <= 0 and maxy >= 0 and abs(maxy) > abs(miny):
			res_y = maxy-miny
			tanc_y = 'pl'
		elif minx <= 0 and maxx <= 0:
			res_y = maxy-miny
			tanc_y = 'min'

		
		# Вывод переменных.
		if console == 'enable':
			print('[SYSTEM] Текущее значение знака по x (tanc_x) =', tanc_x)
			print('[SYSTEM] Текущее значение перемещения по x (res_x) =', res_x)
			print('[SYSTEM] Текущее значение знака по y (tanc_y) =', tanc_y)
			print('[SYSTEM] Текущее значение перемещения по y (res_y) =', res_y)

		# Лучше умножить каждое значение на 0.55. 
		if tanc_x == 'pl':
			x1 -= res_x*0.55
			x2 -= res_x*0.55
			x3 -= res_x*0.55
			x4 -= res_x*0.55

		else:
			x1 += res_x*0.55
			x2 += res_x*0.55
			x3 += res_x*0.55
			x4 += res_x*0.55

		if tanc_y == 'pl':
			y1 -= res_y*0.55
			y2 -= res_y*0.55
			y3 -= res_y*0.55
			y4 -= res_y*0.55
			
		else:
			y1 += res_y*0.55
			y2 += res_y*0.55
			y3 += res_y*0.55
			y4 += res_y*0.55
			
		#print(x1, x2, x3, x4, y1, y2, y3, y4)

	# Это я пишу в любом случае, т.к. это предупреждение о выключенной функции. А кто её будет выключать?? Ладно, идём дальше.
	if transform_mode == 'off':
		print("[SEVERE] Функция авто-перемещения выключена! Будьте осторожны, фигуры могут выходить за рамки текущего экрана.")

	# Следующая функция работает, если все расстояния больше 900 или все расстояния меньше 100.
	if ((abs(x2-x1) <=100) and (abs(x3-x1) <=100) and (abs(x4-x1) <=100) and (abs(x4-x2) <=100) and (abs(x3-x2) <=100) and (abs(x4-x3) <=100) and (abs(y2-x1) <=100) \
	and (abs(y3-y1) <=100) and (abs(y4-y1) <=100) and (abs(y4-y2) <=100) and (abs(y3-y2) <=100) and (abs(y4-y3) <=100)) or ((abs(x2-x1) >=900) or (abs(x3-x1) >=900) \
	or (abs(x4-x1) >=900) or (abs(x4-x2) >=900) or (abs(x3-x2) >=900) or (abs(x4-x3) >=900) or (abs(y2-x1) >=900) or (abs(y3-y1) >=900) or (abs(y4-y1) >=900) \
	or (abs(y4-y2) >=900) or (abs(y3-y2) >=900) or (abs(y4-y3) >=900)):

		# Напомню: это функция авто-масштабирования.
		# Она автоматически вычисляет, на какое значение нужно увеличить все иксы и игреки,
		# Чтобы фигура была умеренного размера и полностью помещалась в экран.
		if resize_mode == 'on':
			
			if console == 'enable':
				print('[SYSTEM] Функция авто-масштабирования включена!')
				print('[SYSTEM] Координаты - ', x1, ',', x2, ',', x3, ',', x4, ',', y1, ',', y2, ',', y3, ',', y4)
				print('[SYSTEM] Длины - ', abs(x2-x1), abs(x3-x1), abs(x4-x1), abs(x4-x2), abs(x3-x2), abs(x4-x3), abs(y2-y1), abs(y3-y1), abs(y4-y1), abs(y4-y2), abs(y3-y2), abs(y4-y3))

			# Так. Эта переменная вычисляется путём сравнения со всеми возможными длинами. Самая длинная длина, так сказать.
			size_big = max(abs(x2-x1), abs(x3-x1), abs(x4-x1), abs(x4-x2), abs(x3-x2), abs(x4-x3), abs(y2-y1), abs(y3-y1), abs(y4-y1), abs(y4-y2), abs(y3-y2), abs(y4-y3))

			if size_big < 1:
				size_big = 1/size_big
			
			if console == 'enable':
				print('[SYSTEM] size_big =', size_big)

			# Да, каждое значение умножается на size_big. Если, например, это
			# квадрат со стороной 50, то каждая его стороная умножается на (50v2), потому
			# что считается по диагоналям. Выходит, каждая сторона увеличивается в 7v2 раз.
			
			x1 *= 700/size_big
			x2 *= 700/size_big
			x3 *= 700/size_big
			x4 *= 700/size_big
	
			y1 *= 700/size_big
			y2 *= 700/size_big
			y3 *= 700/size_big
			y4 *= 700/size_big
			#print(x1, x2, x3, x4, y1, y2, y3, y4)

		# Опять же, предупреждение.
		if resize_mode == 'off':
			print("[SEVERE] Функция авто-масштабирования выключена! Будьте осторожны, фигуры могут выходить за рамки текущего экрана.\n")

	# Вот и прорисовка!
	# Сначала прячем черепашку.
	#t.ht()
	
	# Поднимаем перо и движемся к первой точке.
	t.up()
	t.pensize(size)
	
	t.goto(x1, y1)
	
	# Если заполнение включено - начинаем заполнять.
	if is_filled == 'true':
		t.begin_fill()

	# Опускаем перо и движемся -> 2-я точка -> 3-я -> 4-я -> 1-я.
	t.down()
	t.goto(x2, y2)
	t.goto(x3, y3)
	t.goto(x4, y4)
	t.goto(x1, y1)

	# Если заполнение включено - заканчиваем заполнять.
	if is_filled == 'true':
		t.end_fill()

	# Если включена прорисовка диагоналей, то нам нужно нарисовать ещё два отрезка:
	# От 1-й к 3-й точке и  от 2-й к 4-й точке.
	if diag == 'true':
		t.goto(x3, y3)
		t.goto(x2, y2)
		t.goto(x4, y4)
	
	# Я бы взял уже готовые значения из transform mode, но вдруг кто-нибудь его отключит, а переменных нет?
	# Здесь я объявлю их сам:
	x_min = min(x1, x2, x3, x4)
	x_max = max(x1, x2, x3, x4)
	y_min = min(y1, y2, y3, y4)
	y_max = max(y1, y2, y3, y4)
	
	if get('console')[0] == 'enable':
		if x_min == x1:
			print("1-я точка самая левая")
		if x_min == x2:
			print("2-я точка самая левая")
		if x_min == x3:
			print("3-я точка самая левая")
		if x_min == x4:
			print("4-я точка самая левая")

		if y_min == y1:
			print("1-я точка самая низкая")
		if y_min == y2:
			print("2-я точка самая низкая")
		if y_min == y3:
			print("3-я точка самая низкая")
		if y_min == y4:
			print("4-я точка самая низкая")

		if x_max == x1:
			print("1-я точка самая правая")
		if x_max == x2:
			print("2-я точка самая правая")
		if x_max == x3:
			print("3-я точка самая правая")
		if x_max == x4:
			print("4-я точка самая правая")

		if y_max == y1:
			print("1-я точка самая высокая")
		if y_max == y2:
			print("2-я точка самая высокая")
		if y_max == y3:
			print("3-я точка самая высокая")
		if y_max == y4:
			print("4-я точка самая высокая")
		print("\n")
	# Вот здесь нам пригождаются старые значения. Сохраняем их для четвертей.
	x = x1r
	y = y1r
	h = x2r
	j = y2r
	i = x3r
	u = y3r
	k = x4r
	l = y4r

	quarters = [False, False, False, False, False, False, False]

	if x > 0 and y > 0:
		quarters[0] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 1 точка находится в I четверти")
	elif x < 0 and y > 0:
		quarters[1] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 1 точка находится в II четверти")
	elif x < 0 and y < 0:
		quarters[2] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 1 точка находится в III четверти")
	elif x > 0 and y < 0:
		quarters[3] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 1 точка находится в IV четверти")
	elif x == 0 and y == 0:
		quarters[4] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 1 точка находится в начале координат")
	elif x == 0:
		quarters[5] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 1 точка находится на оси x")
	elif y == 0:
		quarters[6] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 1 точка находится на оси y")

	if h > 0 and j > 0:
		quarters[0] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 2 точка находится в I четверти")
	elif h < 0 and j > 0:
		quarters[1] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 2 точка находится в II четверти")
	elif h < 0 and j < 0:
		quarters[2] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 2 точка находится в III четверти")
	elif h > 0 and j < 0:
		quarters[3] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 2 точка находится в IV четверти")
	elif h == 0 and j == 0:
		quarters[4] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 2 точка находится в начале координат")
	elif h == 0:
		quarters[5] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 2 точка находится на оси x")
	elif j == 0:
		quarters[6] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 2 точка находится на оси y")

	if i > 0 and u > 0:
		quarters[0] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 3 точка находится в I четверти")
	elif i < 0 and u > 0:
		quarters[1] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 3 точка находится в II четверти")
	elif i < 0 and u < 0:
		quarters[2] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 3 точка находится в III четверти")
	elif i > 0 and u < 0:
		quarters[3] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 3 точка находится в IV четверти")
	elif i == 0 and u == 0:
		quarters[4] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 3 точка находится в начале координат")
	elif i == 0:
		quarters[5] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 3 точка находится на оси x")
	elif u == 0:
		quarters[6] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 3 точка находится на оси y\n")

	if k > 0 and l > 0:
		quarters[0] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 4 точка находится в I четверти\n")
	elif k < 0 and l > 0:
		quarters[1] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 4 точка находится в II четверти\n")
	elif k < 0 and l < 0:
		quarters[2] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 4 точка находится в III четверти\n")
	elif k > 0 and l < 0:
		quarters[3] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 4 точка находится в IV четверти\n")
	elif k == 0 and l == 0:
		quarters[4] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 4 точка находится в начале координат\n")
	elif k == 0:
		quarters[5] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 4 точка находится на оси x\n")
	elif l == 0:
		quarters[6] = True
		if get('console')[0] == 'enable':
			print("[SYSTEM] 4 точка находится на оси y\n")

	if quarters[0] == True:
		print("Часть фигуры находится в I четверти")
	if quarters[1] == True:
		print("Часть фигуры находится в II четверти")
	if quarters[2] == True:
		print("Часть фигуры находится в III четверти")
	if quarters[3] == True:
		print("Часть фигуры находится в IV четверти")
	if quarters[4] == True:
		print("Часть фигуры находится в начале координат")
	if quarters[5] == True:
		print("Часть фигуры находится на оси x")
	if quarters[6] == True:
		print("Часть фигуры находится на оси y")
	print("")
	

	# Фигуры.
	
	# Если хотя бы какие-то три точки лежат на одной прямой - это не 4-хугольник.
	# Вычисляем уравнение прямой для каждых двух точек, и два раза
	# подставляем в него обе оставшиеся точки.
	# Так мы вычислим, какие точки лежат на одной прямой.
	# Нам нужно доказать хотя бы одну из последовательностей:
	# а) 1 - 2 - 3;
	# б) 1 - 2 - 4;
	# в) 1 - 3 - 4;
	# г) 2 - 3 - 4.
	# Уравнение прямой: ax+by = c
	# 1. Для 1 и 2 точек: (y1-y2)*x+(x2-x1)*y+(x1*y2+x2*y1) = 0
	# 2. Для 1 и 3 точек: (y1-y3)*x+(x3-x1)*y+(x1*y3+x3*y1) = 0
	# 3. Для 1 и 4 точек: (y1-y4)*x+(x4-x1)*y+(x1*y4+x4*y1) = 0
	# 4. Для 2 и 3 точек: (y2-y3)*x+(x3-x2)*y+(x2*y3+x3*y2) = 0
	# 5. Для 2 и 4 точек: (y2-y4)*x+(x4-x2)*y+(x2*y4+x4*y2) = 0
	# 6. Для 3 и 4 точек: (y3-y4)*x+(x4-x2)*y+(x3*y4+x4*y3) = 0
	# Определим коэффициенты для каждой прямой, и сравним их, а 
	# также определим булевы переменные, показывающие равенства.

	# А также мы берём старые значения и запишем новые...

	x1n = x1
	x2n = x2
	x3n = x3
	x4n = x4
	y1n = y1
	y2n = y2
	y3n = y3
	y4n = y4

	x1 = x1r
	x2 = x2r
	x3 = x3r
	x4 = x4r
	y1 = y1r
	y2 = y2r
	y3 = y3r
	y4 = y4r

	# Вычисляем для каждого уравнения прямой коэффициенты a, b, c.
	a_12 = y1-y2
	b_12 = x2-x1
	c_12 = x1*y2+x2*y1

	a_13 = y1-y3
	b_13 = x3-x1
	c_13 = x1*y3+x3*y1

	a_14 = y1-y4
	b_14 = x4-x1
	c_14 = x1*y4+x4*y1

	a_23 = y2-y3
	b_23 = x3-x2
	c_23 = x2*y3+x3*y2

	a_24 = y2-y4
	b_24 = x4-x2
	c_24 = x2*y4+x4*y2

	a_34 = y3-y4
	b_34 = x4-x3
	c_34 = x3*y4+x4*y3

	if get('console')[0] == 'enable':
		print("[SYSTEM] 1. Для 1 и 2 точек: "+str(a_12)+"x+"+str(b_12)+"y+"+str(c_12)+" = 0")
		print("[SYSTEM] 2. Для 1 и 3 точек: "+str(a_13)+"x+"+str(b_13)+"y+"+str(c_13)+" = 0")
		print("[SYSTEM] 3. Для 1 и 4 точек: "+str(a_14)+"x+"+str(b_14)+"y+"+str(c_14)+" = 0")
		print("[SYSTEM] 4. Для 2 и 3 точек: "+str(a_23)+"x+"+str(b_23)+"y+"+str(c_23)+" = 0")
		print("[SYSTEM] 5. Для 2 и 4 точек: "+str(a_24)+"x+"+str(b_24)+"y+"+str(c_24)+" = 0")
		print("[SYSTEM] 6. Для 3 и 4 точек: "+str(a_34)+"x+"+str(b_34)+"y+"+str(c_34)+" = 0")

	# Вычисляем длины всех отрезков.
	l12 = side(x1, y1, x2, y2)
	l13 = side(x1, y1, x3, y3)
	l14 = side(x1, y1, x4, y4)
	l23 = side(x2, y2, x3, y3)
	l24 = side(x2, y2, x4, y4)
	l34 = side(x3, y3, x4, y4)

	# Создаём булевы. Первая цифра - какая точка находится на прямой между двумя другими.
	# Последние цифры - две другие точки.
	is1_23 = False
	is1_24 = False
	is1_34 = False
	
	is2_13 = False
	is2_14 = False
	is2_34 = False

	is3_12 = False
	is3_14 = False
	is3_24 = False

	is4_12 = False
	is4_13 = False
	is4_23 = False
	
	is123 = False
	is124 = False
	is134 = False
	is234 = False

	# Первая цифра в булевой обозначает, какая точка лежит на прямой, а последние цифры - между какими точками.
	# Например, булева is 2_13 обозначает, лежит ли точка 2 на прямой между точками 1 и 3. Всего 12 переменных,
	# по 1 на каждый случай. Смотрите, далее будет объяснение. Я устал переписывать снова и снова код с опре-
	# делением треугольника, поэтому просто смотрите.
	# По свойству, прямые A1x+B1y+C1 = 0 и A2x+B2y+C2 = 0 параллельны, если:
	# A1*B2 - A2*B1 = 0. Подставляем:
	
	if (a_12*b_23 - a_23*b_12 == 0) and (a_12*b_13 - a_13*b_12 == 0) and (a_13*b_23 - a_23*b_13 == 0):
		is123 = True
	if (a_12*b_24 - a_24*b_12 == 0) and (a_12*b_14 - a_14*b_12 == 0) and (a_14*b_24 - a_24*b_14 == 0):
		is124 = True
	if (a_13*b_34 - a_34*b_13 == 0) and (a_13*b_14 - a_14*b_13 == 0) and (a_14*b_34 - a_34*b_14 == 0):
		is134 = True
	if (a_23*b_34 - a_34*b_23 == 0) and (a_23*b_24 - a_24*b_23 == 0) and (a_24*b_34 - a_34*b_24 == 0):
		is234 = True
	
	# Я создал булеву quadrangle, отвечающую за то, является ли фигура четырёхугольником или нет.
	quadrangle = True

	# Если 1 точка между 2 и 3, 2 точка между 1 и 3, 3 точка между 1 и 2 - всё равно будет выдавать (если бы мы
	# считали даже по одной булевой, на каждый случай расписывая свой цикл if):
	# is2_13 = True, is1_23 = True, is3_12 = True, а все остальные False.
	# Поэтому я смотрю, точно ли выходит именно эта тройка True. Потом свряю суммы отрезков. Если отрезок 13 - это сумма от-
	# резков 12 и 23, то точка 2 - между 1 и 3. Также - это треугольник.
	if is123:
			if l12+l23 == l13:
					is2_13 = True
			if l12+l13 == l23:
					is1_23 = True
			if l13+l23 == l12:
					is3_12 = True

	# Аналогично с другими тремя тройками.
	if is124:
			if l12+l24 == l14:
					is2_14 = True
			if l12+l14 == l24:
					is1_24 = True
			if l14+l24 == l12:
					is4_12 = True
			
	if is134:
			if l13+l34 == l14:
					is3_14 = True
			if l13+l14 == l34:
					is1_34 = True
			if l14+l34 == l13:
					is4_13 = True

	if is234:
			if l23+l34 == l24:
					is3_24 = True
			if l23+l24 == l34:
					is2_34 = True
			if l24+l34 == l23:
					is4_23 = True
			
	if get('console')[0] == 'enable':
		print("\n[SYSTEM] is1_23 = "+str(is1_23))
		print("[SYSTEM] is1_24 = "+str(is1_24))
		print("[SYSTEM] is1_34 = "+str(is1_34))
		print("[SYSTEM] is2_13 = "+str(is2_13))
		print("[SYSTEM] is2_14 = "+str(is2_14))
		print("[SYSTEM] is2_34 = "+str(is2_34))
		print("[SYSTEM] is3_12 = "+str(is3_12))
		print("[SYSTEM] is3_14 = "+str(is3_14))
		print("[SYSTEM] is3_24 = "+str(is3_24))
		print("[SYSTEM] is4_12 = "+str(is4_12))
		print("[SYSTEM] is4_13 = "+str(is4_13))
		print("[SYSTEM] is4_23 = "+str(is4_23))
		print("[SYSTEM] is123 = "+str(is123))
		print("[SYSTEM] is124 = "+str(is124))
		print("[SYSTEM] is134 = "+str(is134))
		print("[SYSTEM] is234 = "+str(is234)+"\n")

	if is123 == True and is124 == is134 == is234 == False:
		quadrangle = False
	if is124 == True and is123 == is134 == is234 == False:
		quadrangle = False
	if is134 == True and is123 == is124 == is234 == False:
		quadrangle = False
	if is234 == True and is123 == is124 == is134 == False:
		quadrangle = False

	k12 = False
	k13 = False
	k14 = False
	k23 = False
	k24 = False
	k34 = False

	if x1 == x2 and y1 == y2:
		k12 = True
	if x1 == x3 and y1 == y3:
		k13 = True
	if x1 == x4 and y1 == y4:
		k14 = True
	if x2 == x3 and y2 == y3:
		k23 = True
	if x2 == x4 and y2 == y4:
		k24 = True
	if x3 == x4 and y3 == y4:
		k34 = True
	

	if k12 or k13 or k14 or k23 or k24 or k34:
		quadrangle = False

	if not quadrangle:

		# Хорошо, мы добились того, что это - не четырёхуголбник.
		
		# Саша Приходько расписал 2 случая, когда фигура - отрезок.
		# 1-й тип - все игреки совпадают:
		if y1 == y2 == y3 == y4:
			is_line = True

		# 2-й тип - Сашин - никакие игреки не совпадают (чтобы не было деления на 0) и отношения разниц координат каждых двух точек равны:
		if (not (y1==y2 or y1==y3 or y1==y4 or y2==y3 or y2==y4 or y3==y4) and (x2-x1)/(y2-y1)==(x3-x1)/(y3-y1) == (x4-x1)/(y4-y1)== (x2-x1)/(y2-y1)):
			is_line = True
			
		# 3-й тип добавил Лёха. Хотя бы какие-то любые 3 точки совпадают - это отрезок.
		if (k12 and k13) or (k12 and k14) or (k12 and k23) or (k12 and k24) or (k12 and k34) \
		or (k13 and k14) or (k13 and k23) or (k13 and k24) or (k13 and k34) or (k14 and k23) \
		or (k14 and k24) or (k14 and k34) or (k23 and k24) or (k23 and k34) or (k24 and k34):
			is_line = True
			
		# 4-й тип добавил Лёха. Появились большие проблемы с отрезками, если какие-то
		# повторяющиеся точки есть - программа падает на ZeroDivisionError с треугольником.
		# Расширенный 2-й тип.
		is_line = False
		if k12:
			if (not (y1==y3 or y1==y4 or y3==y4) and (x3-x1)/(y3-y1) == (x4-x1)/(y4-y1) == (x4-x3)/(y4-y3)):
				is_line = True
		if k13:
			if (not (y1==y2 or y1==y4 or y2==y4) and (x2-x1)/(y2-y1) == (x4-x1)/(y4-y1) == (x4-x2)/(y4-y2)):
				is_line = True
		if k14:
			if (not (y1==y2 or y1==y3 or y2==y3) and (x2-x1)/(y2-y1) == (x3-x1)/(y3-y1) == (x3-x2)/(y3-y2)):
				is_line = True
		if k23:
			if (not (y1==y3 or y1==y4 or y3==y4) and (x3-x1)/(y3-y1) == (x4-x1)/(y4-y1) == (x4-x3)/(y4-y3)):
				is_line = True
		if k24:
			if (not (y1==y3 or y1==y4 or y3==y4) and (x3-x1)/(y3-y1) == (x4-x1)/(y4-y1) == (x4-x3)/(y4-y3)):
				is_line = True
		if k34:
			if (not (y1==y2 or y1==y4 or y2==y4) and (x2-x1)/(y2-y1) == (x4-x1)/(y4-y1) == (x4-x2)/(y4-y2)):
				is_line = True
		if (k12 and k13) or (k12 and k14) or (k12 and k14) or (k12 and k23) or (k12 and k24) or (k12 and k34)\
		 or (k13 and k14) or (k13 and k23) or (k13 and k24) or (k13 and k34) or (k14 and k23) or (k14 and k24)\
		  or (k14 and k24) or (k14 and k34) or (k23 and k24) or (k24 and k34):
			is_line = True
		
		if is_line:
			print("\nЭто отрезок")
			t.up()
			t.goto(-750, 400)
			t.write("Это отрезок.", font=("mr_AfronikG", 25, "normal"))
			# Уравнение прямой для 1 и 2 точек: (y1-y2)*x+(x2-x1)*y+(x1*y2+x2*y1) = 0
			a = float(miny-maxy)
			b = float(maxx-minx)
			c = float(minx*maxy+maxx*miny)
			if b>=0 and c>=0:
				urvn = "Уравнение прямой: "+str(a)+"x + "+str(abs(b))+"y + "+str(abs(c))+" = 0"
			if b>=0 and c<0:
				urvn = "Уравнение прямой: "+str(a)+"x + "+str(abs(b))+"y - "+str(abs(c))+" = 0"
			if b<0 and c>=0:
				urvn = "Уравнение прямой: "+str(a)+"x - "+str(abs(b))+"y + "+str(abs(c))+" = 0"
			if b<0 and c<0:
				urvn = "Уравнение прямой: "+str(a)+"x - "+str(abs(b))+"y - "+str(abs(c))+" = 0"
			t.goto(-750, 360)
			print(urvn)
			t.write(urvn, font=("mr_AfronikG", 25, "normal"))
			j = input("\nНАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ")
			continue
			
		# sides - переменная, обозначающая наличие треугольника.
		# extra - есть ли дополнительный отрезок (а то есть,
		# лежит ли экстра-точка на прямой или же совпадает с другой)
		# a, b, c, bd, ad, d - отрезки. Постараюсь их нарисовать:
		#
		#          A
		#     ad  /\            bd+ad = c.
		# c      /  \ am        bm+cm1 = a.
		#     D /    \      b   am+cm2 = b.
		#      /∖_    \ M2
		#  bd /  d∖_   \        d, AM1, BM2 - дополнительные отрезки.
		#    /      ∖__ \ cm2
		#   /__________-∖\      bd, ad - части отрезка c, смежные с a и b
		#   B bm  M1  cm1 C     соответственно и разделённые d.
		#           a
		#
		# 18 типов треугольников, все расписаны.
		# 6 типов, при которых какие-то две точки совпадают,
		# и 12 типов - если какие-то три точки лежат на одной прямой.

		# 1 тип:
		if k12:
			print("Это треугольник.")
			print("1-я точка совпала со 2-й.")
			# Вычисление параметров.
			sides = 3
			extra = False
			a = side(x1, y1, x3, y3)
			b = side(x1, y1, x4, y4)
			c = side(x3, y3, x4, y4)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			
			xa = x1
			ya = y1
			xb = x2
			yb = y2
			xc = x3
			yc = y3
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1/2 - 3")
				print("[SYSTEM] Сторона 2: 1/2 - 4")
				print("[SYSTEM] Сторона 2: 3 - 4")

			# Также черепашка поднимает перо, идёт в правый верхний угол и пишет результат :]
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 1-я точка совпала со 2-й.", font=("mr_AfronikG", 25, "normal"))

		# 2 тип:
		elif k13:
			print("Это треугольник.")
			print("1-я точка совпала со 3-й.")
			sides = 3
			extra = False
			a = side(x1, y1, x2, y2)
			b = side(x1, y1, x4, y4)
			c = side(x2, y2, x4, y4)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			
			xa = x4
			ya = y4
			xb = x2
			yb = y2
			xc = x1
			yc = y1
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1/3 - 2")
				print("[SYSTEM] Сторона 2: 1/3 - 4")
				print("[SYSTEM] Сторона 2: 2 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 1-я точка совпала со 3-й.", font=("mr_AfronikG", 25, "normal"))

		# 3 тип:
		elif k14:
			print("Это треугольник.")
			print("1-я точка совпала со 4-й.")
			sides = 3
			extra = False
			a = side(x1, y1, x2, y2)
			b = side(x1, y1, x3, y3)
			c = side(x2, y2, x3, y3)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			
			xa = x3
			ya = y3
			xb = x2
			yb = y2
			xc = x1
			yc = y1
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1/4 - 2")
				print("[SYSTEM] Сторона 2: 1/4 - 3")
				print("[SYSTEM] Сторона 2: 2 - 3")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 1-я точка совпала со 4-й.", font=("mr_AfronikG", 25, "normal"))

		# 4 тип:
		elif k23:
			print("Это треугольник.")
			print("2-я точка совпала со 3-й.")
			sides = 3
			extra = False
			a = side(x2, y2, x1, y1)
			b = side(x2, y2, x4, y4)
			c = side(x1, y1, x4, y4)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			
			xa = x4
			ya = y4
			xb = x1
			yb = y1
			xc = x2
			yc = y2
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 2/3 - 1")
				print("[SYSTEM] Сторона 2: 2/3 - 4")
				print("[SYSTEM] Сторона 2: 1 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 2-я точка совпала со 3-й.", font=("mr_AfronikG", 25, "normal"))

		# 5 тип:
		elif k24:
			print("Это треугольник.")
			print("2-я точка совпала со 4-й.")
			sides = 3
			extra = False
			a = side(x2, y2, x1, y1)
			b = side(x2, y2, x3, y3)
			c = side(x1, y1, x3, y3)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			
			xa = x3
			ya = y3
			xb = x1
			yb = y1
			xc = x2
			yc = y2
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 2/4 - 1")
				print("[SYSTEM] Сторона 2: 2/4 - 3")
				print("[SYSTEM] Сторона 2: 2 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 2-я точка совпала со 4-й.", font=("mr_AfronikG", 25, "normal"))

		# 6 тип:
		elif k34:
			print("Это треугольник.")
			print("3-я точка совпала со 4-й.")
			sides = 3
			extra = False
			a = side(x3, y3, x1, y1)
			b = side(x3, y3, x2, y2)
			c = side(x1, y1, x2, y2)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			
			xa = x2
			ya = y2
			xb = x1
			yb = y1
			xc = x3
			yc = y3
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 3/4 - 1")
				print("[SYSTEM] Сторона 2: 3/4 - 2")
				print("[SYSTEM] Сторона 2: 1 - 2")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 3-я точка совпала со 4-й.", font=("mr_AfronikG", 25, "normal"))
			
		# 7 тип:
		elif is1_23:
			print("Это треугольник.")
			print("1-я точка лежит между 2 и 3 точками.")
			sides = 3
			extra = True
			a = side(x2, y2, x4, y4)
			b = side(x3, y3, x4, y4)
			c = side(x2, y2, x3, y3)
			bd = side(x1, y1, x2, y2)
			ad = side(x1, y1, x3, y3)
			d = side(x4, y4, x1, y1)
			
			xa = x2
			ya = y2
			xb = x3
			yb = y3
			xc = x4
			yc = y4
			xd = x1
			yd = y1
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 2 - 1 - 3")
				print("[SYSTEM] Сторона 2: 3 - 4")
				print("[SYSTEM] Сторона 2: 2 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 1-я точка лежит между 2 и 3 точками.", font=("mr_AfronikG", 25, "normal"))

		# 8 тип:
		elif is1_34:
			print("Это треугольник.")
			print("1-я точка лежит между 3 и 4 точками.")
			sides = 3
			extra = True
			a = side(x2, y2, x4, y4)
			b = side(x2, y2, x3, y3)
			c = side(x3, y3, x4, y4)
			bd = side(x1, y1, x4, y4)
			ad = side(x1, y1, x3, y3)
			d = side(x2, y2, x1, y1)
			
			xa = x3
			ya = y3
			xb = x4
			yb = y4
			xc = x2
			yc = y2
			xd = x1
			yd = y1
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 2 - 3")
				print("[SYSTEM] Сторона 2: 3 - 1 - 4")
				print("[SYSTEM] Сторона 2: 2 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 1-я точка лежит между 3 и 4 точками.", font=("mr_AfronikG", 25, "normal"))
			
		# 9 тип:
		elif is1_24:
			print("Это треугольник.")
			print("1-я точка лежит между 2 и 4 точками.")
			sides = 3
			extra = True
			a = side(x3, y3, x4, y4)
			b = side(x2, y2, x3, y3)
			c = side(x2, y2, x4, y4)
			bd = side(x1, y1, x4, y4)
			ad = side(x1, y1, x2, y2)
			d = side(x3, y3, x2, y2)
			
			xa = x2
			ya = y2
			xb = x4
			yb = y4
			xc = x3
			yc = y3
			xd = x1
			yd = y1
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 2 - 3")
				print("[SYSTEM] Сторона 2: 3 - 4")
				print("[SYSTEM] Сторона 2: 2 - 1 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 1-я точка лежит между 2 и 4 точками.", font=("mr_AfronikG", 25, "normal"))

		# 10 тип:
		elif is2_13:
			print("Это треугольник.")
			print("2-я точка лежит между 1 и 3 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x4, y4)
			b = side(x3, y3, x4, y4)
			c = side(x1, y1, x3, y3)
			bd = side(x2, y2, x1, y1)
			ad = side(x2, y2, x3, y3)
			d = side(x4, y4, x2, y2)
			
			xa = x3
			ya = y3
			xb = x1
			yb = y1
			xc = x4
			yc = y4
			xd = x2
			yd = y2
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 2 - 3")
				print("[SYSTEM] Сторона 2: 3 - 4")
				print("[SYSTEM] Сторона 2: 1 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 2-я точка лежит между 1 и 3 точками.", font=("mr_AfronikG", 25, "normal"))

		# 11 тип:
		elif is2_34:
			print("Это треугольник.")
			print("2-я точка лежит между 3 и 4 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x3, y3)
			b = side(x1, y1, x4, y4)
			c = side(x4, y4, x3, y3)
			bd = side(x2, y2, x3, y3)
			ad = side(x2, y2, x4, y4)
			d = side(x1, y1, x2, y2)
			
			xa = x4
			ya = y4
			xb = x3
			yb = y3
			xc = x1
			yc = y1
			xd = x2
			yd = y2
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 3")
				print("[SYSTEM] Сторона 2: 3 - 2 - 4")
				print("[SYSTEM] Сторона 2: 1 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 2-я точка лежит между 3 и 4 точками.", font=("mr_AfronikG", 25, "normal"))

		# 12 тип:
		elif is2_14:
			print("Это треугольник.")
			print("2-я точка лежит между 1 и 4 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x3, y3)
			b = side(x3, y3, x4, y4)
			c = side(x1, y1, x4, y4)
			bd = side(x2, y2, x1, y1)
			ad = side(x2, y2, x4, y4)
			d = side(x3, y3, x2, y2)
			
			xa = x1
			ya = y1
			xb = x4
			yb = y4
			xc = x3
			yc = y3
			xd = x2
			yd = y2
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 3")
				print("[SYSTEM] Сторона 2: 3 - 4")
				print("[SYSTEM] Сторона 2: 1 - 2 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 2-я точка лежит между 1 и 4 точками.", font=("mr_AfronikG", 25, "normal"))

		# 13 тип:
		elif is3_12:
			print("Это треугольник.")
			print("3-я точка лежит между 1 и 2 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x4, y4)
			b = side(x2, y2, x4, y4)
			c = side(x1, y1, x2, y2)
			bd = side(x1, y1, x3, y3)
			ad = side(x2, y2, x3, y3)
			d = side(x4, y4, x3, y3)
			
			xa = x2
			ya = y2
			xb = x1
			yb = y1
			xc = x4
			yc = y4
			xd = x3
			yd = y3
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 3 - 2")
				print("[SYSTEM] Сторона 2: 2 - 4")
				print("[SYSTEM] Сторона 2: 1 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 3-я точка лежит между 1 и 2 точками.", font=("mr_AfronikG", 25, "normal"))

		# 14 тип:
		elif is3_24:
			print("Это треугольник.")
			print("3-я точка лежит между 2 и 4 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x2, y2)
			b = side(x1, y1, x4, y4)
			c = side(x2, y2, x4, y4)
			bd = side(x2, y2, x3, y3)
			ad = side(x4, y4, x3, y3)
			d = side(x1, y1, x3, y3)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
			
			xa = x
			ya = y
			xb = x
			yb = y
			xc = x
			yc = y
			xd = x
			yd = y
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 2")
				print("[SYSTEM] Сторона 2: 2 - 3 - 4")
				print("[SYSTEM] Сторона 2: 1 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 3-я точка лежит между 2 и 4 точками.", font=("mr_AfronikG", 25, "normal"))
			
		# 15 тип:
		elif is3_14:
			print("Это треугольник.")
			print("3-я точка лежит между 1 и 4 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x2, y2)
			b = side(x2, y2, x4, y4)
			c = side(x1, y1, x4, y4)
			bd = side(x2, y2, x1, y1)
			ad = side(x2, y2, x4, y4)
			d = side(x2, y2, x3, y3)
			
			xa = x4
			ya = y4
			xb = x1
			yb = y1
			xc = x2
			yc = y2
			xd = x3
			yd = y3
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 2")
				print("[SYSTEM] Сторона 2: 2 - 4")
				print("[SYSTEM] Сторона 2: 1 - 3 - 4")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 3-я точка лежит между 1 и 4 точками.", font=("mr_AfronikG", 25, "normal"))

		# 16 тип:
		elif is4_12:
			print("Это треугольник.")
			print("4-я точка лежит между 1 и 2 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x3, y3)
			b = side(x2, y2, x3, y3)
			c = side(x1, y1, x2, y2)
			bd = side(x1, y1, x4, y4)
			ad = side(x2, y2, x4, y4)
			d = side(x4, y4, x3, y3)
			
			xa = x2
			ya = y2
			xb = x1
			yb = y1
			xc = x3
			yc = y3
			xd = x4
			yd = y4
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 4 - 2")
				print("[SYSTEM] Сторона 2: 2 - 3")
				print("[SYSTEM] Сторона 2: 1 - 3")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 4-я точка лежит между 1 и 2 точками.", font=("mr_AfronikG", 25, "normal"))
			
		# 17 тип:
		elif is4_23:
			print("Это треугольник.")
			print("4-я точка лежит между 2 и 3 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x2, y2)
			b = side(x1, y1, x3, y3)
			c = side(x2, y2, x3, y3)
			bd = side(x2, y2, x4, y4)
			ad = side(x3, y3, x4, y4)
			d = side(x4, y4, x1, y1)
			
			xa = x3
			ya = y3
			xb = x2
			yb = y2
			xc = x1
			yc = y1
			xd = x4
			yd = y4
			
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d)) 
				
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 2")
				print("[SYSTEM] Сторона 2: 2 - 4 - 3")
				print("[SYSTEM] Сторона 2: 1 - 3")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 4-я точка лежит между 2 и 3 точками.", font=("mr_AfronikG", 25, "normal"))
			
		# 18 тип:
		elif is4_13:
			print("Это треугольник.")
			print("4-я точка лежит между 1 и 3 точками.")
			sides = 3
			extra = True
			a = side(x1, y1, x2, y2)
			b = side(x2, y2, x3, y3)
			c = side(x1, y1, x3, y3)
			bd = side(x1, y1, x4, y4)
			ad = side(x3, y3, x4, y4)
			d = side(x4, y4, x2, y2)
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
				print("[SYSTEM] bd = "+str(bd))
				print("[SYSTEM] ad = "+str(ad))
				print("[SYSTEM] d = "+str(d))
			
			xa = x3
			ya = y3
			xb = x1
			yb = y1
			xc = x2
			yc = y2
			xd = x4
			yd = y4
			
			if console == 'enable':
				print("\n[SYSTEM] Сторона 1: 1 - 2")
				print("[SYSTEM] Сторона 2: 2 - 3")
				print("[SYSTEM] Сторона 2: 1 - 4 - 3")
			t.up()
			t.goto(-750, 400)
			t.write("Это треугольник. 4-я точка лежит между 1 и 3 точками.", font=("mr_AfronikG", 25, "normal"))

	#Ну если нет - то это 4-угольник.
	else:
		print("Это четырёхугольник.")
		sides = 4
		t.up()
		t.goto(-750, 400)
		t.write("Это четырёхугольник.", font=("mr_AfronikG", 25, "normal"))

	if sides == 3:

		# Вычисление периметра и площади.
		P = int(a+b+c)
		p = float(P/2)
		S = sqrt(p*(p-a)*(p-b)*(p-c))
		S = float(S)
		r = float(S/p)
		R = float((a*b*c)/(4*S))
		S = int(S)

		print("\nПлощадь треугольника равна "+str(S)+".")
		print("Периметр треугольника равен "+str(P)+".")
		print("Радиус вписанной окружности равен "+str(r)+".")
		print("Радиус описанной окружности равен "+str(R)+".")

		t.up()
		t.goto(-750, 360)
		t.write("Площадь треугольника равна "+str(S)+".", font=("mr_AfronikG", 25, "normal"))
		t.goto(-750, 320)
		t.write("Периметр треугольника равен "+str(P)+".", font=("mr_AfronikG", 25, "normal"))
		t.goto(-750, 280)
		t.write("Радиус вписанной окружности равен "+str(r)+".", font=("mr_AfronikG", 25, "normal"))
		t.goto(-750, 240)
		t.write("Радиус описанной окружности равен "+str(R)+".", font=("mr_AfronikG", 25, "normal"))

		# В интерпретаторе Geany можно сворачивать циклы. Для удобства код получения центров окружностей 
		# и их прорисовки я закинул в этот цикл. (Кстати, я пользовался и IDLE, и Geany.)
		if True:

			koef_a = float((b+c)/a)
			bm = float(c/koef_a)
			cm1 = float(a-bm)
			koef_b = float((a+c)/b)
			am = float(c/koef_b)
			cm2 = float(b-am)
			
			# Просто так вычислить центр вписанной окружности не получится.
			# После строки 1437 идёт чертёж треугольника, если интересно.
			#
			#          A
			#     ad  /\            bd+ad = c.
			# c      /  \ am        bm+cm1 = a.
			#     D /    \      b   am+cm2 = b.
			#      /∖_    \ M2
			#  bd /  d∖_   \        d, AM1, BM2 - дополнительные отрезки.
			#    /      ∖__ \ cm2
			#   /__________-∖\      bd, ad - части отрезка c, смежные с a и b
			#   B bm  M1  cm1 C     соответственно и разделённые d.
			#           a
			#
			# xa, ya, xb, yb, xc, yc, xd, yd - x и y точек соответственно A, B, C и D. 
			#
			# Составляем 2 уравнения из 2-х формул длины отрезка по координатам.
			# (xb-xm1)**2 + (yb-ym1)**2 = bm**2
			# (xc-xm1)**2 + (yc-ym1)**2 = cm1**2
			#
			# xb**2 - 2*xb*xm1 + xm1**2 + yb**2 - 2*yb*ym1 + ym1**2 = bm**2   (1)
			# xc**2 - 2*xc*xm1 + xm1**2 + yc**2 - 2*yc*ym1 + ym1**2 = cm1**2  (2)
			# 
			# Вычитаем (2) из (1):
			# xb**2 - xc**2 + 2*xm1*(xc-xb) + yb**2 - yc**2 + 2*ym1*(yc-yb) = bm**2 - cm1**2
			#
			# 2*ym1*(yc-yb) = bm**2 - cm1**2 - xb**2 + xc**2 - yb**2 + yc**2 - 2*xm1*(xc-xb)
			#
			#        bm**2 - cm1**2 - xb**2 + xc**2 - yb**2 + yc**2 - 2*xm1*(xc-xb)
			# ym1 = ----------------------------------------------------------------
			#                                2*yc-2*yb
			#
			# Теперь берём уравнение прямой BC и подставляем в него xm1 и ym1.
			# Напомню: для 1 и 2 точек: (y1-y2)*x+(x2-x1)*y+(x1*y2+x2*y1) = 0
			#
			# (yb-yc)*xm1 + (xc-xb)*ym1 + (xb*yc+xc*yb) = 0
			#
			# (xc-xb)*ym1 = -(xb*yc+xc*yb) - (yb-yc)*xm1
			#
			# (xb-xc)*ym1 = (xb*yc+xc*yb) + (yb-yc)*xm1
			#
			#       (xb*yc+xc*yb) + (yb-yc)*xm1
			# ym1 = ----------------------------
			#                  xb-xc
			#
			# Соединяем!
			#
			# (xb*yc+xc*yb) + (yb-yc)*xm1     bm**2 - cm1**2 - xb**2 + xc**2 - yb**2 + yc**2 - 2*xm1*(xc-xb)
			# ---------------------------- = ----------------------------------------------------------------
			#            xb-xc                                           2*yc-2*yb
			#
			# (2*yc-2*yb)*((xb*yc+xc*yb) + (yb-yc)*xm1) = (xb-xc)*(bm**2 - cm1**2 - xb**2 + xc**2 - yb**2 + yc**2 - 2*xm1*(xc-xb))
			#
			# (2*yc-2*yb)*(yb-yc)*xm1 + (xb-xc)*2*xm1*(xc-xb) = (xb-xc)*(bm**2 - cm1**2 - xb**2 + xc**2 - yb**2 + yc**2) - (2*yc-2*yb)*(xb*yc+xc*yb)
			#
			# Вот результат:
			#
			#{        (xb-xc)*(bm**2 - cm1**2 - xb**2 + xc**2 - yb**2 + yc**2) - (2*yc-2*yb)*(xb*yc+xc*yb)
			#{  xm1 = ------------------------------------------------------------------------------------
			#{                                -2*((yb-yc)**2 + (xc-xb)**2)
			#{
			#{         (xb*yc+xc*yb) + (yb-yc)*xm1
			#{  ym1 = -----------------------------
			#{                   xb-xc
			
			xm1 = ((xb-xc)*(bm**2 - cm1**2 - xb**2 + xc**2 - yb**2 + yc**2) - (2*yc-2*yb)*(xb*yc+xc*yb))/(-2*((yb-yc)**2 + (xc-xb)**2))
			
			ym1 = ((xb*yc+xc*yb) + (yb-yc)*xm1)/(xb-xc)
			
			print('xm1 =', xm1)
			print('ym1 =', ym1)
			'''t.up()
			sleep(1)
			t.goto(xb, yb)
			sleep(1)
			t.down()
			t.goto(xm1, ym1)
			sleep(1)
			t.up()'''

		# Вычисление углов.
		# Вот чертёж треугольника, чтобы не возникало вопросов.
		#
		#          A
		#    ad   /\      Точка A напротив стороны a. a=BC
		#        /  \     Точка B напротив стороны b. b=AC
		#     D /∖_  \ b  Точка C напротив стороны c. c=AB
		#      /  d∖_ \
		# bd  /     ∖_ \  При наличии доп. отрезка, d=CD, D принадлежит AB,
		#    /__________\
		#   B    a       C
		#

		# Переменные для углов BAC, ABC, ACB, ADC, BDC, ACD и BCD:
		# angleA, angleB, angleC, angleD-a, angleD-b, angleC-a и angleC-b.

		m_angleA = (b**2+c**2-a**2)/(2*b*c)
		m_angleB = (c**2+a**2-b**2)/(2*a*c)
		m_angleC = (a**2+b**2-c**2)/(2*a*b)
		angleA = acos(m_angleA)
		angleA = degrees(angleA)
		angleA = int(angleA)
		angleA = float(angleA)
		angleA = int(angleA)
		
		angleB = acos(m_angleB)
		angleB = degrees(angleB)
		angleB = int(angleB)
		angleB = float(angleB)
		angleB = int(angleB)
		
		angleC = acos(m_angleC)
		angleC = degrees(angleC)
		angleC = int(angleC)
		angleC = float(angleC)
		angleC = int(angleC)
		
		if get('console')[0] == 'enable':
			print("\nУгол A равен "+str(angleA)+"градусов.")
			print("Угол B равен "+str(angleB)+"градусов.")
			print("Угол C равен "+str(angleC)+"градусов.")

		# extra = True, когда имеется дополнительный отрезок. False - когда нет.
		if extra:
			m_angle__D = (d**2+ad**2-b**2)/(2*d*ad)
			angle__D = acos(m_angle__D)
			angle__D = int(degrees(angle__D))
			angle__D = float(degrees(angle__D))
			angle__D = int(degrees(angle__D))
			
			print("\nПрисутствует дополнительный отрезок.")
			t.goto(-750, 200)
			t.write("Присутствует дополнительный отрезок.", font=("mr_AfronikG", 25, "normal"))
			if (bd == ad) and (bd/a == ad/b):
				t.goto(-750, 160)
				print("Это и медиана, и биссектриса, и высота.")
				t.write("Это и медиана, и биссектриса, и высота.", font=("mr_AfronikG", 25, "normal"))
			elif ad == bd:
				t.goto(-750, 160)
				print("Это медиана.")
				t.write("Это медиана.", font=("mr_AfronikG", 25, "normal"))
			elif bd/a == ad/b:
				t.goto(-750, 160)
				print("Это биссектриса.")
				t.write("Это биссектриса.", font=("mr_AfronikG", 25, "normal"))
			elif angle__D == 90:
				t.goto(-750, 160)
				print("Это высота.")
				t.write("Это высота.", font=("mr_AfronikG", 25, "normal"))
			j = input("НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ")
			continue

		else:
			print("\nОтсутствует дополнительный отрезок.")
			t.goto(-750, 200)
			t.write("Отсутствует дополнительный отрезок.", font=("mr_AfronikG", 25, "normal"))
			j = input("НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ")
			continue	

	# Если это четырёхугольник.
	elif sides == 4:
		# Всё ещё два варианта. Лишняя точка может быть внутри треугольника, и тогда капут.
		# Но есть способ: вот такие формулы я нашёл на CyberForum.ru. И, эти хоть какое-то
		# значение равно 0, то точка лежит на стороне, но это УЖЕ определено как треугольник.
		
		nowpiliat = 0
		# nowpiliat stays for Number Of Which Point Is Located Inside A Triangle.
		if (x2-x1)*(y3-y2) - (x3-x2)*(y2-x1)>=0 and (x3-x1)*(y4-y3) - (x4-x3)*(y3-y1)>=0 and (x4-x1)*(y2-y4) - (x2-x4)*(y4-y1)>=0:
			print('1, >=')
			nowpiliat = 1
		if (x2-x1)*(y3-y2) - (x3-x2)*(y2-x1)<=0 and (x3-x1)*(y4-y3) - (x4-x3)*(y3-y1)<=0 and (x4-x1)*(y2-y4) - (x2-x4)*(y4-y1)<=0:
			print('1, <=')
			nowpiliat = 1

		if (x1-x2)*(y3-y1) - (x3-x1)*(y1-x2)>=0 and (x3-x2)*(y4-y3) - (x4-x3)*(y3-y2)>=0 and (x4-x2)*(y1-y4) - (x1-x4)*(y4-y2)>=0:
			print('2, >=')
			nowpiliat = 2
		if (x1-x2)*(y3-y1) - (x3-x1)*(y1-x2)<=0 and (x3-x2)*(y4-y3) - (x4-x3)*(y3-y2)<=0 and (x4-x2)*(y1-y4) - (x1-x4)*(y4-y2)<=0:
			print('2, <=')
			nowpiliat = 2

		if (x2-x3)*(y1-y2) - (x1-x2)*(y2-x3)>=0 and (x1-x3)*(y4-y1) - (x4-x1)*(y1-y3)>=0 and (x4-x3)*(y2-y4) - (x2-x4)*(y4-y3)>=0:
			print('3, >=')
			nowpiliat = 3
		if (x2-x3)*(y1-y2) - (x1-x2)*(y2-x3)<=0 and (x1-x3)*(y4-y1) - (x4-x1)*(y1-y3)<=0 and (x4-x3)*(y2-y4) - (x2-x4)*(y4-y3)<=0:
			print('3, <=')
			nowpiliat = 3

		if (x2-x4)*(y1-y2) - (x1-x2)*(y2-x4)>=0 and (x1-x4)*(y3-y1) - (x3-x1)*(y1-y4)>=0 and (x3-x4)*(y2-y3) - (x2-x3)*(y3-y4)>=0:
			print('4, >=')
			nowpiliat = 4
		if (x2-x4)*(y1-y2) - (x1-x2)*(y2-x4)<=0 and (x1-x4)*(y3-y1) - (x3-x1)*(y1-y4)<=0 and (x3-x4)*(y2-y3) - (x2-x3)*(y3-y4)<=0:
			print('4, <s=')
			nowpiliat = 4
		
		if nowpiliat == 4:
			print("4 точка находится внутри четырёхугольника.")
			sides = 3
			extra = False
			a = side(x1, y1, x2, y2)
			b = side(x1, y1, x3, y3)
			c = side(x2, y2, x3, y3)
			xa = x1
			ya = y1
			xb = x2
			yb = y2
			xc = x3
			yc = y3
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			t.up()
			t.goto(-750, 360)
			t.write("4 точка находится внутри четырёхугольника.", font=("mr_AfronikG", 25, "normal"))
			
		elif nowpiliat == 3:
			print("3 точка находится внутри четырёхугольника.")
			sides = 3
			extra = False
			a = side(x1, y1, x2, y2)
			b = side(x1, y1, x4, y4)
			c = side(x2, y2, x4, y4)
			xa = x1
			ya = y1
			xb = x2
			yb = y2
			xc = x4
			yc = y4
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			t.up()
			t.goto(-750, 360)
			t.write("3 точка находится внутри четырёхугольника..", font=("mr_AfronikG", 25, "normal"))
			
		elif nowpiliat == 2:
			print("2 точка находится внутри четырёхугольника.")
			sides = 3
			extra = False
			a = side(x1, y1, x3, y3)
			b = side(x1, y1, x4, y4)
			c = side(x3, y3, x4, y4)
			xa = x1
			ya = y1
			xb = x3
			yb = y3
			xc = x4
			yc = y4
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			t.up()
			t.goto(-750, 360)
			t.write("2 точка находится внутри четырёхугольника.", font=("mr_AfronikG", 25, "normal"))
			
		elif nowpiliat == 1:
			print("1 точка находится внутри четырёхугольника.")
			sides = 3
			extra = False
			a = side(x2, y2, x3, y3)
			b = side(x2, y2, x4, y4)
			c = side(x3, y3, x4, y4)
			xa = x2
			ya = y2
			xb = x3
			yb = y3
			xc = x4
			yc = y4
			if get('console')[0] == 'enable':
				print("\n[SYSTEM] a = "+str(a))
				print("[SYSTEM] b = "+str(b))
				print("[SYSTEM] c = "+str(c))
			t.up()
			t.goto(-750, 360)
			t.write("1 точка находится внутри четырёхугольника.", font=("mr_AfronikG", 25, "normal"))
			
		a_12 = y1-y2
		b_12 = x2-x1
		c_12 = x1*y2+x2*y1

		a_14 = y1-y4
		b_14 = x4-x1
		c_14 = x1*y4+x4*y1

		a_23 = y2-y3
		b_23 = x3-x2
		c_23 = x2*y3+x3*y2

		a_34 = y3-y4
		b_34 = x4-x3
		c_34 = x3*y4+x4*y3
		
		is_trap = False
		if (a_12*b_34 == a_34*b_12) and (a_14*b_23 != a_23*b_14):
			is_trap = True
			kkqww = 1423
		if (a_12*b_34 != a_34*b_12) and (a_14*b_23 == a_23*b_14):
			is_trap = True
			kkqww = 1234
			
		type = None
			
		if l12 == l34 and l23 == l14:
			print("Это параллелограмм.")
			type = 'параллелограмм'
			if l13 == l24:
				print("Это прямоугольник.")
				type = 'прямоугольник'
				if l12 == l23:
					print("Это квадрат.")
					type = 'квадрат'
			if l12 == l23:
				print("Это ромб")
				type = 'ромб'
			
		if is_trap:
			print("Это трапеция.")
			type = 'трапеция'
			if kkqww == 1423:
				if l14 == l23:
					type = 'равнобедренная трапеция'
					print("Равнобедренная.")
				elif a_14*b_23 == -1*a_23*b_14:
					type = 'прямоугольная трапеция'
					print("Прямоугольная трапеция")
			if kkqww == 1234:
				if l12 == l34:
					type = 'равнобедренная трапеция'
					print("Равнобедренная.")
				elif a_12*b_34 == -1*a_34*b_12:
					type = 'прямоугольная трапеция'
					print("Прямоугольная трапеция")
			
		if type != None:
			t.down()
			t.goto(-750, 360)
			t.write("Это "+type+".", font=("mr_AfronikG", 25, "normal"))
		
		# Чтобы вычислить центр вписанной окружности, нужно сначала доказать,
		# что её можно вписать. То есть, доказать, что суммы противоположных 
		# сторон равны.
		if l12+l34 == l23+l14:
			pass
			# Теперь. Центр вписанной окружности лежит на пересечении биссектрис 
			# смежных углов четырёхугольника.
			# Возьмём 1 и 2 точки.
			# Тогда биссектриса 1 точки лежит между отрезками 14 и 12,
			# а биссектриса 2 точки леэит между отрезками 12 и 23.
			#
			# Вычисляем уравнение прямой для биссектрисы 1 точки:
			#
			# a1*x + b1*y + c1      a2*x + b2*y + c2
			# ---------------- = +- ----------------
			# \/a1**2 + b1**2       \/a2**2 + b2**2
			#
			# (a1*x + b1*y + c1)**2   +- (a2*x + b2*y + c2)**2
			# --------------------- = ------------------------
			#     a1**2 + b1**2             a2**2 + b2**2
			#
			# (a2**2 + b2**2)*(a1*x + b1*y + c1)**2 = +-(a1**2 + b1**2)*(a2*x + b2*y + c2)**2
			#
			# Разбиваем на два случая:
			#
			# 1) +
			# (a2**2 + b2**2)*(a1*x + b1*y + c1)**2 = (a1**2 + b1**2)*(a2*x + b2*y + c2)**2
			#
			# 
		
		j = input("НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ")
		continue
	else:
		j = input("НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ")
		continue


# Краткое описание предыдущих версий.
# Я добавлял сюда записи всё время создания программы.

# Преальфа!
# Создал базовый цикл, ввод, получение координат,
# Парочку команд для входа-выхода, добавил черепашку.

# Альфа-версия 1.0!
# Добавил много различных выводов-вводов, уже построение
# на плоскости.

# Альфа-версия 1.1!
# Команды ушли куда-то далеко, чуть ли не язык программирования.
# Я создал базовый подгон фигур к центру, но работает через раз.
# Также всякие инпуты-континьюты и т.п.

# Альфа-версия 1.2!
# Я создал режим авто-перемещения. Также в разработке режим авто-
# -увеличения/уменьшения. Программа сама определяла, как увеличить фигуру.
# Также добавлены всякие настройки в команды.

# Альфа-версия 1.4!
# Я тут много сделал. Можно версию 1.3 пропустить.
# Программа уже на 400 строк. Я доделал режим авто-масштабирования.
# А также я решил добавить считывание данных из файла. Давно я
# этого не делал. Это будет сложно. Программа считывает определённый файл
# и создаёт из него словарь. Нужно будет почитать про словари.

# Альфа-версия 1.4.7!
# Под-версия. Я доделал работу с файлом, то есть оттуда уже считываются данные.
# Но со словарём проблемы.

# Бета-версия 1.5!
# Добавлено:
# - Считывание файла, создание словаря, предупреждение ошибок и создание пустых
# файлов.
# - Возможность выводить на холст различные символы. Добавлено два шрифта, но и
# без них программа всё равно работает.
# - Начало добавления главных программ. Добавлено определение точки, отрезка.

# Бета-версия 1.6!
# С файлом я разобрался. Случайно сделал защиту от дурачка. Создал изменение цветов,
# скорости, заполнения и многих других настроек. Вся помощь - !help.

# Бета-версия 1.7!
# Добавлено кривое определение треугольника. Есть 18 вариантов построения треугольника,
# расписаны все.
# Изменены все команды "под файл". То есть они все редактируют не внутрипрограммные
# переменные, а значения файла. Это очень сложно.

# Бета-версия 1.8!
# Добавлены функции change и get. Удобны при работе с файлом.
# Добавлен вывод на черепаший холст значений, полученных в программе.
# Полностью переписано определение треугольника. v2.0

# Бета-версия 1.9!
# Добавлена функция side, определяющая сторону по 4-м координатам 2-х точек.
# Изменено определение треугольника на v4.0. Грядёт масштабное обновление,
# что бы сделать...

# Версия 1.10!
# Добавлено:
# - Полный перевод всей программы на русский язык.
# - Перевод всех системных выводов на русский язык.
# - Подробные комментарии всей программы.
# - Улучшенная работа с файлом. Все ошибки предугаданы.
# - В команде появился QA-тестер, поэтому исправлено
# большое количество ошибок, багов и киллерфич.
# - Программа разрослась на >1500 строк!
# - Мы выходим из беты! В архиве появились два шрифта.

# Версия 1.11!
# Обновления продолжают выходить.
# Мы перешагнули рубеж в 2000 строк!
# - Для каждого из 18 случаев треугольников расписаны свои переменные и оптимизированы
# для дальнейшей работы.
# - Ненадолго появился второй цикл, но это было исправлено. Правда, теперь весь код на
# 4 пробела выше. Но ошибок никаких не возникает.
# - Исправлены ошибки с различными параметрами точек и отрезков. Различные случаи
# распределены по программе, чтобы не возникло подобных ошибок.
# Следующее обновление выйдет после Университетской Субботы!
# Upd: да, задержался. Как 3000 строк будет, как переборю вписанную окружность -
# - выйдет обновление, обещаю.
