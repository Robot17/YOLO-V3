
def evaluate(pre_path,test_path):
    data_lines=read_file(test_path)
    n=0
    np=0
    p=0


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