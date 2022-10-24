"""
�������� ��������� ���������� ����� ���������� ������ �������.
"""


# ��������� ����� ���

import time

def decorate(func):
    def log():
        start=time.time()
        func()
        end=time.time()
        all=end-start
        print(all)
    return log



def func_to_decor():
    for i in range(1000):
        print(i)

func_to_decor()