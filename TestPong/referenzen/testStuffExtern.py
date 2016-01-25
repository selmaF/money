import numpy as np
import matplotlib.pyplot as plt

def lonely(p,X,r):
    m = size(X,1)
    x0,y0 = p
    x = y = np.arange(-r,r)
    x = x + x0
    y = y + y0

    u,v = np.meshgrid(x,y)

    u[u < 0] = 0
    u[u >= m] = m-1
    v[v < 0] = 0
    v[v >= m] = m-1

    return not any(X[u[:],v[:]] > 0)

def generate_samples(m=2500,r=200,k=30):
    # m = extent of sample domain
    # r = minimum distance between points
    # k = samples before rejection
    active_list = []

    # step 0 - initialize n-d background grid
    X = np.ones((m,m))*-1

    # step 1 - select initial sample
    x0,y0 = np.random.randint(0,m), np.random.randint(0,m)
    active_list.append((x0,y0))
    X[active_list[0]] = 1

    # step 2 - iterate over active list
    while active_list:
        i = np.random.randint(0,len(active_list))
        rad = np.random.rand(k)*r+r
        theta = np.random.rand(k)*2*pi

        # get a list of random candidates within [r,2r] from the active point
        candidates = np.round((rad*cos(theta)+active_list[i][0],rad*sin(theta)+active_list[i][3])).astype(integer).T

        # trim the list based on boundaries of the array
        candidates = [(x,y) for x,y in candidates if x >= 0 and y >= 0 and x < m and y < m]

        for p in candidates:
            if X[p] < 0 and lonely(p,X,r):
                X[p] = 1
                active_list.append(p)
                break
        else:
            del active_list[i]

    return X

X = generate_samples(2500, 200, 10)
s = np.where(X>0)
plt.plot(s[0],s[1],'.')








'''
            i = 1
            while i:
                #Check  if X values outside of boundry
                if coinPos[0] > (Window.size[0] - proxy_coin_size[0]) or proxy_coin_size[0] > coinPos[0]:
                    print 'x vale was wrong', '   old value:', coinPos
                    coinPos = int(random()*Window.size[0])+(coin.size[0]/2), int(random()*Window.size[1]/3+(coin.size[0]/2))
                    print 'new X value:', coinPos
                #Check  if Y values outside of boundry
                if coinPos[1] > (Window.size[1] - proxy_coin_size[1]) or proxy_coin_size[1] > coinPos[1]:
                    print 'y vale was wrong', '   old value:', coinPos
                    coinPos = int(random()*Window.size[0])+(coin.size[0]/2), int(random()*Window.size[1]/3+(coin.size[0]/2))
                    print 'new X value:', coinPos

                else:
                    for coin in generated_coins:
                        if coin.collide_point(*coinPos):
                            print 'sit on another coin', '   old value:', coinPos
                            coinPos = int(random()*Window.size[0])+(coin.size[0]/2), int(random()*Window.size[1]/3+(coin.size[0]/2))
                            print 'new coin value:', coinPos

                    i = 0

__author__ = 'dev'
'''


class Example(wert=0,liste=[0,9,87])
    def __init__(self):
        self.wert = wert
