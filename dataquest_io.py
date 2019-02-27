#!/usr/bin/env python
# coding=utf-8

import sys
import csv
import re
import time
import datetime
import numpy
import pandas as pd
import os

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

kk = os.getcwd()
# print os.listdir(kk)


with open("legislators_4.txt", 'r') as leg:
    # legislators = leg.readlines()

    csv_file = csv.reader(leg)
    legislators = list(csv_file)

print legislators


exit()
print sys.executable
print sys.exec_prefix
print sys.prefix
print sys.platform

# import uj_csomag.proba_modul
# import uj_csomag.csomag_2.modul2



from uj_csomag import *
# import uj_csomag.csomag_2.modul2

# for p in sorted(sys.path):
#     print (p)

exit()
print
print "-----------1-----------"
print uj_csomag.proba_modul.attri
uj_csomag.proba_modul.kiir()
print
ujobj = uj_csomag.proba_modul.Ujclass()
ujobj.kiir()
print ujobj.attri
print "-----------1-----------"

print
print
print "-----------2-----------"
print uj_csomag.csomag_2.modul2.attri
uj_csomag.csomag_2.modul2.kiir()
print
ujobj = uj_csomag.csomag_2.modul2.Ujclass()
ujobj.kiir()
print ujobj.attri
print "-----------2-----------"



# import proba_modul





# class Ujclass:
#     def kiir(self):
#         print "proba_modul classmethod vagyok!"


exit()

nfl = pd.read_csv("nfl_suspensions_data.csv", index_col=0)
nfl.index.name = None
nfl_shape = nfl.shape
print nfl_shape



exit()




