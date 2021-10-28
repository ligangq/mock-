# -*- coding: utf-8 -*-
import csv


def write_csv(name, password):
    path = "result.csv"
    with open(path, 'a+', newline='') as f:
        csv_write = csv.writer(f)
        data_row = [name, password]
        csv_write.writerow(data_row)
        
        
def read_open(name,password):
    path = "result.csv"
    with open("result.csv",'r',encoding='UTF-8')as f:
        read=csv.reader(f)
        for row in read:
            if name in row and password in row:
                return True



            
