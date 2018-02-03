'''
使用matplotlib制作sin和cos的曲线图，并在x=1处做标示
'''

import numpy as np
from matplotlib import pyplot as  plt
def main():
    # line
    # 画一个sin和cos的曲线图
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True )
    c,s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color='blue', linewidth=1.0,linestyle='-', label='COS', alpha=0.5)
    plt.plot(x, s, color='red', linestyle=':', label='SIN')
    plt.title('COS & SIN')
    # 将坐标轴移到原点，隐藏掉right和top两条线
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    # 修改坐标轴上的label， 调整成适合使用的样式
    plt.xticks(
        [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$' ]
    )
    plt.yticks(np.linspace(-1,1,5, endpoint=True))
    for lable in ax.get_xticklabels() + ax.get_yticklabels():
        lable.set_fontsize(12)
        lable.set_bbox(dict(facecolor= 'white', edgecolor='none', alpha=0.2))
    plt.legend(loc= 'upper left')
    plt.grid()
    # plt.axis([-1,1,-0.5,1])
    # 在x=1处做条黄色虚线
    t=1
    plt.plot([t,t],[0,np.cos(t)], color='y', linewidth=2, linestyle='--')
    #对x=1做标注
    plt.annotate('COS(1)',xy= (t,np.cos(1)), xycoords= 'data', xytext= (+10, +30), textcoords='offset points',
                 arrowprops= dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))
    plt.show()
if __name__ == '__main__':
    main()