borrower_default_count_240 = [1606, 1567, 269, 184, 93, 75, 52, 88, 12, 5, 36, 154, 155, 104, 149, 278, 186, 223, 3546, 580, 331, 102, 106, 232, 86, 83, 822, 268, 43, 323, 258, 114, 63, 41, 41, 53, 674, 278, 883, 22, 23, 253, 217, 54, 892, 79, 155, 5, 598, 2, 2112, 54, 0, 32, 20,
                              251, 46, 553, 73, 435, 12, 17, 120, 84, 815, 157, 338, 264, 24, 69, 405, 8, 757, 44, 117, 18, 25, 197, 96, 339, 45, 20, 64, 132, 8, 20, 253, 48, 53, 162, 313, 197, 402, 337, 221, 97, 440, 1000, 549, 3, 72, 260, 114, 6, 111, 109, 61, 115, 104, 72, 889,
                              45, 19, 30, 70, 56, 36, 128, 33, 55, 25, 51, 59, 132, 174, 31, 184, 111, 235, 14, 179, 124, 58, 87, 50, 1333, 137, 157, 21, 148, 41, 45, 203, 12, 5, 42, 6, 66, 62, 50, 406, 20, 24, 166, 164, 58, 240, 26, 38, 15, 66, 192, 365, 153, 312, 88, 2, 69, 121,
                              32, 127, 11, 48, 679, 324, 131, 37, 91, 47, 7, 136, 24, 55, 22, 261, 131, 19, 211, 73, 130, 49, 1, 86, 2, 158, 78, 85, 10, 190, 36, 936, 334, 18, 135, 59, 184, 0, 41, 24, 45, 5, 172, 329, 13, 2, 102, 714, 845, 63, 330, 627, 361, 907, 17, 614, 485, 409,
                              217, 315, 205, 1838, 368, 157, 4, 104, 55, 57, 65, 16, 84, 168, 78, 38, 16, 153, 460, 54, 27, 286, 110, 77, 961, 753, 200, 85, 277, 6, 33, 169, 104, 40, 57, 882, 1018, 150, 3, 21, 502, 53, 9, 320, 876, 192, 156, 581, 209, 409, 91, 2, 598, 131, 323, 139,
                              9, 19, 9, 181, 181, 16, 138, 110, 42, 615, 112, 92, 55, 25, 626, 568, 410, 313, 53, 146, 293, 287, 427, 403, 27, 75, 599, 179, 275, 63, 58, 477, 29, 19, 5, 19, 51, 462, 190, 898, 22, 10, 246, 0, 485, 41, 142, 168, 14, 33, 602, 160, 92, 27, 186, 464, 8,
                              295, 550, 193, 237, 418, 114, 1534, 155, 57, 151, 66, 93, 166, 367, 14, 128, 19, 301, 0, 380, 988, 1458, 675, 162, 267, 20, 46, 243, 159, 9, 1368, 136, 18, 86, 138, 63, 827, 2, 133, 88, 125, 591, 47, 13, 101, 295, 78, 701, 43, 109, 61, 397, 142, 0, 1243,
                              47, 62, 82, 269, 325, 138, 386, 44, 201, 32, 116, 476, 57, 217, 175, 184, 66, 1, 37, 208, 442, 71, 17, 0, 205, 183, 164, 216, 120, 197, 93, 17, 35, 77, 158, 438, 189, 35, 2, 594, 154, 905, 139, 104, 40, 77, 95, 111, 221, 159, 138, 84, 789, 574, 44, 183,
                              140, 4, 276, 928, 82, 279, 26, 179, 65, 564, 106, 150, 180, 22, 99, 724, 1169, 169, 307, 20728, 132, 531, 99, 21, 318, 21, 70, 285, 168, 126, 1, 0, 222, 772, 233, 74, 0, 235, 52, 154, 47, 83, 20, 606, 6, 391, 56, 8, 213, 527, 282, 51, 83, 353, 188, 260,
                              433, 148, 69, 214, 1114, 212, 65, 52, 288, 418, 90, 1070, 67, 72, 167, 4, 391, 954, 12, 767, 91, 222, 9, 8, 57, 299, 935, 4, 79, 117, 103, 82, 194, 35, 83, 40, 89, 188, 907, 627, 42, 55, 93, 161, 638, 237, 201, 156, 84, 259, 165, 135, 89, 54, 350, 47, 13,
                              42, 89, 94, 146, 186, 33, 85, 377, 361, 166, 0, 219, 284, 114, 43, 389, 140, 212, 630, 259, 75, 207, 470, 206, 160, 30, 189, 832, 149, 32, 191, 150, 64, 325, 379, 317, 22, 140, 442, 86, 149, 762, 177, 124, 124, 42, 122, 88, 28, 55, 411, 61, 65, 1041, 96,
                              142, 14, 337, 302, 404, 164, 228, 67, 163, 437, 176, 78, 124, 1495, 426, 54, 121, 223, 66, 55, 30, 126, 3, 306, 1081, 350, 269, 131, 125, 31, 265, 349, 178, 1, 203, 43, 660, 2955, 255, 529, 672, 141, 573, 489, 455, 70, 160, 62, 247, 79, 108, 171, 209, 31,
                              106, 410, 232, 1046, 161, 628, 6, 31, 82, 96, 145, 55, 66, 485, 186, 74, 227, 129, 18, 144, 233, 301, 141, 29, 2, 402, 73, 65, 15, 194, 89, 172, 165, 82, 300, 173, 214, 17, 20, 87, 148, 396, 137, 412, 170, 149, 172, 4, 323, 139, 177, 1266, 633, 202, 678,
                              4, 116, 206, 384, 247, 264, 142, 13, 183, 234, 394, 534, 118, 79, 984, 367, 165, 203, 68, 88, 345, 77, 492, 945, 281, 13, 107, 21, 161, 21, 2, 559, 401, 73, 302, 1433, 201, 269, 343, 32, 39, 18, 90, 37, 90, 97, 64, 139, 207, 4, 846, 175, 237, 96, 119, 197,
                              525, 567, 214, 132, 121, 75, 211, 68, 181, 6, 163, 138, 153, 1188, 323, 1410, 302, 0, 31, 392, 214, 39, 220, 167, 991, 2810, 178, 9, 1910, 53, 276, 223, 0, 168, 141, 1309, 1136, 57, 122, 695, 542, 8, 54, 101, 190, 8, 58, 51, 10, 52, 175, 407, 151, 103, 27,
                              223, 74, 9, 75, 20, 109, 7, 43, 42, 60, 139, 19, 242, 184, 11, 0, 118, 133, 7, 105, 162, 6, 117, 12, 33, 106, 15, 99, 96, 101, 360, 234, 40, 330, 36, 521, 97, 3, 89, 285, 14, 13, 238, 117, 267, 148, 61, 139, 44, 218, 198, 64, 42, 133, 3, 14, 230, 256, 88,
                              385, 627, 294, 641, 437, 89, 66, 34, 0, 239, 7, 236, 24, 340, 557, 114, 149, 460, 440, 679, 479, 233, 147, 74, 201, 95, 1695, 62, 75, 389, 93, 2385, 4, 55, 111, 225, 629, 81, 1037, 721, 623, 1167, 106, 131, 24, 24, 584, 218, 581, 74, 88, 129, 907, 137, 271,
                              274, 23, 204, 72, 8, 326, 90, 186, 1, 283, 736, 761, 94, 237, 315, 148, 126, 161, 3, 565, 111, 40, 71, 177, 261, 76, 89, 103, 135, 328, 1812, 587, 195, 264, 74, 891, 7, 843, 211, 31, 86, 572, 420, 246, 179, 192, 52, 126, 12, 190, 277, 125, 77, 101, 130, 100,
                              158, 2, 283, 186, 434, 179, 107, 815, 95, 73, 33, 57, 41, 197, 105, 141, 268, 246, 2, 103, 72, 1034, 98, 262, 22, 35, 163, 18, 103, 154, 448, 50, 857, 181, 42, 61, 65, 296, 224, 301, 28, 55, 83, 252, 785, 28, 100, 124, 32, 203, 470, 181, 175, 957, 1258, 13]

