class Emp:
      count = 0
      def __init__(self,name,salary):
          self.name = name
          self.salary = salary
          Emp.count += 1
      def disp(self):
          print "total emp %r" % Emp.count
      def dispemp(self):
          print " Name:", self.name, "salry" , self.salary

x =  Emp("nibin",1000)
y = Emp("sagar",100)
x.dispemp()
y.dispemp()
print "Total emp %r"% Emp.count
print "Emp.__doc__", Emp.__doc__
print "Emp.__name__", Emp.__name__
print "Emp.__module__",Emp.__module__
