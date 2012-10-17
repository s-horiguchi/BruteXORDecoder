# BruteXORDecoder
## What's this?
与えられたバイナリファイルを、0x00〜0xFFでXORして、fileコマンドに渡し、結果を表示します。

    $ python BruteXORDecoder.py
    Usage: ./BruteXORDecoder.py [options] FILE_PATH
    
    Options:
      -h, --help            show this help message and exit
      -s CODE, --single-mode=CODE
                            not-bruteforce mode. just XOR the file with the
                            number<CODE>.
      -o, --overwrite       not save XORed file.(finally original file will be
                            restored)
      -d SAVEDIR, --save-directory=SAVEDIR
                            set the directory where xor-ed/checked file will be
                            saved.(default is 'xor_<FILENAME>')


デフォルトでは、fileコマンドの結果が`data`以外のときは`xor_<FILE名>`という名前のディレクトリ以下にそのファイルをコピーします。

CTFとかでXORでエンコードってよくあるよねーっていうことで作りました。
本来の解き方ではないと思うので普通に解きましょう。

fileコマンドで何らかのファイルとして認識されても、たまたまシグネチャが合っちゃったけど実際のファイルフォーマットのパラメータはめちゃくちゃなもの、ってのがほとんどです。