principal_outstanding_240 = [1606, 1567, 269, 184, 93, 75, 52, 88, 12, 5, 36, 154, 155, 104, 149, 278, 186, 223, 3546, 580, 331, 102, 106, 232, 86, 83, 822, 268, 43, 323, 258, 114, 63, 41, 41, 53, 674, 278, 883, 22, 23, 253, 217, 54, 892, 79, 155, 5, 598, 2, 2112, 54, 0, 32, 20,
                                251, 46, 553, 73, 435, 12, 17, 120, 84, 815, 157, 338, 264, 24, 69, 405, 8, 757, 44, 117, 18, 25, 197, 96, 339, 45, 20, 64, 132, 8, 20, 253, 48, 53, 162, 313, 197, 402, 337, 221, 97, 440, 1000, 549, 3, 72, 260, 114, 6, 111, 109, 61, 115, 104, 72, 889,
                                45, 19, 30, 70, 56, 36, 128, 33, 55, 25, 51, 59, 132, 174, 31, 184, 111, 235, 14, 179, 124, 58, 87, 50, 1333, 137, 157, 21, 148, 41, 45, 203, 12, 5, 42, 6, 66, 62, 50, 406, 20, 24, 166, 164, 58, 240, 26, 38, 15, 66, 192, 365, 153, 312, 88, 2, 69, 121,
                                32, 127, 11, 48, 679, 324, 131, 37, 91, 47, 7, 136, 24, 55, 22, 261, 131, 19, 211, 73, 130, 49, 1, 86, 2, 158, 78, 85, 10, 190, 36, 936, 334, 18, 135, 59, 184, 0, 41, 24, 45, 5, 172, 329, 13, 2, 102, 714, 845, 63, 330, 627, 361, 907, 17, 614, 485, 409,
                                217, 315, 205, 1838, 368, 157, 4, 104, 55, 57, 65, 16, 84, 168, 78, 38, 16, 153, 460, 54, 27, 286, 110, 77, 961, 753, 200, 85, 277, 6, 33, 169, 104, 40, 57, 882, 1018, 150, 3, 21, 502, 53, 9, 320, 876, 192, 156, 581, 209, 409, 91, 2, 598, 131, 323, 139,
                                9, 19, 9, 181, 181, 16, 138, 110, 42, 615, 112, 92, 55, 25, 626, 568, 410, 313, 53, 146, 293, 287, 427, 403, 27, 75, 599, 179, 275, 63, 58, 477, 29, 19, 5, 19, 51, 462, 190, 898, 22, 10, 246, 0, 485, 41, 142, 168, 14, 33, 602, 160, 92, 27, 186, 464, 8,
                                295, 550, 193, 237, 418, 114, 1534, 155, 57, 151, 66, 93, 166, 367, 14, 128, 19, 301, 0, 380, 988, 1458, 675, 162, 267, 20, 46, 243, 159, 9, 1368, 136, 18, 86, 138, 63, 827, 2, 133, 88, 125, 591, 47, 13, 101, 295, 78, 701, 43, 109, 61, 397, 142, 0, 1243,
                                47, 62, 82, 269, 325, 138, 386, 44, 201, 32, 116, 476, 57, 217, 175, 184, 66, 1, 37, 208, 442, 71, 17, 0, 205, 183, 164, 216, 120, 197, 93, 17, 35, 77, 158, 438, 189, 35, 2, 594, 154, 905, 139, 104, 40, 77, 95, 111, 221, 159, 138, 84, 789, 574, 44, 183,
                                140, 4, 276, 928, 82, 279, 26, 179, 65, 564, 106, 150, 180, 22, 99, 724, 1169, 169, 307, 20728, 132, 531, 99, 21, 318, 21, 70, 285, 168, 126, 1, 0, 222, 772, 233, 74, 0, 235, 52, 154, 47, 83, 20, 606, 6, 391, 56, 8, 213, 527, 282, 51, 83, 353, 188, 260,
                                433, 148, 69, 214, 1114, 212, 65, 52, 288, 418, 90, 1070, 67, 72, 167, 4, 391, 954, 12, 767, 91, 222, 9, 8, 57, 299, 935, 4, 79, 117, 103, 82, 194, 35, 83, 40, 89, 188, 907, 627, 42, 55, 93, 161, 638, 237, 201, 156, 84, 259, 165, 135, 89, 54, 350, 47, 13,
                                42, 89, 94, 146, 186, 33, 85, 377, 361, 166, 0, 219, 284, 114, 43, 389, 140, 212, 630, 259, 75, 207, 470, 206, 160, 30, 189, 832, 149, 32, 191, 150, 64, 325, 379, 317, 22, 140, 442, 86, 149, 762, 177, 124, 124, 42, 122, 88, 28, 55, 411, 61, 65, 1041, 96,
                                142, 14, 337, 302, 404, 164, 228, 67, 163, 437, 176, 78, 124, 1495, 426, 54, 121, 223, 66, 55, 30, 126, 3, 306, 1081, 350, 269, 131, 125, 31, 265, 349, 178, 1, 203, 43, 660, 2955, 255, 529, 672, 141, 573, 489, 455, 70, 160, 62, 247, 79, 108, 171, 209, 31,
                                106, 410, 232, 1046, 161, 628, 6, 31, 82, 96, 145, 55, 66, 485, 186, 74, 227, 129, 18, 144, 233, 301, 141, 29, 2, 402, 73, 65, 15, 194, 89, 172, 165, 82, 300, 173, 214, 17, 20, 87, 148, 396, 137, 412, 170, 149, 172, 4, 323, 139, 177, 1266, 633, 202, 678,
                                4, 116, 206, 384, 247, 264, 142, 13, 183, 234, 394, 534, 118, 79, 984, 367, 165, 203, 68, 88, 345, 77, 492, 945, 281, 13, 107, 21, 161, 21, 2, 559, 401, 73, 302, 1433, 201, 269, 343, 32, 39, 18, 90, 37, 90, 97, 64, 139, 207, 4, 846, 175, 237, 96, 119, 197,
                                525, 567, 214, 132, 121, 75, 211, 68, 181, 6, 163, 138, 153, 1188, 323, 1410, 302, 0, 31, 392, 214, 39, 220, 167, 991, 2810, 178, 9, 1910, 53, 276, 223, 0, 168, 141, 1309, 1136, 57, 122, 695, 542, 8, 54, 101, 190, 8, 58, 51, 10, 52, 175, 407, 151, 103, 27,
                                223, 74, 9, 75, 20, 109, 7, 43, 42, 60, 139, 19, 242, 184, 11, 0, 118, 133, 7, 105, 162, 6, 117, 12, 33, 106, 15, 99, 96, 101, 360, 234, 40, 330, 36, 521, 97, 3, 89, 285, 14, 13, 238, 117, 267, 148, 61, 139, 44, 218, 198, 64, 42, 133, 3, 14, 230, 256, 88,
                                385, 627, 294, 641, 437, 89, 66, 34, 0, 239, 7, 236, 24, 340, 557, 114, 149, 460, 440, 679, 479, 233, 147, 74, 201, 95, 1695, 62, 75, 389, 93, 2385, 4, 55, 111, 225, 629, 81, 1037, 721, 623, 1167, 106, 131, 24, 24, 584, 218, 581, 74, 88, 129, 907, 137, 271,
                                274, 23, 204, 72, 8, 326, 90, 186, 1, 283, 736, 761, 94, 237, 315, 148, 126, 161, 3, 565, 111, 40, 71, 177, 261, 76, 89, 103, 135, 328, 1812, 587, 195, 264, 74, 891, 7, 843, 211, 31, 86, 572, 420, 246, 179, 192, 52, 126, 12, 190, 277, 125, 77, 101, 130, 100,
                                158, 2, 283, 186, 434, 179, 107, 815, 95, 73, 33, 57, 41, 197, 105, 141, 268, 246, 2, 103, 72, 1034, 98, 262, 22, 35, 163, 18, 103, 154, 448, 50, 857, 181, 42, 61, 65, 296, 224, 301, 28, 55, 83, 252, 785, 28, 100, 124, 32, 203, 470, 181, 175, 957, 1258, 13]

