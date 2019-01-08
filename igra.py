class Tor:

	def __init__(self,name):
		self.health=100
		self.streight=20
		self.name=name
	def hit(self,target):
		target.health=target.health-self.streight
		print(self.name, "hit the", target.name)
	def heal(self,value):
		self.health=self.health+value
	def isAlive(self):
		return self.health>0
a=Tor("Navalny")
b=Tor("putin")
def duel(a,b):
	Att=a
	Def=b
	while(True):
		Att.hit(Def)
		if not Def.isAlive():
			break
		t=Att
		Att=Def
		Def=t
duel(a, b)
input()