
def hello():
    print('Hello from the reactor loop!')
    print('Lately I feel like I\'m stuck in a rut.')


from twisted.internet import reactor

reactor.callWhenRunning(hello)

print('Starting the reactor.')
reactor.run()
"""
输出如下：
Starting the reactor.
Hello from the reactor loop!
Lately I feel like I'm stuck in a rut.
"""
