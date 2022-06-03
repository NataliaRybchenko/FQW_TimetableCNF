from itertools import combinations
import math
from math import factorial
import numpy as np

def print_res_len (CNF_dict, rest_num):
    sum_len = 0                        
    for k_pol in CNF_dict.keys():
        for k_num in CNF_dict[k_pol].keys():
            print ('+', rest_num, ': len(', k_pol, k_num, ') = ', len(CNF_dict[k_pol][k_num]))
            sum_len = sum_len + len(CNF_dict[k_pol][k_num])
    print ('+', rest_num, ': len(CNF) = ', sum_len)
    print()

def add_dis_one_pol (pol, CNF_dict, keys, X, in_dis_num, X_possible_str, X_possible_fs):
    forbiddenDis = set()
    Cnk = combinations(X, in_dis_num)
    for Cnk_i in Cnk:
        Cnk_i = frozenset(Cnk_i)
        sign = True
        # forbiddenDis = set()
        for s in keys:
            if sign:
                if in_dis_num > s:
                    Cnk_i_others = list(set(X) - Cnk_i)
                    split_num_iter = factorial(len(Cnk_i))/(factorial(s) * factorial(len(Cnk_i) - (s)))
                    check_num_iter = len(CNF_dict[pol][s])
                    if len(Cnk_i_others) > 0 and len(Cnk_i_others) - (in_dis_num-s) > 0:
                        addition_num_iter = factorial(len(Cnk_i_others))/(factorial(in_dis_num-s) * factorial(len(Cnk_i_others) - (in_dis_num-s)))
                    else:
                        addition_num_iter = np.inf
                    min_time = min(split_num_iter, check_num_iter, addition_num_iter)
                    if min_time == check_num_iter:
                        for dis in CNF_dict[pol][s]:
                            if dis.issubset(Cnk_i):
                                sign = False
                                break
                    elif min_time == split_num_iter:
                        isItInCNF = combinations(Cnk_i, s)
                        for isItInCNF_i in isItInCNF:
                            isItInCNF_i = frozenset(isItInCNF_i)
                            if isItInCNF_i in CNF_dict[pol][s]:
                                sign = False
                                break
                    elif min_time == addition_num_iter:
                        add_combinations = combinations(Cnk_i_others, in_dis_num-s)
                        for add_comb in add_combinations:
                            fd = set()
                            fd.update(Cnk_i)
                            fd.update(add_comb)
                            fd = frozenset(fd)
                            forbiddenDis.add(fd)
            else:
                break
        if sign and (Cnk_i not in forbiddenDis):
            if in_dis_num not in CNF_dict[pol].keys():
                CNF_dict[pol][in_dis_num] = set()
            CNF_dict[pol][in_dis_num].add(Cnk_i)
            # print ('add: ', Cnk_i)
            if pol == '-':
                for s in keys:
                    if s > 1 and s > in_dis_num:
                        Cnk_i_others = list(X_possible_str - Cnk_i)
                        comb_num = factorial(len(Cnk_i_others))/(factorial(s-in_dis_num) * factorial(len(Cnk_i_others) - (s-in_dis_num)))
                        if len(CNF_dict[pol][s]) < comb_num:
                            for dis3 in CNF_dict[pol][s]:
                                if Cnk_i.issubset(dis3):
                                    CNF_dict[pol][s].remove(dis3)
                                    # print ('remove: ', dis3)
                        else:
                            Cnk_inDisNum_i = combinations(Cnk_i_others, s-in_dis_num)
                            for cnk in Cnk_inDisNum_i:
                                fd = set()
                                fd.update(Cnk_i)
                                fd.update(cnk)
                                fd = frozenset(fd)
                                if fd in CNF_dict[pol][s]:
                                    CNF_dict[pol][s].remove(fd)
                                    # print ('remove: ', fd)
            if 1 in CNF_dict[pol].keys():
                X_possible_fs = X_possible_fs.difference(CNF_dict[pol][1])
                for fs in X_possible_fs:
                    for x in fs:
                        X_possible_str.add(x)
        # else:
        #     print('forbidden: ', Cnk_i)

def make_part_one_pol (pol, CNF_dict, keys, X, num):
    DIS_part = set()
    forbiddenDis = set()
    for s in keys:
        if num >= s:
            Cnk = combinations(X, s)
            for Cnk_i in Cnk:
                Cnk_i = set(Cnk_i)
                Cnk_i_pol = set()
                if pol == '-':
                    for x in Cnk_i:
                        Cnk_i_pol.add('-' + x)
                    Cnk_i_pol = frozenset(Cnk_i_pol)
                else:
                    Cnk_i_pol = frozenset(Cnk_i)
                if Cnk_i_pol in CNF_dict[pol][s]:
                    Cnk_i_others = list(set(X) - Cnk_i)
                    Cnk_inDisNum_i = combinations(Cnk_i_others, num-s)
                    for cnk in Cnk_inDisNum_i:
                        fd = set()
                        fd.update(Cnk_i)
                        fd.update(cnk)
                        fd = frozenset(fd)
                        forbiddenDis.add(fd)
    Cnk = combinations(X, num)
    for Cnk_i in Cnk:
        Cnk_i = frozenset(Cnk_i)
        if Cnk_i not in forbiddenDis:
            DIS_part.add(Cnk_i)
        #     print ('add to pos part: ', Cnk_i)
        # else:
        #     print('forbidden pos part: ', Cnk_i)
    return DIS_part

def add_pos_neg_dis (CNF_dict, X7_pos, X7_neg, pos_num, neg_num, keys_pos, keys_neg):
    # Конструируем позитивную часть
    DIS_pos = make_part_one_pol('+', CNF_dict, keys_pos, X7_pos, pos_num)
    # Конструируем негативную часть
    DIS_neg = make_part_one_pol('-', CNF_dict, keys_neg, X7_neg, neg_num)
    
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
                CNF_dict['+-']['all'].add(new_dis)