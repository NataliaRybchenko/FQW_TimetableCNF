from itertools import combinations

# 6 временных единиц (1 неделя, 3 дня)
#     2 пары в 1 день 
#     2 пары во 2 день 
#     2 пары в 3 день
# 7 групп
#     2 группы
#     1 поток
#     4 подгруппы
# 5 занятий
#     2 по 1 предмету (лекция и практика)
#     2 по 2 предмету (лекция и практика)
#     1 по 3 предмету (практика по подгруппам)
# 4 преподавателя 
#     1 ведет по 1 предмету лекцию и практику
#     2 ведет по 2 предмету лекцию и практику
#     3-4 ведет по 3 предмету практику по подгруппам
# Учебный план (для обеих групп) 
#     2 лекции (1 и 2 преподаватели 1 и 2 предметы, соответсвенно)
#     2 практики по группам (1 и 2 преподаватели 1 и 2 предметы, соответсвенно)
#     1 практика по подгруппам (3 и 4 преподаватели)


# Функция δ(массив, индексы)
# Возвращает 1, если элемент массива с соответсвующим индексом является обязательным требованием, 0 в противном случае
# Установим в 1, чтобы выполнение всех требований было обязательным
def delta(Arr, idx):
    return 1

W_num = 1
D_num = 3
C_num = 2
U_num = W_num*D_num*C_num

G_num = 2
F_num = 1
P_num = 4
N_num = G_num + F_num + P_num

# Принадлежность групп подгруппам ===========================
GF = []
for g in range(G_num):
    GF_g = []
    for f in range(F_num):
        GF_g.append(0)
    GF.append(GF_g)
GF[0][0] = 1
GF[1][0] = 1
print ('GF:')
for g in range(G_num):
    for f in range(F_num):
        print (GF[g][f], end =' ')
    print (end = '\n')
print ('_____________________')


# Принадлежность подгрупп группам ============================
GP = []
for g in range(G_num):
    GP_g = []
    for p in range(P_num):
        GP_g.append(0)
    GP.append(GP_g)
GP[0][0] = 1
GP[0][1] = 1
GP[1][2] = 1
GP[1][3] = 1
print ('GP:')
for g in range(G_num):
    for p in range(P_num):
        print (GP[g][p], end =' ')
    print (end = '\n')
print ('_____________________')


# Численность групп, потоков и подгрупп =======================
QN = [15, 18, 33, 7, 8, 9, 9]
print ('QN = ', QN)
print ('_____________________')


# Ограничение сверху на количество пар в день у каждой из групп
G_maxC = []
for g in range(G_num):
    G_maxC.append(0)
G_maxC = [2, 2]
print ('G_maxC = ', G_maxC)
print ('_____________________')

# ========================================================================================

S_num = 3
K_num = 2
Z_num = 5
Z = [[0,0], [0,1], [1,0], [1,1], [2,1]]
print ('Z = ', Z)
print ('_____________________')


# Количество пар у группы n по занятию z в неделю w =============
QNZW = []
for n in range(N_num):
    QZW = []
    for z in range(Z_num):
        QW = []
        for w in range(W_num):
            QW.append(0)
        QZW.append(QW)
    QNZW.append(QZW)
# Практики по группам
QNZW[0][1][0] = 1
QNZW[0][3][0] = 1
QNZW[1][1][0] = 1
QNZW[1][3][0] = 1

# Лекции по потокам
QNZW[2][0][0] = 1
QNZW[2][2][0] = 1

# Практики по подгруппам
QNZW[3][4][0] = 1
QNZW[4][4][0] = 1
QNZW[5][4][0] = 1
QNZW[6][4][0] = 1

print ('QNZW:')
for n in range(N_num):
    print ('n =', n, end = '| ')
    for w in range(W_num):
        for z in range(Z_num):
            print (QNZW[n][z][w], end =' ')
        print (end = '\n')
print ('_____________________')


# Запрет на проведение у группы занятий по дисциплине-виду в определенную единицу времени
NSK_U = []
for n in range(N_num):
    SK_U = []
    for s in range(S_num):
        K_U = []
        for k in range(K_num):
            _U = []
            for u in range(U_num):
                _U.append(1)
            K_U.append(_U)
        SK_U.append(K_U)
    NSK_U.append(SK_U)