strings = [[1606, 1567, 269, 184, 93, 75, 52, 88, 12, 5, 36, 154, 155, 104, 149, 278, 186, 223, 3546, 580, 331, 102, 106, 232, 86, 83, 822, 268, 43, 323, 258, 114, 63, 41, 41, 53, 674, 278, 883, 22, 23, 253, 217, 54, 892, 79, 155, 5, 598, 2, 2112, 54, 0, 32, 20,
                                251, 46, 553, 73, 435, 12, 17, 120, 84, 815, 157, 338, 264, 24, 69, 405, 8, 757, 44, 117, 18, 25, 197, 96, 339, 45, 20, 64, 132, 8, 20, 253, 48, 53, 162, 313, 197, 402, 337, 221, 97, 440, 1000, 549, 3, 72, 260, 114, 6, 111, 109, 61, 115, 104, 72, 889,
                                45, 19, 30, 70, 56, 36, 128, 33, 55, 25, 51, 59, 132, 174, 31, 184, 111, 235, 14, 179, 124, 58, 87, 50, 1333, 137, 157, 21, 148, 41, 45, 203, 12, 5, 42, 6, 66, 62, 50, 406, 20, 24, 166, 164, 58, 240, 26, 38, 15, 66, 192, 365, 153, 312, 88, 2, 69, 121,
                                32, 127, 11, 48, 679, 324, 131, 37, 91, 47, 7, 136, 24, 55, 22, 261, 131, 19, 211, 73, 130, 49, 1, 86, 2, 158, 78, 85, 10, 190, 36, 936, 334, 18, 135, 59, 184, 0, 41, 24, 45, 5, 172, 329, 13, 2, 102, 714, 845, 63, 330, 627, 361, 907, 17, 614, 485, 409,
                                217, 315, 205, 1838, 368, 157, 4, 104, 55, 57, 65, 16, 84, 168, 78, 38, 16, 153, 460, 54, 27, 286, 110, 77, 961, 753, 200, 85, 277, 6, 33, 169, 104, 40, 57, 882, 1018, 150, 3, 21, 502, 53, 9, 320, 876, 192, 156, 581, 209, 409, 91, 2, 598, 131, 323, 139,
                                295, 550, 193, 237, 418, 114, 1534, 155, 57, 151, 66, 93, 166, 367, 14, 128, 19, 301, 0, 380, 988, 1458, 675, 162, 267, 20, 46, 243, 159, 9, 1368, 136, 18, 86, 138, 63, 827, 2, 133, 88, 125, 591, 47, 13, 101, 295, 78, 701, 43, 109, 61, 397, 142, 0, 1243,
                                47, 62, 82, 269, 325, 138, 386, 44, 201, 32, 116, 476, 57, 217, 175, 184, 66, 1, 37, 208, 442, 71, 17, 0, 205, 183, 164, 216, 120, 197, 93, 17, 35, 77, 158, 438, 189, 35, 2, 594, 154, 905, 139, 104, 40, 77, 95, 111, 221, 159, 138, 84, 789, 574, 44, 183,
                                433, 148, 69, 214, 1114, 212, 65, 52, 288, 418, 90, 1070, 67, 72, 167, 4, 391, 954, 12, 767, 91, 222, 9, 8, 57, 299, 935, 4, 79, 117, 103, 82, 194, 35, 83, 40, 89, 188, 907, 627, 42, 55, 93, 161, 638, 237, 201, 156, 84, 259, 165, 135, 89, 54, 350, 47, 13,
                                42, 89, 94, 146, 186, 33, 85, 377, 361, 166, 0, 219, 284, 114, 43, 389, 140, 212, 630, 259, 75, 207, 470, 206, 160, 30, 189, 832, 149, 32, 191, 150, 64, 325, 379, 317, 22, 140, 442, 86, 149, 762, 177, 124, 124, 42, 122, 88, 28, 55, 411, 61, 65, 1041, 96,
                                142, 23423234545, 14, 337, 302, 404, 164, 228, 67, 163, 437, 176, 78, 124, 1495, 426, 54, 121, 223, 66, 55, 30, 126, 3, 306, 1081, 350, 269, 131, 125, 31, 265, 349, 178, 1, 203, 43, 660, 2955, 255, 529, 672, 141, 573, 489, 455, 70, 160, 62, 247, 79, 108, 171, 209, 31],
           [32, 127, 11, 48, 679, 324, 131, 37, 91, 47, 7, 136, 24, 55, 22, 261, 131, 19, 211, 73, 130, 49, 1, 86, 2,
           158, 78, 85, 10, 190, 36, 936, 334, 18, 135, 59, 184, 0, 41, 24, 45, 5, 172, 329, 13, 2, 102, 714, 845, 63,
           330, 627, 361, 907, 17, 614, 485, 409,
           217, 315, 205, 1838, 368, 157, 4, 104, 55, 57, 65, 16, 84, 168, 78, 38, 16, 153, 460, 54, 27, 286, 110, 77,
           961, 753, 200, 85, 277, 6, 33, 169, 104, 40, 57, 882, 1018, 150, 3, 21, 502, 53, 9, 320, 876, 192, 156, 581,
           209, 409, 91, 2, 598, 131, 323, 139,
           295, 550, 193, 237, 418, 114, 1534, 155, 57, 151, 66, 93, 166, 367, 14, 128, 19, 301, 0, 380, 988, 1458, 675,
           162, 267, 20, 46, 243, 159, 9, 1368, 136, 18, 86, 138, 63, 827, 2, 133, 88, 125, 591, 47, 13, 101, 295, 78,
           701, 43, 109, 61, 397, 142, 0, 1243,
           47, 62, 82, 269, 325, 138, 386, 44, 201, 32, 116, 476, 57, 217, 175, 184, 66, 1, 37, 208, 442, 71, 17, 0,
           205, 183, 164, 216, 120, 197, 93, 17, 35, 77, 158, 438, 189, 35, 2, 594, 154, 905, 139, 104, 40, 77, 95, 111,
           221, 159, 138, 84, 789, 574, 44, 183]]



