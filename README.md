# Fibonacci
フィボナッチ数を返すAPIサービスの開発

## 使い方
1. ``` uvicorn main:app --reload ```
2. ``` curl -X 'GET' 'http://127.0.0.1:8000/fib?n=1000' -H 'accept: application/json'  ```
  →この場合はn = 1000で入力