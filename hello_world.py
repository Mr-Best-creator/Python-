# ライブラリ、モジュールを使う方法(import分)
# 標準。外部関係なく使えます
import tkintr # import ライブラリ名
import tkinter as tk # import ライブラリ名 as 省略名
import tkinter, os, re # import ライブラリ名1, ライブラリ名2, ライブラリ名3
from tkinter import ttk # frome ライブラリ名 import モジュール名
from multiprocessing import Process, Queue #fromから始まるimport文でも複数まとめてインポートできる


print("Hello world!")

# 実行するとコンソールに表示される↓
# >>> Hello world!