pp = ["2015-06-02 02:48:34",
	"2015-06-13 14:25:17",
	"2015-09-28 03:07:16",
	"2015-08-21 20:23:43",
	"2015-08-20 15:01:50",
	"2015-08-19 14:08:00",
	"2015-08-09 23:10:09",
	"2015-08-06 00:51:28",
	"2015-11-19 03:39:11",
	"2015-08-23 19:27:49",
	"2015-11-26 15:05:52",
	"2015-07-09 12:27:03",
	"2015-05-08 05:40:58",
	"2015-01-13 20:33:05",
	"2015-03-15 00:01:09",
	"2015-02-09 16:04:12",
	"2015-10-14 17:48:47",
	"2015-08-14 02:52:37",
	"2015-08-19 01:19:40",
	"2015-08-14 09:51:00",
	"2015-08-09 16:44:45",
	"2015-08-18 12:12:23",
	"2015-08-10 13:36:59",
	"2015-08-11 11:06:27",
	"2015-08-26 04:54:43"]

data = [['Id',
  'Year',
  'Id',
  'Sex',
  'Id',
  'Hispanic Origin',
  'Id',
  'Id2',
  'Geography',
  'Total',
  'Race Alone - White',
  'Race Alone - Hispanic',
  'Race Alone - Black or African American',
  'Race Alone - American Indian and Alaska Native',
  'Race Alone - Asian',
  'Race Alone - Native Hawaiian and Other Pacific Islander',
  'Two or More Races'],
 ['cen42010',
  'April 1, 2010 Census',
  'totsex',
  'Both Sexes',
  'tothisp',
  'Total',
  '0100000US',
  '',
  'United States',
  '308745538',
  '197318956',
  '44618105',
  '40250635',
  '3739506',
  '15159516',
  '674625',
  '6984195']]


