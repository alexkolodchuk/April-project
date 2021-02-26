# Апрельский проект 2020
Создание графического приложения на Python, строящего двумерные геометрические фигуры по заданным координатам в плоскости и сообщающего о них обширные сведения, свойства.

Сложность заключалась в разработке умного масштабирования изображения геометрической фигуры на плоскости, построении интерфейса внутренней командной строки программы.

Над проектом работало 5 человек (5 учеников кафедры с углубленным изучением информатики и информационных технологий Предуниверситария НИЯУ МИФИ). Я возглавлял проект и выполнил 70-80% от общей работы (3500±200 строк кода на языке программирования Python 3), разрабатывал все аспекты и концепты работы приложения. 

===================================================================================

ОРИГИНАЛЬНАЯ СУТЬ ЗАДАЧИ заключалась в этом:

Даны координаты 4-х точек. Выяснить:
1) какая фигура получится, если соединить все точки ?
2) в каких четвертях плоскости лежит фигура?
Пример входных данных:
1 2
3 3
4 7
5 5
Пример выходных данных:
четырехугольник
1 четверть

2) является ли фигура выпуклой? (для четырехугольника)
3) найти площадь и периметр фигуры
4) можно ли описать/вписать окружность вокруг этой фигуры? Каков радиус
и координаты центра?
5) если получился отрезок - уравнение прямой, длину отрезка и насколько
близко разбиение отрезка точками (одной и другой) к золотому сечению (т.е.
на какое расстояние нужно было бы сдвинуть точки, чтобы они делили
отрезок в соответствии с золотым сечением)
6) если получился треугольник - вид по сторонам и углам (равносторонний,
равнобедренный, разносторонний; остроугольный, прямоугольный,
тупоугольный); является ли дополнительный отрезок высотой, медианой,
биссектрисой?
7) если получился четырехугольник - какой: квадрат?, ромб?
параллелограмм? трапеция? равнобедренная? и т.д.
8) есть ли у фигуры оси симметрии? цент симметрии? Уравнение оси,
координаты центра?

===================================================================================

Задача давалась на 1 месяц, для работы команде. Наша команда дополнила проект следующими аспектами:

1. Графическое отображение фигур
2. Функции умного масштабирования, умного подгона расположения на экране
3. Интерфейс командной строки, дающей возможность настройки графического и консольного интерфейса (далее приведено).
4. Сохранение настроек интерфейса, истории входных данных в файл, анализ данных, работа с файлом.

Суммарно программа составляет 2911 строк кода на языке программирования Python 3.

===================================================================================

Патч-лист:

Преальфа!
Создал базовый цикл, ввод, получение координат,
Парочку команд для входа-выхода, добавил черепашку.

Альфа-версия 1.0!
Добавил много различных выводов-вводов, уже построение на плоскости.

Альфа-версия 1.1!
Команды ушли куда-то далеко, чуть ли не язык программирования.
Я создал базовый подгон фигур к центру, но работает через раз.
Также всякие инпуты-континьюты и т.п.

Альфа-версия 1.2!
Я создал режим авто-перемещения. Также в разработке режим авто-увеличения/уменьшения. Программа сама определяла, как увеличить фигуру. Также добавлены всякие настройки в команды.

Альфа-версия 1.4!
Я тут много сделал. Можно версию 1.3 пропустить.
Программа уже на 400 строк. Я доделал режим авто-масштабирования.
А также я решил добавить считывание данных из файла. Давно я этого не делал. Это будет сложно. Программа считывает определённый файл и создаёт из него словарь. Нужно будет почитать про словари.

Альфа-версия 1.4.7!
Под-версия. Я доделал работу с файлом, то есть оттуда уже считываются данные.
Но со словарём проблемы.

Бета-версия 1.5!
Добавлено:
- Считывание файла, создание словаря, предупреждение ошибок и создание пустых
файлов.
- Возможность выводить на холст различные символы. Добавлено два шрифта, но и без них программа всё равно работает.
- Начало добавления главных программ. Добавлено определение точки, отрезка.

Бета-версия 1.6!
С файлом я разобрался. Случайно сделал защиту от дурачка. Создал изменение цветов,
скорости, заполнения и многих других настроек. Вся помощь - !help.

Бета-версия 1.7!
Добавлено кривое определение треугольника. Есть 18 вариантов построения треугольника,
расписаны все.
Изменены все команды "под файл". То есть они все редактируют не внутрипрограммные
переменные, а значения файла. Это очень сложно.

Бета-версия 1.8!
Добавлены функции change и get. Удобны при работе с файлом.
Добавлен вывод на черепаший холст значений, полученных в программе.
Полностью переписано определение треугольника. v2.0

Бета-версия 1.9!
Добавлена функция side, определяющая сторону по 4-м координатам 2-х точек.
Изменено определение треугольника на v4.0. Грядёт масштабное обновление, что бы сделать...

Версия 1.10!
Добавлено:
- Полный перевод всей программы на русский язык.
- Перевод всех системных выводов на русский язык.
- Подробные комментарии всей программы.
- Улучшенная работа с файлом. Все ошибки предугаданы.
- В команде появился QA-тестер, поэтому исправлено большое количество ошибок, багов и киллерфич.
- Программа разрослась на >1500 строк!
- Мы выходим из беты! В архиве появились два шрифта.

Версия 1.11!
Обновления продолжают выходить.
Мы перешагнули рубеж в 2000 строк!
- Для каждого из 18 случаев треугольников расписаны свои переменные и оптимизированы
для дальнейшей работы.
- Ненадолго появился второй цикл, но это было исправлено. Правда, теперь весь код на
4 пробела выше. Но ошибок никаких не возникает.
- Исправлены ошибки с различными параметрами точек и отрезков. Различные случаи
распределены по программе, чтобы не возникло подобных ошибок.
Следующее обновление выйдет после Университетской Субботы!
