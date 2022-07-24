import numpy as np
from pylab import *
x=np.arange(-5,5,0.1)

p1=figure(1)
plot(x,np.sin(x))
xlabel('x - axis')
ylabel('y - axis')
title('Sin Saperate')
savefig("p1.png")

p2=figure(2)
plot(x,np.cos(x))
xlabel('x - axis')
ylabel('y - axis')
title('Cos Saperate')
savefig("p2.png")

p3=figure(3)
plot(x,x*x+2*x+1)
xlabel('x - axis')
ylabel('y - axis')
title('Y Saperate')
savefig("p3.png")

p4=figure(4)
plot(x,np.sin(x))
plot(x,np.cos(x))
plot(x,x*x+2*x+1)
xlabel('x - axis')
ylabel('y - axis')
title('Same Graph')
legend(["Sin", "Cos","x²+2x+1"])
savefig("p4.png")