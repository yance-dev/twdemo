from twisted.internet.defer import Deferred


def got_poem(res):
    print('Your poem is served:')
    print(res)


def poem_failed(err):
    print('No poetry for you.')


d = Deferred()

# add a callback/errback pair to the chain
d.addCallbacks(got_poem, poem_failed)

# fire the chain with a normal result
d.callback('This poem is short.')

print("Finished")

"""
Your poem is served:
This poem is short.
Finished
"""
