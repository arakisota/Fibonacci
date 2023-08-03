# Fibonacci
フィボナッチ数を返すAPIサービスの開発

## フィボナッチ数
最初の二項が1で、第三項以降の項がすべて直前の二項の和になっている数列です。例として 次のように1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...のような数列となる。

## 使い方
1. ``` uvicorn main:app --reload ```
2. ``` curl -X 'GET' 'http://127.0.0.1:8000/fib?n=1000' -H 'accept: application/json'  ```
  →この場合はn = 1000で入力