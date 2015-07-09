class emp:
      def detail(self):
          print "(%r,%r,%r,%r)" %(self.name,self.age,self.pos,self.sala)
class join:
      def joi(self):
          c = emp()
          c.name = self.mid.x + self.mid.y
          return c
a = emp()
a.name = "nibin"
a.age = 18
a.pos = "student"
a.sala = "nill"
a.detail()

b = emp()
b.name = "sree"
b.age = 18
b.pos = "manager"
b.sala = 10000
b.detail()

d = join()
d.mid.x = "nibin"
d.mid.y = "sha"
d.joi()
