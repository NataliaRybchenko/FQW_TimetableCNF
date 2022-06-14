import sys
import CNF_functions
from CNF_functions import *

print ('Output file name is', sys.argv[1])

opt_num = 0
while (opt_num != '3'):
    opt_num = input('Select option: \n 1. Test for 1 week \n 2. Test for 2 weeks \n 3. Quit \n Your answer is ')
    while (opt_num != '1' and opt_num != '2' and opt_num != '3'):
        print ('Wrong answer! Try again.')
        print()
        opt_num = input('Select option: \n 1. Test for 1 week \n 2. Test for 2 weeks \n 3. Quit \n Your answer is ')
    print()
    if opt_num == '1':
        from W1 import *
    if opt_num == '2':
        from W2 import *
    if opt_num == '3':
        exit()

    file = open(sys.argv[1], 'w')

    CNF_dict = dict()

    X_neg_possible_str = set()
    X_pos_possible_str = set()
    X_neg_possible_fs = set()
    X_pos_possible_fs = set()
    for u in range(U_num):
        for r in range(R_num):
            for n in range(N_num):
                for e in range(E_num):
                    for z in range(Z_num):
                        oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                        oper_set = set()
                        oper_set.add(oper)
                        oper_set = frozenset(oper_set)
                        X_neg_possible_fs.add(oper_set)
                        X_neg_possible_str.add(oper)
                        oper = 'Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                        oper_set = set()
                        oper_set.add(oper)
                        oper_set = frozenset(oper_set)
                        X_pos_possible_fs.add(oper_set)
                        X_pos_possible_str.add(oper)


    # ЗАПИШЕМ В ФАЙЛ ДИЗЪЮНКТЫ, СООТВЕТСТВУЮЩИЕ ОГРАНИЧЕНИЯМ 

    print ('ADD NEGATIVE:')
    CNF_dict['-'] = dict()

    # Ограничение 5 =============================================================================
    num = 1
    CNF_dict['-'][num] = set()

    for u in range(U_num):
        for r in range (R_num):
            for n in range(N_num):
                if (QR[r]/QN[n] < 1):
                    for e in range(E_num):
                        for z in range(Z_num):
                            DIS = set()
                            DIS.add('-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z))
                            DIS = frozenset(DIS)
                            CNF_dict['-'][num].add(DIS)
    X_neg_possible_fs = X_neg_possible_fs.difference(CNF_dict['-'][1])
    for fs in X_neg_possible_fs:
        for x in fs:
            X_neg_possible_str.add(x)

    print_res_len (CNF_dict, 5)

    # Ограничение 8 =============================================================================
    num = 1
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
                                                        CNF_dict['-'][num].add(DIS)
    X_neg_possible_fs = X_neg_possible_fs.difference(CNF_dict['-'][1])
    for fs in X_neg_possible_fs:
        for x in fs:
            X_neg_possible_str.add(x)

    print_res_len (CNF_dict, 8)


    # Ограничения 1-4 ============================================================================        
    num = 2
    CNF_dict['-'][num] = set()

    X14 = list()
    for u in range(U_num):
        for r in range(R_num):
            for n in range(N_num):
                for e in range(E_num):
                    for z in range(Z_num):
                        oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                        oper_set = set()
                        oper_set.add(oper)
                        if oper_set in X_neg_possible_fs:
                            idxs = list()
                            idxs.append(u)
                            idxs.append(r)
                            idxs.append(n)
                            idxs.append(e)
                            idxs.append(z)
                            X14.append(idxs)
    Cnk = combinations(X14, 2)
    for Cnk_i in Cnk:
        if Cnk_i[0][0] == Cnk_i[1][0] and (Cnk_i[0][1] == Cnk_i[1][1] or Cnk_i[0][2] == Cnk_i[1][2] or Cnk_i[0][3] == Cnk_i[1][3]):
            oper1 = '-Xurnez_' + str(Cnk_i[0][0]) + '_' + str(Cnk_i[0][1]) + '_' + str(Cnk_i[0][2]) + '_' + str(Cnk_i[0][3]) + '_' + str(Cnk_i[0][4])
            oper2 = '-Xurnez_' + str(Cnk_i[1][0]) + '_' + str(Cnk_i[1][1]) + '_' + str(Cnk_i[1][2]) + '_' + str(Cnk_i[1][3]) + '_' + str(Cnk_i[1][4])
            DIS = set()
            DIS.add(oper1)
            DIS.add(oper2)
            DIS = frozenset(DIS)
            CNF_dict['-'][num].add(DIS)
    
    print_res_len (CNF_dict, '1-4')

    # Начиная с этого момента длина дизъюнктов зависит от других параметров задачи => при их добавлении необходимо учитывать возможность поглощения

    # Ограничение 10 ============================================================================
    keys_neg = list(CNF_dict['-'].keys())

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
                                    if set_oper in X_neg_possible_fs:
                                        X10.append(oper)
                    in_dis_num = EWD_maxC[e][w][d] + 1
                    add_dis_one_pol ('-', CNF_dict, keys_neg, X10, in_dis_num, X_neg_possible_str, X_neg_possible_fs)

    print_res_len (CNF_dict, 10)


    # Ограничение 7 =============================================================================
    keys_neg = list(CNF_dict['-'].keys())

    if (W_num == 2):
        for n in range(N_num):
            for z in range(Z_num):
                for w in range(W_num):
                    # В X7_pos лежат все соответсвующие n и z Х, а в X7_neg только те, которые можно использовать с отрицанием
                    X7_neg = list()
                    for d in range(D_num):
                        for c in range(C_num):
                            u = w*D_num + d*C_num + c
                            for r in range(R_num):
                                for e in range(E_num):
                                    oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                                    set_oper = set()
                                    set_oper.add(oper)
                                    if set_oper in X_neg_possible_fs:
                                        X7_neg.append(oper)
                    if QNZW[n][z][0] > 0 or QNZW[n][z][1] > 0:
                        neg_num_dis1 = QNZW[n][z][0] + 1
                        neg_num_dis2 = QNZW[n][z][1] + 1
                        in_dis_num = min(neg_num_dis1,neg_num_dis2)
                        add_dis_one_pol ('-', CNF_dict, keys_neg, X7_neg, in_dis_num, X_neg_possible_str, X_neg_possible_fs)
                        
        print_res_len (CNF_dict, 7)


    # Ограничение 6 =============================================================================
    keys_neg = list(CNF_dict['-'].keys())

    for n in range(N_num):
        for z in range(Z_num):
            # X6_neg - все -Х с соответсвующими n и z, еще не вошедшие в CNF
            X6_neg = list()
            for u in range(U_num):
                for r in range(R_num):
                    for e in range(E_num):
                        oper_2 = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                        set_oper2 = set()
                        set_oper2.add(oper_2)
                        if set_oper2 in X_neg_possible_fs:
                            X6_neg.append(oper_2)
            SUM_QNZW = 0
            for w in range(W_num):
                SUM_QNZW = SUM_QNZW + QNZW[n][z][w]
            in_dis_num = SUM_QNZW + 1
            add_dis_one_pol ('-', CNF_dict, keys_neg, X6_neg, in_dis_num, X_neg_possible_str, X_neg_possible_fs)

    print_res_len (CNF_dict, 6)


    # Ограничение 9 =============================================================================
    keys_neg = list(CNF_dict['-'].keys())

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
                                    if set_oper in X_neg_possible_fs:
                                        X9.append(oper)
                                    for f in Fg:
                                        oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(f+G_num) + '_' + str(e) + '_' + str(z)
                                        set_oper = set()
                                        set_oper.add(oper)
                                        if set_oper in X_neg_possible_fs:
                                            X9.append(oper)
                                    for p in Pg:
                                        oper = '-Xurnez_' + str(u) + '_' + str(r) + '_' + str(p+G_num+F_num) + '_' + str(e) + '_' + str(z)
                                        set_oper = set()
                                        set_oper.add(oper)
                                        if set_oper in X_neg_possible_fs:
                                            X9.append(oper)
                    in_dis_num = G_maxC[g] + 1
                    add_dis_one_pol ('-', CNF_dict, keys_neg, X9, in_dis_num, X_neg_possible_str, X_neg_possible_fs)

    print_res_len (CNF_dict, 9)


    print ('ADD POSITIVE:')
    CNF_dict['+'] = dict()

    if (W_num == 2):
    # Ограничение 7 =============================================================================
        for n in range(N_num):
            for z in range(Z_num):
                for w in range(W_num):
                    # В X7_pos лежат все соответсвующие n и z Х, а в X7_neg только те, которые можно использовать с отрицанием
                    X7_pos = list()
                    for d in range(D_num):
                        for c in range(C_num):
                            u = w*D_num + d*C_num + c
                            for r in range(R_num):
                                for e in range(E_num):
                                    oper_pos = 'Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                                    X7_pos.append(oper_pos)
                    if QNZW[n][z][0] > 0 or QNZW[n][z][1] > 0:
                        pos_num_dis1 = D_num*C_num*R_num*E_num - QNZW[n][z][0] + 1
                        pos_num_dis2 = D_num*C_num*R_num*E_num - QNZW[n][z][1] + 1
                        in_dis_num = max(pos_num_dis1,pos_num_dis2)
                        # Все дизъюнкты, добавленные до этого, состояли исключительно из переменных с отрицаниями => необходимости в провке поглощения нет
                        Cnk = combinations(X7_pos, in_dis_num)
                        for Cnk_i in Cnk:
                            if in_dis_num not in CNF_dict['+'].keys():
                                CNF_dict['+'][in_dis_num] = set()
                            DIS = set(Cnk_i)
                            DIS = frozenset(DIS)
                            CNF_dict['+'][in_dis_num].add(DIS)
                    
        print_res_len (CNF_dict, 7)

    # Ограничение 6 =============================================================================
    keys_pos = list(CNF_dict['+'].keys())

    for n in range(N_num):
        for z in range(Z_num):
            # X6_pos - все Х с соответсвующими n и z
            X6_pos = list()
            for u in range(U_num):
                for r in range(R_num):
                    for e in range(E_num):
                        oper_1 = 'Xurnez_' + str(u) + '_' + str(r) + '_' + str(n) + '_' + str(e) + '_' + str(z)
                        X6_pos.append(oper_1)
            SUM_QNZW = 0
            for w in range(W_num):
                SUM_QNZW = SUM_QNZW + QNZW[n][z][w]
            in_dis_num = U_num*R_num*E_num - SUM_QNZW + 1
            add_dis_one_pol ('+', CNF_dict, keys_pos, X6_pos, in_dis_num, X_pos_possible_str, X_pos_possible_fs)

    print_res_len (CNF_dict, 6)


    if (W_num == 2):
        # Добавляем смешанные дизъюнкты
        print ('ADD MIXED:')

        # Ограничение 7 ===========================================================================
        CNF_dict['+-'] = dict()
        CNF_dict['+-']['all'] = set()
        keys_pos = list(CNF_dict['+'].keys())
        keys_neg = list(CNF_dict['-'].keys())

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
                                    if set_oper_neg in X_neg_possible_fs:
                                        X7_neg.append(oper_pos)
                    if QNZW[n][z][0] > 0 or QNZW[n][z][1] > 0:
                        pos_num_dis1 = D_num*C_num*R_num*E_num - QNZW[n][z][0] + 1
                        pos_num_dis2 = D_num*C_num*R_num*E_num - QNZW[n][z][1] + 1
                        neg_num_dis1 = QNZW[n][z][0] + 1
                        neg_num_dis2 = QNZW[n][z][1] + 1
                        if QNZW[n][z][0] >= QNZW[n][z][1] + 2:
                            add_pos_neg_dis(CNF_dict, X7_pos, X7_neg, pos_num_dis1, neg_num_dis2, keys_pos, keys_neg)
                        if QNZW[n][z][1] >= QNZW[n][z][0] + 2:
                            add_pos_neg_dis(CNF_dict, X7_pos, X7_neg, pos_num_dis2, neg_num_dis1, keys_pos, keys_neg)

        print_res_len (CNF_dict, 7)
    print ('The final CNF in DIMACS format is in the file', sys.argv[1])
    print()

    CNF_sort = list()
    for pol in CNF_dict.keys():
        for num, cnf_num in CNF_dict[pol].items():
            for dis in cnf_num:
                dis = list(dis)
                dis.sort()
                CNF_sort.append(dis)
    CNF_sort.sort()

    file.write(str(U_num*R_num*N_num*E_num*Z_num) + '\n')
    file.write(str(len(CNF_sort)) + '\n')

    for dis in CNF_sort:
        for x in dis:        
            file.write(x + ' ')
        file.write('0')
        file.write('\n')

