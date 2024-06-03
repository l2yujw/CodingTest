# 멀티 쓰레딩(threading) 환경에서 사용되며, 내부적으로 라킹(locking)을 지원
from queue import Queue

que = Queue()

# 추가
que.put(1)

# 삭제
que.get()