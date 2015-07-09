class Time:
      def time(self):
          print "%r:%r:%r"%(self.hour,self.minute,self.second)
      def add(self,t1,t2):
          sum = time()
          sum.hour = t1.hour+t2.hour
          sum.minute = t1.minute+t2.minute
          sum.second = t1.second + t2.second
          return sum

start = Time()
start.hour = 5
start.minute = 30
start.second = 40
start.time()

dura = Time()
dura.hour = 3
dura.minute = 35
dura.second = 0
dura.time()

s = Time()
s.add(start,dura)
s.time()
