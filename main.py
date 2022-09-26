import random
from datetime import datetime
import time

RR = {}


def gen_R(RR):
    random.seed()
    for i in range(0, 256):
        RR[i] = int(random.uniform(0, 256) // 1)
    return RR


RR = gen_R(RR)


def R(ki):
    return RR[(ki)]


def CRC(ki):
    h = 0
    for i in range(0, len(ki)):
        ki_1 = ord(ki[i])
        highorder = h & 0xf8000000
        h = h << 5
        h = h ^ (highorder >> 27)
        h = (h ^ (ki_1))
    return h


def PJW(ki):
    h = 0
    for i in range(0, len(ki)):
        ki_1 = ord(ki[i])
        h = (h << 4) + ki_1
        g = h & 0xf0000000
        if g != 0:
            h = h ^ (g >> 24)
            h = h ^ g
    return h


def BUZ (ki):
    h = 0
    for i in range(0, len(ki)):
        ki_1 = ord(ki[i])
        highorder = h & 0x80000000
        h = h << 1
        h = h ^ (highorder >> 31)
        h = h ^ R(ki_1)
    return h

def file_reader(p, v):

    list_f = []
    for i in range(0, (v+1)):
        name = str(i) + ".txt"
        list_f.append((p + name))
    return list_f

def find_duplicates(files: list[str], hash_function: callable) -> list[str]:

    time_v = datetime.now()
    h_list = []
    hash_res = []
    coll_v = 0

    for i in range(0, 500):
        name = str(i) + ".txt"
        f = open("out\\" + name)
        line = f.readline()
        while (line != ""):
            if line != "\n":
                hash_res.append(hash_function(line.split('\n')[0]))
            line = f.readline()
        if hash_res in h_list:
            coll_v += 1
        else:
            h_list.append(hash_res)
            hash_res = []

    time_v = datetime.now() - time_v
    print("Количество дубликатов - " + str(coll_v))
    print("Время работы - " + str(time_v))

print()
print("Встроенная фунция - hash")
find_duplicates((file_reader("out\\", 499)), hash)
print()
print("--------------------------------------------")
print()
print("Хэш фунция - CRC")
find_duplicates((file_reader("out\\", 499)), CRC)
print()
print("--------------------------------------------")
print()
print("Хэш фунция - PJW")
find_duplicates((file_reader("out\\", 499)), PJW)
print()
print("--------------------------------------------")
print()
print("Хэш фунция - BUZ")
find_duplicates((file_reader("out\\", 499)), BUZ)
print()
print("--------------------------------------------")

