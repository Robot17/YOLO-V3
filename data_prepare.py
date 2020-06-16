#!/usr/bin/env python
# -- coding: utf-8 --
"""
Copyright (c) 2018. All rights reserved.
Created by C. L. Wang on 2018/6/14
"""
import os

train_bbx_file = 'dataset/train.txt'
out_file='dataset/new_train.txt'

train_data_folder = 'dataset/cartoon_train/'
my_val_file = 'dataset/my_val.txt'
my_train_file='dataset/my_train.txt'

def split_to_train_and_val(file,my_train_file,my_val_file,total,num):
    if os.path.exists(my_val_file):
        os.remove(my_val_file)
    if os.path.exists(my_train_file):
        os.remove(my_train_file)
    data_lines=read_file(file)
    line=""
    num1=0
    num2=0
    for data_line in data_lines:
        data_line = data_line.strip('\n')
        if line=="":
            line=data_line
            num1=int(line.split(' ')[0].split('/')[-1].split('.')[0])
            continue
        num2=int(data_line.split(' ')[0].split('/')[-1].split('.')[0])
        if num1==num2:
            line+=" "+data_line.split(' ')[1]
        else:
            if num1<=6000:
                write_line(my_train_file,line)
            else:
                write_line(my_val_file,line)
            line=data_line
            num1=num2
    if num1 <= 6000:
        write_line(my_train_file, line)
    else:
        write_line(my_val_file, line)
    return

def generate_train_file(bbx_file, data_folder, out_file):
    os.remove(out_file)
    data_lines = read_file(bbx_file)
    for data_line in data_lines:
        data_line=data_line.strip('\n')
        data_line=train_data_folder+data_line+',0'
        lines=data_line.split(',',1)
        write_line(out_file,lines[0]+' '+lines[1])
        continue




def read_file(data_file, mode='more'):
    """
    读文件, 原文件和数据文件
    :return: 单行或数组
    """
    try:
        with open(data_file, 'r') as f:
            if mode == 'one':
                output = f.read()
                return output
            elif mode == 'more':
                output = f.readlines()
                # return map(str.strip, output)
                return output
            else:
                return list()
    except IOError:
        return list()


def write_line(file_name, line):
    """
    将行数据写入文件
    :param file_name: 文件名
    :param line: 行数据
    :return: None
    """
    if file_name == "":
        return
    with open(file_name, "a+") as fs:
        if type(line) is (tuple or list):
            fs.write("%s\n" % ", ".join(line))
        else:
            fs.write("%s\n" % line)


if __name__ == '__main__':
    generate_train_file(train_bbx_file, train_data_folder, out_file)
    split_to_train_and_val(out_file,my_train_file,my_val_file,8000,6000)