# Запрет на проведения лекций в конце дня (на вторых парах)
NSK_U[2][0][0][1] = 0
NSK_U[2][0][0][3] = 0
NSK_U[2][0][0][5] = 0

NSK_U[2][1][0][1] = 0
NSK_U[2][1][0][3] = 0
NSK_U[2][1][0][5] = 0


# ========================================================================================

R_num = 5
B_num = 1

# Вместимость аудиторий =============================================
QR = [10, 12, 17, 18, 35]
print ('QR = ', QR)
print ('_____________________')

# Принадлежность аудитории корпусу
RB = []
for r in range(R_num):
    Btmp = []
    for b in range(B_num):
        Btmp.append(0)
    RB.append(Btmp)
RB[0][0] = 1
RB[1][0] = 1
RB[2][0] = 1
RB[3][0] = 1
RB[4][0] = 1
print ('RB:')
for r in range(R_num):
    for b in range(B_num):
        print (RB[r][b], end =' ')
    print (end = '\n')
print ('_____________________')

# Запрет проведения занятий по дисциплине-виду в некоторых аудиториях
SK_R = []
for s in range(S_num):
    K_R = []
    for k in range(K_num):
        _R = []
        for r in range(R_num):
            _R.append(1)
        K_R.append(_R)
    SK_R.append(K_R)
# Не проводить практики в лекционной
SK_R[0][1][4] = 0
SK_R[1][1][4] = 0
SK_R[2][1][4] = 0
print ('SK_R:')
for s in range(S_num):
    for r in range(R_num):
        for k in range(K_num):
            print (SK_R[s][k][r], end =' ')
        print (end = ' ')
    print (end = '\n')
print ('_____________________')


# Запрет проведения занятий по дисциплине-виду в некоторых корпусах ==
SK_B = []
for s in range(S_num):
    K_B = []
    for k in range(K_num):
        _B = []
        for b in range(B_num):
            _B.append(1)
        K_B.append(_B)
    SK_B.append(K_B)
print ('SK_B:')
for s in range(S_num):
    for b in range(B_num):
        for k in range(K_num):
            print (SK_B[s][k][b], end =' ')
        print (end = ' ')
    print (end = '\n')
print ('_____________________')


# ========================================================================================

E_num = 4

# Требования преподавателей не назначать занятия на определенные пары ===========
E_U = []
for e in range(E_num):
    U = []
    for u in range(U_num):
        U.append(0)
    E_U.append(U)

E_U[0] = [1, 1,   0, 0,   1, 1]
E_U[1] = [0, 1,   1, 1,   0, 0]
E_U[2] = [0, 0,   0, 1,   1, 1]
E_U[3] = [1, 1,   0, 1,   1, 0]

print ('E_U:')
for e in range(E_num):
    for u in range(U_num):
        print (E_U[e][u], end =' ')
    print (end = '\n')
print ('_____________________')


# Назначение преподавателя на проведение занятий у группы n по дисциплине s вида k
NSKE = []
for n in range(N_num):
    SKE = []
    for s in range(S_num):
        KE = []
        for k in range(K_num):
            Etmp = []
            for e in range(E_num):
                Etmp.append(0)
            KE.append(Etmp)
        SKE.append(KE)
    NSKE.append(SKE)
# Практики по группам
NSKE[0][0][1][0] = 1
NSKE[0][1][1][1] = 1
NSKE[1][0][1][0] = 1
NSKE[1][1][1][1] = 1

# Лекции
NSKE[2][0][0][0] = 1
NSKE[2][1][0][1] = 1

# Практики по подгруппам
NSKE[3][2][1][2] = 1
NSKE[4][2][1][3] = 1
NSKE[5][2][1][2] = 1
NSKE[6][2][1][3] = 1


# Ограничение сверху на количество пар у преподавателья е в день d на неделе w
EWD_maxC = []
for e in range(E_num):
    WD_maxC = []
    for w in range(W_num):
        D_maxC = []
        for d in range(D_num):
            D_maxC.append(2)
        WD_maxC.append(D_maxC)
    EWD_maxC.append(WD_maxC)
