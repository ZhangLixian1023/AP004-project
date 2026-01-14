# 运行python inference.py 一键看到我transformer最佳翻译效果

改一改 inference.py 里面的语句，可以看rnn的翻译效果

还想训练的话，就进 rnn_frame.py 或 transformer_frame.py 设定好模型参数和训练设定，然后在 t.py 里 运行 e.train()

使用方法：在 inference.py 里面写好要执行的操作，然后运行 python  t.py

# 主要模块

utils/preprocess.ipynb: 负责语料清洗、分词及词库生成，词嵌入向量矩阵构建，保存以备主函数使用。

exp_frame.py : Exp_frame 框架类，实验全流程的抽象基类

transfomer_frame.py: Transformer 实验、测试全流程的框架类，继承Exp_frame 

rnn_frame.py:  RNN 实验、测试全流程的框架类，继承Exp_frame

inference.py: 主要入口，可以在里面train，eval，test。

processed_data/: 包含词表和预训练词向量


# 下载 checkpoint:

rnn:【超级会员V1】通过百度网盘分享的文件：rnn0114081515_epoch_15.pt
链接：https://pan.baidu.com/s/1QUDIWxzULGBwauAC5I17rA?pwd=love 
提取码：love

transformer:【超级会员V1】通过百度网盘分享的文件：transformer0114055250_epoch_30.pt
链接：https://pan.baidu.com/s/19a0Ogaa9sMwTCY35YO9YBw?pwd=love 
提取码：love
