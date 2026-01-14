from rnn_frame import RNN_frame
from transformer_frame import Transformer_frame

e = Transformer_frame()

#e = RNN_frame()

#e.init_model(save=True)

e.load_model('./saved/transformer0114055250_epoch_30.pt',save=False)

#e.load_model('./saved/rnn0114081515_epoch_15.pt',save=False)

#e.evaluate()

#e.train(n_epochs=5)

e.test( e.valid_pairs[0:10] , show=True, strategy='greedy' , noref=False)

e.test( [
    "我 爱 自然 语言 处理 。",
     "今天 天气 很 好 。" ,
     "你 真的 会 思考 吗 ？"
     ], show=True, strategy='beam' , noref=True)
