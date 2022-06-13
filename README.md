# TimetableCNF
Данная система предназначена для построения и предобработки КНФ, соответствующей задаче составления расписания с определенными заданными параметрами.

Система включает в себя 4 файла:
- Файлы `W1.py` и `W2.py` представляют из себя тестовые экземпляры входных данных.
- Файл `CNF_functions.py` содержит функции, используемые для вывода промежуточных результатов, а также добавления в КНФ дизъюнктов соответствующей полярности и длины.
- Файл `TimetableCNF.py` является основным. Его запуск инициирует построение КНФ, соответсвующей задаче составления расписания из `W1.py` или `W2.py` в зависисмости от выбранной опции, с последующим сохранением полученной формулы в формате DIMACS.


При запуске основного файла `TimetableCNF.py` необходимо в качестве второго аргумента передать путь к текстовому файлу, в который в результате работы программы будет записана КНФ в формате DIMACS.

