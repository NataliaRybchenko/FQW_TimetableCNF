# 6 временных единиц (1 неделя, 3 дня)
#     2 пары в 1 день 
#     2 пары во 2 день 
#     2 пары в 3 день
# 14 групп
#     4 группы
#     2 потока
#     8 подгрупп
# 5 занятий
#     2 по 1 предмету (лекция и практика)
#     2 по 2 предмету (лекция и практика)
#     1 по 3 предмету (практика по подгруппам)
# 8 преподавателей
#     1,5 ведут по 1 предмету лекцию и практику
#     2,6 ведут по 2 предмету лекцию и практику
#     3-4,7-8 ведут по 3 предмету практику по подгруппам
# Учебный план (для обеих групп) 
#     2 лекции (1,5 и 2,6 преподаватели 1 и 2 предметы, соответсвенно)
#     2 практики по группам (1,5 и 2,6 преподаватели 1 и 2 предметы, соответсвенно)
#     1 практика по подгруппам (3, 4, 7 и 8 преподаватели)


# Функция δ(массив, индексы)
# Возвращает 1, если элемент массива с соответсвующим индексом является обязательным требованием, 0 в противном случае
# Установим в 1, чтобы выполнение всех требований было обязательным
def delta(Arr, idx):
    return 1

W_num = 1
D_num = 3
C_num = 2
U_num = W_num*D_num*C_num

G_num = 4
F_num = 2
P_num = 8
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
GF[2][1] = 1
GF[3][1] = 1
# print ('GF:')
# for g in range(G_num):
#     for f in range(F_num):
#         print (GF[g][f], end =' ')
#     print (end = '\n')
# print ('_____________________')


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
GP[2][4] = 1
GP[2][5] = 1
GP[3][6] = 1
GP[3][7] = 1
# print ('GP:')
# for g in range(G_num):
#     for p in range(P_num):
#         print (GP[g][p], end =' ')
#     print (end = '\n')
# print ('_____________________')


# Численность групп, потоков и подгрупп =======================
QN = [15, 18, 16, 17, 33, 33, 7, 8, 9, 9, 8, 8, 9, 8]
# print ('QN = ', QN)
# print ('_____________________')


# Ограничение сверху на количество пар в день у каждой из групп
G_maxC = []
for g in range(G_num):
    G_maxC.append(0)
G_maxC = [2, 2, 2, 2]
# print ('G_maxC = ', G_maxC)
# print ('_____________________')

# ========================================================================================

S_num = 3
K_num = 2
Z_num = 5
Z = [[0,0], [0,1], [1,0], [1,1], [2,1]]
# print ('Z = ', Z)
# print ('_____________________')


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

QNZW[2][1][0] = 1
QNZW[2][3][0] = 1
QNZW[3][1][0] = 1
QNZW[3][3][0] = 1

# Лекции по потокам
QNZW[4][0][0] = 1
QNZW[4][2][0] = 1

QNZW[5][0][0] = 1
QNZW[5][2][0] = 1

# Практики по подгруппам
QNZW[6][4][0] = 1
QNZW[7][4][0] = 1
QNZW[8][4][0] = 1
QNZW[9][4][0] = 1

QNZW[10][4][0] = 1
QNZW[11][4][0] = 1
QNZW[12][4][0] = 1
QNZW[13][4][0] = 1

# print ('QNZW:')
# for n in range(N_num):
#     for w in range(W_num):
#         for z in range(Z_num):
#             print (QNZW[n][z][w], end =' ')
#         print (end = '\n')
# print ('_____________________')


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
NSK_U[4][0][0][1] = 0
NSK_U[4][0][0][3] = 0
NSK_U[4][0][0][5] = 0

NSK_U[4][1][0][1] = 0
NSK_U[4][1][0][3] = 0
NSK_U[4][1][0][5] = 0

NSK_U[5][0][0][1] = 0
NSK_U[5][0][0][3] = 0
NSK_U[5][0][0][5] = 0

NSK_U[5][1][0][1] = 0
NSK_U[5][1][0][3] = 0
NSK_U[5][1][0][5] = 0


# ========================================================================================

R_num = 10
B_num = 1

# Вместимость аудиторий =============================================
QR = [10, 12, 17, 18, 35, 12, 12, 20, 16, 40]
# print ('QR = ', QR)
# print ('_____________________')

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
RB[5][0] = 1
RB[6][0] = 1
RB[7][0] = 1
RB[8][0] = 1
RB[9][0] = 1
# print ('RB:')
# for r in range(R_num):
#     for b in range(B_num):
#         print (RB[r][b], end =' ')
#     print (end = '\n')
# print ('_____________________')

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
SK_R[0][1][9] = 0
SK_R[1][1][9] = 0
SK_R[2][1][9] = 0
# print ('SK_R:')
# for s in range(S_num):
#     for r in range(R_num):
#         for k in range(K_num):
#             print (SK_R[s][k][r], end =' ')
#         print (end = ' ')
#     print (end = '\n')
# print ('_____________________')


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
# print ('SK_B:')
# for s in range(S_num):
#     for b in range(B_num):
#         for k in range(K_num):
#             print (SK_B[s][k][b], end =' ')
#         print (end = ' ')
#     print (end = '\n')
# print ('_____________________')


# ========================================================================================

E_num = 8

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
E_U[4] = [1, 1,   0, 0,   1, 1]
E_U[5] = [0, 1,   1, 1,   0, 0]
E_U[6] = [0, 0,   0, 1,   1, 1]
E_U[7] = [1, 1,   0, 1,   1, 0]

# print ('E_U:')
# for e in range(E_num):
#     for u in range(U_num):
#         print (E_U[e][u], end =' ')
#     print (end = '\n')
# print ('_____________________')


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

NSKE[2][0][1][4] = 1
NSKE[2][1][1][5] = 1
NSKE[3][0][1][4] = 1
NSKE[3][1][1][5] = 1

# Лекции
NSKE[4][0][0][0] = 1
NSKE[4][1][0][1] = 1

NSKE[5][0][0][4] = 1
NSKE[5][1][0][5] = 1

# Практики по подгруппам
NSKE[6][2][1][2] = 1
NSKE[7][2][1][3] = 1
NSKE[8][2][1][2] = 1
NSKE[9][2][1][3] = 1

NSKE[10][2][1][6] = 1
NSKE[11][2][1][7] = 1
NSKE[12][2][1][6] = 1
NSKE[13][2][1][7] = 1


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
EWD_maxC[7][0][0] = 1

# print ('EWD_maxC:')
# for e in range(E_num):
#     for w in range(W_num):
#         for d in range(D_num):
#             print (EWD_maxC[e][w][d], end =' ')
#         print (end = ' ')
#     print (end = '\n')
# print ('____________________________________________________________')
