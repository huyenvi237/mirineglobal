"""
Exception Errorsのリスト：
    - IOError: ファイルの名前また場所が違う
    - KeyboardInterrupt: ユーザ自身が実行しているプログラムを停止したいと
            Ctrl+C/ Ctrl+Zを入力します。この停止の処理を行なっているのが、KeyboardInterrupt 例外になります。
    - ValueError: 関数の引数に対して関数が処理できない値を渡してしまうことで発生するエラー。
    - EOFError: 実行しているinput()を停止するため Ctrl+Dを入力します。そのとき　EOFError(end-of-file)が発生します。
    - NameError: localまたglobal valueが見つけない。
    (RuntimeError, TypeError, ZeroDivisionError....)
"""

import sys

randomList = ['a', 0, 2]

for nhap in randomList:
    try:
        print("Phần tử:", nhap)
        r = 1/int(nhap)
        break
    except ValueError:
        print("Exception: ",sys.exc_info()[0])
        print("Go to next element.")
    except ZeroDivisionError:
        print("Exception: ", sys.exc_info()[0])
        print("Go to next element.")
    finally:
        print('Next!')

print()