# У 0 преподавателя во 2 день максимум 1 пара
# У 2 преподавателя во 2 день максимум 1 пара
# У 3 преподавателя в 0 день максимум 1 пара
EWD_maxC[0][0][2] = 1
EWD_maxC[2][0][2] = 1
EWD_maxC[3][0][0] = 1

print ('EWD_maxC:')
for e in range(E_num):
    for w in range(W_num):
        for d in range(D_num):
            print (EWD_maxC[e][w][d], end =' ')
        print (end = ' ')
    print (end = '\n')
print ('____________________________________________________________')


# ========================================================================================

# Массив переменных
X = list()
for u in range(U_num): 
    for r in range(R_num): 
        for n in range(N_num): 
            for e in range(E_num): 
                for z in range(Z_num):
                    X.append(str('Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)))

CNF = set()
file = open('/home/nata/1.SPBU_homework/ВКР/DIMACS.txt', 'w')

# ЗАПИШЕМ В ФАЙЛ ДИЗЪЮНКТЫ, СООТВЕТСТВУЮЩИЕ ОГРАНИЧЕНИЯМ 
# С целью увеличения эффективности, сперва добавим в КНФ дизъюнкты, состоящие из 1 и 2 переменных.

# Ограничение 5 =============================================================================

for u in range(U_num):
    for r in range (R_num):
        for n in range(N_num):
            if (QR[r]/QN[n] < 1):
                for e in range(E_num):
                    for z in range(Z_num):
                        DIS = set()
                        DIS.add('-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z))
                        DIS = frozenset(DIS)
                        CNF.add(DIS)

print ('+ 5: len(CNF) = ', len(CNF))

# Ограничение 8 =============================================================================

for w in range(W_num):
    for d in range(D_num):
        for c in range(C_num):
            u = w*D_num + d*C_num + c
            for r in range(R_num):
                for b in range(B_num):
                    if RB[r][b] == 1:
                        for n in range(N_num):
                            for e in range(E_num):
                                for s in range(S_num):
                                    for k in range(K_num):
                                        sk = [s, k]
                                        for z_idx in range(Z_num):
                                            if Z[z_idx] == sk:
                                                z = z_idx
                                                # print('s = ', s, ' k = ', k, ' z = ', z)
                                                if (NSKE[n][s][k][e] * E_U[e][u] * NSK_U[n][s][k][u] * SK_R[s][k][r] * SK_B[s][k][b] < 1):
                                                    DIS = set()
                                                    DIS.add('-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z))
                                                    DIS = frozenset(DIS)
                                                    CNF.add(DIS)

print ('+ 8: len(CNF) = ', len(CNF))

# Ограничения 1-4 ============================================================================        

X = list()
for u in range(U_num):
    for r in range(R_num):
        for n in range(N_num):
            for e in range(E_num):
                for z in range(Z_num):
                    oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                    oper_set = set()
                    oper_set.add(oper)
                    if oper_set not in CNF:
                        idxs = list()
                        idxs.append(u)
                        idxs.append(r)
                        idxs.append(n)
                        idxs.append(e)
                        idxs.append(z)
                        X.append(idxs)
Cnk = combinations(X, 2)
for Cnk_i in Cnk:
    if Cnk_i[0][0] == Cnk_i[1][0] and (Cnk_i[0][1] == Cnk_i[1][1] or Cnk_i[0][2] == Cnk_i[1][2] or Cnk_i[0][3] == Cnk_i[1][3]):
        oper1 = '-Xurnez_' + str(Cnk_i[0][0]) + '_' + str(Cnk_i[0][1]) + '_' + str(Cnk_i[0][2]) + '_' + str(Cnk_i[0][3]) + '_' + str(Cnk_i[0][4])
        oper2 = '-Xurnez_' + str(Cnk_i[1][0]) + '_' + str(Cnk_i[1][1]) + '_' + str(Cnk_i[1][2]) + '_' + str(Cnk_i[1][3]) + '_' + str(Cnk_i[1][4])
        DIS = set()
        DIS.add(oper1)
        DIS.add(oper2)
        DIS = frozenset(DIS)
        CNF.add(DIS)
        
print ('+ 1-4: len(CNF) = ', len(CNF))

# Начиная с этого момента длина дизъюнктов зависит от других параметров задачи => 
# При их добавлении необходимо учитывать возможность поглощения как старыми дизъюнктами новых, так и новыми дизъюнктами старых.

# Ограничение 6 =============================================================================

for n in range(N_num):
    for z in range(Z_num):
        # X1 - все Х с соответсвующими n и z
        # X2 - все -Х с соответсвующими n и z, еще не вошедшие в КНФ
        X1 = list()
        X2 = list()
        for u in range(U_num):
            for r in range(R_num):
                for e in range(E_num):
                    oper_1 = 'Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                    X1.append(oper_1)
                    oper_2 = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                    set_oper2 = set()
                    set_oper2.add(oper_2)
                    if set_oper2 not in CNF:
                        X2.append(oper_2)
        SUM_QNZW = 0
        for w in range(W_num):
            SUM_QNZW = SUM_QNZW + QNZW[n][z][w]
        
        # Добавляем дизъюнкты, состоящие из переменных без отрицаний. 
        # Поскольку все добавленные ранее дизъюнкты состоят исключительно из переменных с отрицанием, необходимости в проверке поглощения нет.
        in_dis_num1 = U_num*R_num*E_num - SUM_QNZW + 1
        Cnk1 = combinations(X1, in_dis_num1)
        for Cnk1_i in Cnk1:
            DIS = set(Cnk1_i)
            DIS = frozenset(DIS)
            CNF.add(DIS)

        # Добавляем дизъюнкты, состоящие из переменных с отрицаниями
        in_dis_num2 = SUM_QNZW + 1
        # in_dis_num2 = 4
        CNFcopy = list(CNF.copy())
        Cnk2 = combinations(X2, in_dis_num2)
        for Cnk2_i in Cnk2:
            Cnk2_i = set(Cnk2_i)
            sign = True
            for DIS in CNFcopy:
                if DIS.issubset(Cnk2_i):
                    sign = False
                    break
                if Cnk2_i.issubset(DIS):
                    CNF.remove(DIS)
            CNFcopy = list(CNF.copy())
            if sign:
                Cnk2_i = frozenset(Cnk2_i)
                CNF.add(Cnk2_i)

print ('+ 6: len(CNF) = ', len(CNF))

# Ограничение 9 =============================================================================

for g in range(G_num):
    if delta(G_maxC,g) == 1:
        Pg = []
        for p in range(P_num):
            if GP[g][p] == 1:
                Pg.append(p)
        Fg = []
        for f in range(F_num):
            if GF[g][f] == 1:
                Fg.append(f)
        for w in range(W_num):
            for d in range(D_num):
                X9 = list()
                for c in range(C_num):
                    u = w*D_num + d*C_num + c
                    for r in range(R_num):
                        for e in range(E_num):
                            for z in range(Z_num):
                                oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(g) + '_' + str(e) + '_' + str(z)
                                set_oper = set()
                                set_oper.add(oper)
                                if set_oper not in CNF:
                                    X9.append(oper)
                                for f in Fg:
                                    oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(f+G_num) + '_' + str(e) + '_' + str(z)
                                    set_oper = set()
                                    set_oper.add(oper)
                                    if set_oper not in CNF:
                                        X9.append(oper)
                                for p in Pg:
                                    oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(p+G_num+F_num) + '_' + str(e) + '_' + str(z)
                                    set_oper = set()
                                    set_oper.add(oper)
                                    if set_oper not in CNF:
                                        X9.append(oper)
                in_dis_num = G_maxC[g] + 1
                # in_dis_num = 3
                CNFcopy = list(CNF.copy())
                Cnk = combinations(X9, in_dis_num)
                for Cnk_i in Cnk:
                    Cnk_i = set(Cnk_i)
                    sign = True
                    for DIS in CNFcopy:
                        if DIS.issubset(Cnk_i):
                            sign = False
                            break
                        if Cnk_i.issubset(DIS):
                            CNF.remove(DIS)
                    CNFcopy = list(CNF.copy())
                    if sign:
                        Cnk_i = frozenset(Cnk_i)
                        CNF.add(Cnk_i)

print ('+ 9: len(CNF) = ', len(CNF))

# Ограничение 10 ============================================================================

for e in range(E_num):
    for w in range(W_num):
        for d in range(D_num):
            if delta(EWD_maxC, [e, w, d]) == 1:
                X10 = list()
                for c in range(C_num):
                    u = w*D_num + d*C_num + c
                    for r in range(R_num):
                        for n in range(N_num):
                            for z in range(Z_num):
                                oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                                set_oper = set()
                                set_oper.add(oper)
                                if set_oper not in CNF:
                                    X10.append(oper)
                in_dis_num = EWD_maxC[e][w][d] + 1
                # in_dis_num = 5 
                CNFcopy = list(CNF.copy())
                Cnk = combinations(X10, in_dis_num)
                for Cnk_i in Cnk:
                    Cnk_i = set(Cnk_i)
                    sign = True
                    for DIS in CNFcopy:
                        if DIS.issubset(Cnk_i):
                            sign = False
                            break
                        if Cnk_i.issubset(DIS):
                            CNF.remove(DIS)
                    CNFcopy = list(CNF.copy())
                    if sign:
                        Cnk_i = frozenset(Cnk_i)
                        CNF.add(Cnk_i)

print ('+ 10: len(CNF) = ', len(CNF))

# Ограничение 7 =============================================================================

if (W_num == 2):
    for n in range(N_num):
        for z in range(Z_num):
            for w in range(W_num):
                # В X7_pos лежат все соответсвующие n и z Х, а в X7_neg только те, которые можно использовать с отрицанием
                X7_neg = list()
                X7_pos = list()
                for d in range(D_num):
                    for c in range(C_num):
                        u = w*D_num + d*C_num + c
                        for r in range(R_num):
                            for e in range(E_num):
                                oper_pos = 'Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                                X7_pos.append(oper_pos)
                                oper_neg = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                                set_oper_neg = set()
                                set_oper_neg.add(oper_neg)
                                if set_oper_neg not in CNF:
                                    X7_neg.append(oper_pos)
                            
                pos_num_dis1 = D_num*C_num*R_num*E_num - QNZW[n][z][0] + 1
                pos_num_dis2 = D_num*C_num*R_num*E_num - QNZW[n][z][1] + 1
                neg_num_dis1 = QNZW[n][z][0] + 1
                neg_num_dis2 = QNZW[n][z][1] + 1

                posDISnum = max(pos_num_dis1,pos_num_dis2)
                negDISnum = max(neg_num_dis1,neg_num_dis2)

                # Добавляем дизъюнкты, состоящие из переменных без отрицаний
                CNFcopy = list(CNF.copy())
                Cnk = combinations(X7_pos, posDISnum)
                for Cnk_i in Cnk:
                    Cnk_i = set(Cnk_i)
                    sign = True
                    for DIS in CNFcopy:
                        if DIS.issubset(Cnk_i):
                            sign = False
                            break
                        if Cnk_i.issubset(DIS):
                            CNF.remove(DIS)
                    CNFcopy = list(CNF.copy())
                    if sign:
                        Cnk_i = frozenset(Cnk_i)
                        CNF.add(Cnk_i)
                
                # Добавляем дизъюнкты, состоящие из переменных c отрицаниями
                CNFcopy = list(CNF.copy())
                Cnk = combinations(X7_neg, negDISnum)
                for Cnk_i in Cnk:
                    Cnk_i = set(Cnk_i)
                    Cnk_i_neg = set()
                    for x in Cnk_i:
                        Cnk_i_neg.add('-' + x)
                    sign = True
                    for DIS in CNFcopy:
                        if DIS.issubset(Cnk_i_neg):
                            sign = False
                            break
                        if Cnk_i_neg.issubset(DIS):
                            CNF.remove(DIS)
                    CNFcopy = list(CNF.copy())
                    if sign:
                        Cnk_i_neg = frozenset(Cnk_i_neg)
                        CNF.add(Cnk_i_neg)

                # Функция, формирующая дизъюнкты, состоящие из pos_num переменных без отрицаний и neg_num переменных с отрицаниями.
                # Поскольку это единственные дизъюнкты смешанного типа, они не могут поглотить никакие другие. Таким образом закон поглощения может быть
                # учтен посредством формирования базы запрещенных дизъюнктов.
                def POS_NEG_DIS_7 (CNF, X7_pos, X7_neg, pos_num, neg_num):
                    DIS_pos = set()
                    forbiddenDisPos_3 = set()
                    for i in range(2, pos_num+1):
                        Cnk = combinations(X7_pos, i)
                        for Cnk_i in Cnk:
                            Cnk_i = set(Cnk_i)
                            if Cnk_i in CNF:
                                Cnk_i_others = list(set(X7_pos) - Cnk_i)
                                Cnk_inDisNum_i = combinations(Cnk_i_others, pos_num-i)
                                for cnk in Cnk_inDisNum_i:
                                    fd = set()
                                    fd.update(Cnk_i)
                                    fd.update(cnk)
                                    fd = frozenset(fd)
                                    forbiddenDisPos_3.add(fd)  
                    Cnk = combinations(X7_pos, pos_num)
                    for Cnk_i in Cnk:
                        Cnk_i = set(Cnk_i)
                        if Cnk_i not in forbiddenDisPos_3:
                            Cnk_i = frozenset(Cnk_i)
                            DIS_pos.add(Cnk_i)

                    DIS_neg = set()
                    forbiddenDisNeg_3 = set()
                    for i in range(2, neg_num+1):
                        Cnk = combinations(X7_neg, i)
                        for Cnk_i in Cnk:
                            Cnk_i = set(Cnk_i)
                            Cnk_i_neg = set()
                            for x in Cnk_i:
                                Cnk_i_neg.add('-' + x)
                            Cnk_i_neg = frozenset(Cnk_i_neg)
                            if Cnk_i_neg in CNF:
                                Cnk_i_others = list(set(X7_neg) - Cnk_i)
                                Cnk_inDisNum_i = combinations(Cnk_i_others, neg_num-i)
                                for cnk in Cnk_inDisNum_i:
                                    fd = set()
                                    fd.update(Cnk_i)
                                    fd.update(cnk)
                                    fd = frozenset(fd)
                                    forbiddenDisNeg_3.add(fd) 

                    Cnk = combinations(X7_neg, neg_num)
                    for Cnk_i in Cnk:
                        Cnk_i = set(Cnk_i)
                        if Cnk_i not in forbiddenDisNeg_3:
                            Cnk_i = frozenset(Cnk_i)
                            DIS_neg.add(Cnk_i)

                    for dis_pos in DIS_pos:
                        for dis_neg in DIS_neg:
                            if dis_pos.isdisjoint(dis_neg):
                                new_dis = set()
                                dis_pos = frozenset(dis_pos)
                                new_dis.update(dis_pos)
                                dis_realy_neg = set()
                                for x in dis_neg:
                                    dis_realy_neg.add('-' + x)
                                dis_realy_neg = frozenset(dis_realy_neg)
                                new_dis.update(dis_realy_neg)
                                new_dis = frozenset(new_dis)
                                CNF.add(new_dis)

                if QNZW[n][z][0] >= QNZW[n][z][1] + 2:
                    POS_NEG_DIS_7(CNF, X7_pos, X7_neg, pos_num_dis1, neg_num_dis2)
                if QNZW[n][z][1] >= QNZW[n][z][0] + 2:
                    POS_NEG_DIS_7(CNF, X7_pos, X7_neg, pos_num_dis2, neg_num_dis1)
                        
    print ('+ 7: len(CNF) = ', len(CNF))


CNF_sort = list()
for dis in CNF:
    dis = list(dis)
    dis.sort()
    CNF_sort.append(dis)
CNF_sort.sort()

file.write(str(U_num*R_num*N_num*E_num*Z_num) + '\n')
file.write(str(len(CNF)) + '\n')

for dis in CNF_sort:
    for x in dis:        
        file.write(x + ' ')
    file.write('\n')