tt = numpy.array(data)

# print tt.shape
# print tt.ndim
# print type(tt)

strings = [[201,2,23,4,25,6,7],
           [48,69,710,100,911,102,3],
           [8,9,10,100,11,52,13]]

strings_np = numpy.array(strings)
print strings_np.shape[0]
strings_np_bool = strings_np > 50
zeros_vert = numpy.zeros([strings_np.shape[0], 1], int)
zeros_hor = numpy.zeros(strings_np.shape[1], int)
# zeros_hor = numpy.zeros([1,strings_np.shape[1]], int)
zeros_hor = numpy.expand_dims(zeros_hor,axis = 0)
print zeros_vert
print
print zeros_hor

print strings_np.max(axis = 0)
print strings_np.max(axis = 1)

# print numpy.concatenate([strings_np, zeros_vert], axis=1)
# print numpy.concatenate([strings_np, zeros_hor])



# print strings_np_bool
# print strings_np[strings_np_bool]


exit()
# february_bool = pickup_month == 2
# february = pickup_month[february_bool]
# february_rides = february.shape[0]
#
# march_bool = pickup_month == 3
# march = pickup_month[march_bool]
# march_rides = march.shape[0]
#
# def month_rides(month_num):
#     bool = pickup_month == month_num
#     month = pickup_month[bool]
#     month_rides = month.shape[0]
#
#     return month_rides

print
strings2 = [[201,2,23,4,25,6,7]]
strings2_np = numpy.array(strings2)
# print strings2_np[:,1]



print
taxi = [[ 2016, 1, 1, 5, 0, 2, 4, 21, 2037, 52, 0.8, 5.54, 11.65, 69.99, 1],
       [ 2016, 2, 1, 5, 0, 2, 1, 16.29, 1520, 45, 1.3, 0, 8, 54.3, 1],
       [ 2016, 4, 1, 5, 0, 2, 6, 12.7, 1462, 36.5, 1.3, 0, 0, 37.8, 2],
       [ 2016, 10, 1, 5, 0, 2, 6, 8.7, 1210, 26, 1.3, 0, 5.46, 32.76, 1],
       [ 2016, 6, 1, 5, 0, 2, 6, 5.56, 759, 17.5, 1.3, 0, 0, 18.8, 2]]

taxi_np = numpy.array(taxi)

pickup_month = taxi_np[:,1]
print pickup_month

def month_rides(month_num):
    bool = pickup_month == month_num
    month = pickup_month[bool]
    month_rides = month.shape[0]

    return bool

february_rides = month_rides(2)
march_rides = month_rides(3)

print february_rides

exit()

# print (taxi_np[0,8])
trip_mph = taxi_np[:,7] / taxi_np[:,8] * 3600
print trip_mph
tip_amount = taxi_np[:,13]

print
print
print tip_amount
cleaned_taxi = taxi[trip_mph < 100]
# print cleaned_taxi
mean_distance = taxi_np[:7].mean()
# print mean_distance
mean_length = taxi_np[:8].mean()
mean_total_amount = taxi_np[:13].mean()
mean_mph = trip_mph.mean()
print mean_mph



