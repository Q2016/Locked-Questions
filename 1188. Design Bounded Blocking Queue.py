Implement a thread safe bounded blocking queue that has the following methods:

BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
int size() Returns the number of elements currently in the queue.
Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only makes calls to the enqueue method or a consumer thread that only makes calls to the dequeue method. The size method will be called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview.

 

Example 1:

Input:
1
1
["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
[[2],[1],[],[],[0],[2],[3],[4],[]]

Output:
[1,0,2,2]

Explanation:
Number of producer threads = 1
Number of consumer threads = 1

BoundedBlockingQueue queue = new BoundedBlockingQueue(2);   // initialize the queue with capacity = 2.

queue.enqueue(1);   // The producer thread enqueues 1 to the queue.
queue.dequeue();    // The consumer thread calls dequeue and returns 1 from the queue.
queue.dequeue();    // Since the queue is empty, the consumer thread is blocked.
queue.enqueue(0);   // The producer thread enqueues 0 to the queue. The consumer thread is unblocked and returns 0 from the queue.
queue.enqueue(2);   // The producer thread enqueues 2 to the queue.
queue.enqueue(3);   // The producer thread enqueues 3 to the queue.
queue.enqueue(4);   // The producer thread is blocked because the queue's capacity (2) is reached.
queue.dequeue();    // The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
queue.size();       // 2 elements remaining in the queue. size() is always called at the end of each test case.
 

Example 2:

Input:
3
4
["BoundedBlockingQueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","enqueue"]
[[3],[1],[0],[2],[],[],[],[3]]

Output:
[1,0,2,1]

Explanation:
Number of producer threads = 3
Number of consumer threads = 4

BoundedBlockingQueue queue = new BoundedBlockingQueue(3);   // initialize the queue with capacity = 3.

queue.enqueue(1);   // Producer thread P1 enqueues 1 to the queue.
queue.enqueue(0);   // Producer thread P2 enqueues 0 to the queue.
queue.enqueue(2);   // Producer thread P3 enqueues 2 to the queue.
queue.dequeue();    // Consumer thread C1 calls dequeue.
queue.dequeue();    // Consumer thread C2 calls dequeue.
queue.dequeue();    // Consumer thread C3 calls dequeue.
queue.enqueue(3);   // One of the producer threads enqueues 3 to the queue.
queue.size();       // 1 element remaining in the queue.

Since the number of threads for producer/consumer is greater than 1, we do not know how the threads will be scheduled in the operating system, even though the input seems to imply the ordering. Therefore, any of the output [1,0,2] or [1,2,0] or [0,1,2] or [0,2,1] or [2,0,1] or [2,1,0] will be accepted.
answer:

Use ReentrantLock lock. For each method, lock.lock() first, and finally lock.unlock().

Two Condition full and empty, while size == capacity, full.await(). Exist while, givs empty signal. Vice versa.

Time Complexity: O(1).

Space: O(n).




"""
the notify() and notifyAll() methods don’t release the lock; 
this means that the thread or threads awakened will not return from their wait() call immediately, 
but only when the thread that called notify() or notifyAll() finally relinquishes ownership of the lock.
不能put self.cv.notify outside with self.cv:  比如
        with self.cv:
            while self.count == self.capa:
                self.cv.wait()
            self.q.append(element)
            self.count += 1
        self.cv.notify()   不可以
因为 可能 thread 1 -> release lock;  thread 2-> acquire lock;   thread 1 -> notify thread 2 -> wait ,造成thread 2 miss the notify 
https://stackoverflow.com/questions/46076186/why-does-python-threading-condition-notify-require-a-lock
假如notify after releasel lock 有三个thread, 一个producer, 两个consuemer; cause a scheduling priority inversion; 在wait 的会后执行
The following sequence may occur:
P                         LC                       HC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              execute(item)（not wait)            (in wait())
lock()                                  
wq.push(item)
release()
                     acquire()
                     item = wq.pop()
                     release();
notify()
                                                     (wake-up)
                                                     while (wq.empty())
                                                       wait();
Whereas if the notify() happened before release(), LC wouldn't have been able to acquire() before HC had been woken-up. 
This is where the priority inversion occurred. This is the second argument.
In Python, you MUST HOLD the lock while notifying. The internal implementation does not allow the underlying OS to avoid priority inversion
, because it enforces a FIFO order on the waiters. 
The developers of the Python threading module might have specifically wanted a FIFO order for some reason, 
and found that this was somehow the best way of achieving it,
and wanted to establish that as a `Condition` at the expense of the other (probably more prevalent) approaches. 
"""


import threading

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.cv = threading.Condition()
        self.q = collections.deque()
        self.capa = capacity
        self.count = 0

    def enqueue(self, element: int) -> None:
        with self.cv:
            while self.count == self.capa:
                self.cv.wait()
            self.q.append(element)
            self.count += 1
            self.cv.notify()

    def dequeue(self) -> int:
        val = 0
        with self.cv:
            while self.count == 0:
                self.cv.wait()
            val = self.q.popleft()
            self.count -= 1
            self.cv.notify()
        return val
            
    def size(self) -> int:
        with self.cv:
            return len(self.q)




import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
      
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
      self.pushing.acquire()
      self.editing.acquire()
      
      self.queue.append(element)
      
      self.editing.release()
      self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        self.pushing.release()
        return res

    def size(self) -> int:
      return len(self.queue)

