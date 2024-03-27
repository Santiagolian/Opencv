import matplotlib.pyplot as plt
import math
import numpy as np


# plt.subplot(112)
compass = plt.subplot(121, polar=True)
# 确保包含rmax，设置合适的尺度
line , =compass.plot([0, 0], [0,200])       #plot(theta, r), arrowstyle='->'
x,y = line.get_xdata()[-1], line.get_ydata()[-1]
compass.annotate('', xy=(x, y), xytext=(x, y-1), arrowprops=dict(facecolor='blue', arrowstyle='->,head_width=.15', mutation_scale=20))



radius = 200
theta = math.pi/4
scale = math.cos(theta)
# compass.set_rmax(200)
# compass.set_rticks([40, 80, 120, 160, 200])
# compass.quiver(0,0,radius*math.cos(theta),radius*math.sin(theta),scale=scale, scale_units='xy')
# compass.quiver(0,0,radius*math.cos(math.pi),radius*math.sin(math.pi), scale=1000)

theta1 = np.array([0,0])
r = np.array([0,0])
dr = np.array([radius*math.cos(theta),radius*math.cos(math.pi)])
dtheta = np.array([radius*math.sin(theta),radius*math.sin(math.pi)])
quiv = compass.quiver(theta1,r,dr, dtheta,scale=400,color=['red', 'blue'],scale_units='width')
compass.set_aspect('equal')
# print('dpi', fig.get_dpi)
print(quiv.U)
print(dr)
arrows = plt.subplot(1,2,2)
arrows.arrow(0, 0, 50,100, width=0.4, head_width=1, head_length=5)
arrows.quiver(0,0,20,80,scale=1, scale_units='xy')

plt.figure(2)
plt.quiver(0,0,20,80,scale=1, scale_units='xy')
plt.plot([100,100],[100,100])    # 无此行无法绘制箭头
plt.axis([0,100,0,100])

fig2, arrow1 = plt.subplots()


# x = np.linspace(-4, 4, 6)
# y = np.linspace(-4, 4, 6)
# X, Y = np.meshgrid(x, y)
# U = X + Y
# V = Y - X


# arrow1.quiver(X, Y, U, V, color="C0", angles='xy',
#           scale_units='xy', scale=5, width=.015)

# arrow1.axis([-5,5,-5,5])
arrow1.quiver(0,0,20,80,scale=1, angles='xy', scale_units='xy')
plt.plot([100,100],[100,100])    # 无此行无法绘制箭头
arrow1.axis([0,100,0,100])


plt.show()

