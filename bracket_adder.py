#!/usr/bin/env python
# coding=utf-8

import re

def expression_analyzer(expr):

    orig_expression = expr.split('=')[0]
    orig_result = int(expr.split('=')[1])
    print orig_expression


    # all_numpairs = re.findall(r'(?=([+-/*]+|\A\d+[+-/*]\d+))', orig_expression)
    # all_numpairs = re.sub(r'(?=(\d+[+-/*]\d+))', "", orig_expression)
    # all_numpairs = re.sub(r'(\d+)([+-/*]\d+)', r'\1', orig_expression)
    # all_numpairs = re.sub(r'(\d+)([+-/*]\d+)', r'\2', orig_expression)

    all_new_pairs = []
    all_new_pairs_with_bracket = []
    # all_numpairs = re.findall(r'(?=((\A|[^\d])\d+[+-/*]\d+))', orig_expression)  #JOOO
    all_numpairs = re.findall(r'(?=((\A|[^\d])(\d+[\+\-\/\*]{1,2}\d+){1}))', orig_expression) #JOOOOO

    all_numpairs_compile = re.compile(r'(?=((\A|[^\d])(\d+[\+\-\/\*]\d+){1,}))') #JOOOOO

    # all_numpairs = re.findall(r'(?=((\A|[^\d])\d+([\+\-\*\/]+\d+){0,}?))', orig_expression)

    # all_numpairs = re.compile(r'(?=((\A|[^\d])\d+([\+\-\*\/]+\d+){0,}))')
    # print all_numpairs.search(orig_expression)
    print all_numpairs

    for num in all_numpairs:
        print num[0]

    print
    print all_numpairs_compile.search(orig_expression)


    # for i, old_num_pair in enumerate(all_numpairs):
    #     all_new_pairs.append(old_num_pair[0].replace(old_num_pair[1], "", 1))
    #     # all_new_pairs_with_bracket.append(add_bracket(all_new_pairs[i]))
    # print
    # print all_new_pairs
    # print all_new_pairs_with_bracket


    # all_new_expr = []
    # new_expr_results = []
    # for i, pair in enumerate(all_new_pairs):
    #     # all_new_expr.append(orig_expression.replace(all_new_pairs[i], all_new_pairs_with_bracket[i]))
    #     all_new_expr.append(make_new_expr(orig_expression, all_new_pairs[i], all_new_pairs_with_bracket[i]))
    #
    #     new_expr_results.append(evaluate(all_new_expr[i]))
    #     if new_expr_results[i] == orig_result:
    #         # print "Van megoldás: %s" % all_new_expr[i] + "=" + str(orig_result)
    #         break

    # print all_new_expr
    # print (new_expr_results)


    print '\n'

    dd = "beveled"
    print re.findall(r'bevel+ed', dd)

    ff = "136"
    print re.findall(r'\d+?', ff)

    gg = ['aircdshjshd', 'aircraft', 'dfgdairghhg', 'airplane', 'jettt', 'sfsdfjet', 'jet']
    gg = 'airplane'
    print re.findall(r'(air(craft|plane))', gg)


    kk = '1=dgdfg 4=fdfgdfgnmb 55=34rergekjl dgdfgf=ferkjfgh'
    print re.findall(r'(\d+)=(.+)', kk)



def make_new_expr(orig_expr, string_to_change, new_string):
    return orig_expr.replace(string_to_change, new_string)



def add_bracket(pair_in):
    return "(" + pair_in + ")"


def evaluate(expression_in):
    return eval(expression_in)


def main():
    # whole_expression = "115+3*41-42*22+345/88=30"
    whole_expression = "15+8-4**2+83/2-75*39-51/17*94=23"

    expression_analyzer(whole_expression)


if __name__ == '__main__':
    main()
