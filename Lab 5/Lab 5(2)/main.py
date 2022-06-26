from Document import *

romulo = User("Romulo", True)
rafael = User("Rafael",False)
bruno = User("Bruno",False)

test = Document("TESTANDO 123", rafael)
test.showState()
test.publish(rafael)
test.showState()
test.review(romulo, False)
test.showState()
test.publish(rafael)
test.showState()
test.review(romulo, True)
test.showState()
test.expire(romulo)
test.showState()
test.publish(romulo)
test.showState()
print("\nRafael:\n")
test.render(rafael)
print("\nRomulo:\n")
test.render(romulo)
print("\nBruno:\n")
test.render(bruno)



