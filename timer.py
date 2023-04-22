'''timer'''

import time

class Timer:
    '''timer'''

    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        '''start'''
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()
    
    def stop(self):
        '''stop'''
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None
    
    def reset(self):
        '''reset rename rename'''
        self.elapsed = 0.0
    
    @property
    def running(self):
        return self._start is not None
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, *args):
        self.stop()

def countdown(n):
    while n > 0:
        n -= 1

t = Timer()
t.start()

#countdown(1000000) # 0.036127799889072776
#countdown(10000000) # 0.3711192000191659
#countdown(100000000) # 3.8038582999724895
countdown(1000000000) # 38.76235580001958
t.stop()
print(t.elapsed)
