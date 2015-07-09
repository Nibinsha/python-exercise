class Time:
      def time(x):
         
          print "%r:%r:%r" %(x.hour,x.min,x.sec)  

t = Time()
t.hour = 11
t.min = 59
t.sec = 30
t.time()