print "vége"
print
print
tip_amount_bool = tip_amount > 50
# print tip_amount_bool
# print tip_amount_bool.shape[0]
top_tips = taxi_np[tip_amount_bool,2]
# print top_tips


ee = 0
taxi_np[0] = 2222222
# print
# print taxi_np[:,ee]

print
kkk = strings_np[strings_np[:,6] == 3]
print kkk
print kkk.shape[0]

# pickup_code_2 = taxi_modified[:,5] == 2
# pickup_code_3 = taxi_modified[:,5] == 3
# pickup_code_5 = taxi_modified[:,5] == 5
#
# taxi_modified[pickup_code_2,15] = 1
# taxi_modified[pickup_code_3,15] = 1
# taxi_modified[pickup_code_5,15] = 1

# print strings_np.shape
# print strings_np.ndim
# print type(strings_np)
# print strings_np.max(axis = 0)
# print len(strings_np.max(axis = 0))

# print strings_np[0:2,2:6]
# print strings_np.mean(axis = 0)


# pp_np = numpy.array(pp)
# print pp_np
# print numpy.argsort(pp_np)
# print pp_np[numpy.argsort(pp_np)]










# intents = [row[3] for row in data]
# print (intents)
# sex_counts = {}
# for sex in intents:
#     if sex in sex_counts:
#         sex_counts[sex] += 1
#     else:
#         sex_counts[sex] = 1
# print (sex_counts)



exit()
race_counts = {'Asian/Pacific Islander': 1326,
 'Black': 23296,
 'Hispanic': 9022,
 'Native American/Native Alaskan': 917,
 'White': 66237}
for key, value in race_counts.items():
    pass


races = data[0]
nums = data[1]
mapping = {}
total_num = 0
for i, race in enumerate(races):
    if 16 > i > 9:
        race_mod = race.replace("Race Alone - ", "")

        if race_mod.startswith("Black"): race_mod = "Black"
        if race_mod.startswith("Native") or race_mod.startswith("Asian"):
            race_mod = "Asian/Pacific Islander"

        if race_mod.startswith("American"): race_mod = "Native American/Native Alaskan"

        if race_mod in mapping:
            mapping[race_mod] += int(nums[i])
        else:
            mapping[race_mod] = int(nums[i])

        total_num += mapping[race_mod]

total_num = 0
for m in mapping:
    total_num += mapping[m]

race_per_hundredk = {}
for race in race_counts:
    # print  race_counts[race], mapping[race]
    race_per_hundredk[race] = float(1/(mapping[race] / race_counts[race])) * 10000

print (race_per_hundredk)















exit()
sexes = [row[5] for row in data]
sex_counts = {}
for sex in sexes:
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1

print (sex_counts)


races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

print (race_counts)

# for post in posts:
#     new_post = float(post[2])
#     dt = datetime.datetime.fromtimestamp(new_post)
#     post[2] = dt

kirks_birthday = datetime.datetime(2233, 3, 22)
print kirks_birthday

exit()
mystery_date = datetime.datetime(2015, 12, 31)
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print (mystery_date_formatted_string)

exit()
kirks_birthday = datetime.datetime(2233, 3, 22)
print kirks_birthday
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff

exit()
today = datetime.datetime.now()
print today
diff = datetime.timedelta(weeks = 3, days = 2, hours = 0)
print diff
future = today + diff
print future







exit()
current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month

print current_datetime
print current_year
print current_month

print
print

exit()
current_time = time.time()
current_struct_time = time.gmtime(current_time)
print current_time, type(current_time)
print current_struct_time, type(current_struct_time)

print
print current_struct_time.tm_hour

for t in current_struct_time:
    pass
    # print t

exit()
strings_st = []
for s in strings:
    strings_st.append(str(s))
# print strings_st

years = []
for st in strings_st:
    if (re.findall('[0-2][0-9][0-9][0-9]', st)):
        years.append(st)
print years


exit()
year_strings = []
for st in strings:
    if re.search('[0-2][0-9][0-9][0-9]', str(st)) is not None:
        year_strings.append(st)

print year_strings

exit()

# for post in posts:
#     post[0] = re.sub("[\(\[][sS]erious\][\)\]]", "[Serious]", post[0])

exit()

serious_count = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count += 1

exit()
total = 10
def find_total(column, valami = "def"):
    # total = 20
    # total = total + sum(column)
    return type(total)

print(find_total(principal_outstanding_240))






exit()

nfl = open("nfl_suspensions_data.csv", 'r')
csv_file = csv.reader(nfl)
nfl_suspensions = list(csv_file)
nfl_suspensions = nfl_suspensions[1:]

#----------------------------------------------------------

class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except:
            self.year = 0


    def get_year(self):
        return self.year

third_suspension = Suspension(nfl_suspensions[2])
missing_year = Suspension(nfl_suspensions[22])

