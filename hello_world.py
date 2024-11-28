# ライブラリ、モジュールを使う方法(import分)
# 標準。外部関係なく使えます
import tkintr # import ライブラリ名
import tkinter as tk # import ライブラリ名 as 省略名
import tkinter, os, re # import ライブラリ名1, ライブラリ名2, ライブラリ名3
from tkinter import ttk # frome ライブラリ名 import モジュール名
from multiprocessing import Process, Queue #fromから始まるimport文でも複数まとめてインポートできる
# ローカルからインポートする場合
import my.my1 #myというフォルダのmy1.pyファイルをインポートする　フォルダの区切り文字は.(ドット)
from my import my1 #こちらでも可

# 使い方
# ライブラリ名.クラス名(引数)
# ライブラリ名.関数名(引数)

print("Hello world!")

# 実行するとコンソールに表示される↓
# >>> Hello world!
