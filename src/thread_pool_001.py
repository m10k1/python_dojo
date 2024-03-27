# ThreadPoolの実行例
# 関数を複数のスレッドに分けて実行できる
# ThreadPoolを使うとユーザーはスレッドを直接管理する必要がなくなる
# 関数をsubmitメソッドを通じてThreadPoolExecutorに渡すだけでよい
# Futureオブジェクトを返し、このオブジェクトを通じて非同期処理の結果を取得
# タスクの完了を待つことができる

from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * 2


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(10)]

    for future in futures:
        print(future.result())

