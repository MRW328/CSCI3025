from Fish import Fish 
#name species age water type
    
myAquarium = []

myAquarium.append(Fish('Nemo', 'clown', 21, 'Salt'))
myAquarium.append(Fish("Gabriel", 'Angel', 17, 'Salt', True))
myAquarium.append(Fish('Sally', 'Salmon', 6, 'Fresh'))

print(myAquarium[0])
myAquarium[0].feed()
myAquarium[0].feed()
print(f"Fish fed: { myAquarium[0].isFed()}")

myAquarium[0].age = -5
print(myAquarium[0].age) 

print(myAquarium[1])
print(f"Fish fed: {myAquarium[1].isFed()}")

print(myAquarium[2])
myAquarium[0].feed()
print(f"Fish fed: { myAquarium[0].isFed()}")