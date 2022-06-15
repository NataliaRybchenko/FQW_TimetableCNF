# TimetableCNF
Данная система предназначена для построения и предобработки КНФ, соответствующей задаче составления расписания с определенными заданными параметрами.

Система включает в себя 4 файла:
- Файлы `w1_6_7.py`, `w1_6_14.py`, `w1_24_7.py` и `w2_12_7.py` представляют из себя тестовые экземпляры входных данных.
- Файл `CNF_functions.py` содержит функции, используемые для вывода промежуточных результатов, а также добавления в КНФ дизъюнктов соответствующей полярности и длины.
- Файл `TimetableCNF.py` является основным. Его запуск инициирует построение КНФ, соответсвующей задаче составления расписания из `w1_6_7.py`, `w1_6_14.py`, `w1_24_7.py` или `w2_12_7.py` в зависисмости от заданного аргумента, с последующим сохранением полученной формулы в формате DIMACS.


При запуске основного файла `TimetableCNF.py` необходимо в качестве второго аргумента передать путь к файлу с данными (`w1_6_7.py`, `w1_6_14.py`, `w1_24_7.py` или `w2_12_7.py`), а в качестве третьего — путь к текстовому файлу, в который в результате работы программы будет записана КНФ в формате DIMACS.

