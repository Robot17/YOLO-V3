# YOLO-V3
- 借鉴自网络：https://blog.csdn.net/demm868/article/details/103052307?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-9
## 数据集的准备
- 将train数据集与test数据集分别命名为cartoon_train和cartoon_test放在dataset文件夹下
- 运行data_prepare.py将数据集划为训练集，验证集，并满足输入格式
## 训练模型
- 加载权重，将权重h5文件放入models文件夹
- 最新权重下载地址：https://pan.baidu.com/s/1QKODAhRU_Rw5lpf8NcIR4g
- 最新训练权重/模型下载地址：https://drive.google.com/drive/folders/1qY18oFpBfrywnJyr9WuvzQLsdGFEVjHa?usp=sharing
- 本次作业采用的是将上述链接的最新权重作为预训练，然后以作业数据为数据集训练出自己的模型
- 运行train.py
## 预测
- 加载权重，将训练好的权重h5文件放入models文件夹
- 运行run.py，对数据集进行预测输出，输出在dataset/my_test.txt中
- 如果需要保存输出图片的话，可保存在output/文件夹
- 预测新的图片
## 环境说明
- tensorflow-gpu==1.9.0
- keras==2.2.0
- 貌似只要不是tensorflow2以上就好