twenty_third_year = missing_year.get_year()
print twenty_third_year








exit()

teams = [row[1] for row in nfl_suspensions]
unique_teams = set(teams)
print (unique_teams)

games = [row[2] for row in nfl_suspensions]
unique_games = set(games)
print (unique_games)

exit()

years ={}
for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1

print (years)



exit()

legislators_old = [
 ['1994-01-23', 1, 2, 7, 7772],
 ['1996-01-23', 1, 3, 1, 10142],
 ['1997-01-23', 1, 4, 2, 11248],
 ['1994-01-23', 1, 5, 3, 11053],
 ['1990-01-23', 1, 6, 4, 11406],
 ['1990-01-23', 1, 7, 5, 11251],
 ['1992-01-23', 1, 8, 6, 8653],
 ['1994-01-23', 1, 9, 7, 7910],
 ['1994-01-23', 1, 10, 1, 10498]]

with open("legislators_4.txt", 'r') as leg:
    # legislators = leg.readlines()

    csv_file = csv.reader(leg)
    legislators = list(csv_file)


top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and int(row[7]) > 1740:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[row[1]] += 1
        else:
            male_name_counts[row[1]] = 1

highest_male_count = None
for key, value in male_name_counts.items():
    if highest_male_count is None or value > highest_male_count:
        highest_male_count = value


for key, value in male_name_counts.items():
    if value == highest_male_count:
        top_male_names.append(key)






exit()

name_counts = {}
for row in legislators:
    if row[3] == "M" and int(row[7]) > 1740:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

print name_counts

exit()

for row in legislators:
    date = row[0]
    try:
        birth_year = int(date.split("-")[0])
    except:
        birth_year = 0

    row.append(birth_year)

print legislators

exit()

converted_years = []
for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except:
        pass

exit()

try:
    int('ss')
except Exception as exc:
    print(type(exc))
    print str(exc)


exit()

birth_years = []
for row in legislators:
    date = row[2]
    parts = date.split("-")
    birth_years.append(parts)

print (birth_years[0])


exit()

with open("legislators.csv", "r") as f:
    csv_file = csv.reader(f)
    data = list = (csv_file)
    gender = []
    for i, row in enumerate(data):
        if i > 0:
            gender.append(row[3])

    gender = set(gender)
    print (gender)

nfl_data = [["year", "week", "winner", "loser", "people"],
 [1994, 1, 2, 7, 7772],
 [1996, 1, 3, 1, 10142],
 [1997, 1, 4, 2, 11248],
 [1994, 1, 5, 3, 11053],
 [1990, 1, 6, 4, 11406],
 [1990, 1, 7, 5, 11251],
 [1992, 1, 8, 6, 8653],
 [1994, 1, 9, 7, 7910],
 [1994, 1, 10, 1, 10498]]


class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    # def __str__(self):
    #     res = ""
    #     for i, row in enumerate(self.data):
    #         if i < 11:
    #             res += "".join(str(row))
    #     return res

    def __str__(self):
        data_string = self.data[:10]
        return str(data_string)


    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column


    # Add your count unique method here
    def count_unique(self, label):
        return len(set(self.column(label)))

nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')
print year_column
print player_column
print nfl_dataset.count_unique('year')

print nfl_dataset

exit()

cdc_list = [[1994, 1, 1, 6, 8096],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 3, 1, 10142],
 [1994, 1, 4, 2, 11248],
 [1994, 1, 5, 3, 11053],
 [1994, 1, 6, 4, 11406],
 [1994, 1, 7, 5, 11251],
 [1994, 1, 8, 6, 8653],
 [1994, 1, 9, 7, 7910],
 [1994, 1, 10, 1, 10498]]

def month_births(list_name):
    births_per_month = {}

    for dd in list_name:
        print dd

        if dd[1] in births_per_month:
            births_per_month[dd[1]] += int(dd[4])
        else:
            births_per_month[dd[1]] = int(dd[4])

    return births_per_month


cdc_month_births = month_births(cdc_list)
print (cdc_month_births)


def dow_births(list_name):
    cdc_day_births = {}

    for dd in list_name:
        if dd[3] in cdc_day_births:
            cdc_day_births[dd[3]] += int(dd[4])
        else:
            cdc_day_births[dd[3]] = int(dd[4])

    return cdc_day_births


cdc_day_births = dow_births(cdc_list)
print (cdc_day_births)




cdc_month_births = month_births(cdc_list)
print (cdc_month_births)


def calc_counts(list_name, col_num):
    sum_dict = {}

    for dd in list_name:
        if dd[col_num] in sum_dict:
            sum_dict[dd[col_num]] += int(dd[4])
        else:
            sum_dict[dd[col_num]] = int(dd[4])

    return sum_dict


sum_dict = calc_counts(cdc_list, 3)
print (sum_dict)

