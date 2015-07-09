class Emp:
      def emp1(self,name,age,salary):
          self.n = name
          self.a = age
          self.s = salary
          print "name:%r"%self.n + "Age:%r"  %self.a + "salary:%r"%self.s
      def allowance(self):
          self.all = 1000
class Details:
      def sala(self):
          d = Emp()
          d.emp1("name",20,100001)
          d.allowance()
          if d.s > 10000:
             print d.s + d.all
          else: 
             print "have not allowance"

x = Emp()
x.emp1("x",1,2)
x.allowance()

y = Details()
y.sala()
