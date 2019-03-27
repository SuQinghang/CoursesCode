import matplotlib.pyplot as plt
import matplotlib.patches as patches
#裁剪算法
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

XL = 100
XR = 300
YB = 100
YT = 300
#line = [x1,x2,y1,y2]
line1 = [50,350,350,50]
line2 = [200,400,350,400]
line3 = [150,250,150,250]

#对线段的端点进行编码
def encode(x,y):
    c = 0
    if x<XL:
        c |= LEFT
    if x>XR:
        c |= RIGHT
    if y<YB:
        c |= BOTTOM
    if y>YT:
        c |= TOP
    return c
#Cohen-Sutherland算法
def CS_LineClip(line):
    x1 = line[0]
    x2 = line[1]
    y1 = line[2]
    y2 = line[3]
    code1 = encode(x1,y1)
    code2 = encode(x2,y2)
    while(code1 != 0 or code2 != 0):
        if(code1 & code2)!=0:
            return
        if(code1 != 0):
            code = code1
        else:
            code = code2
        if(LEFT&code)!=0:
            x = XL
            y = y1+(y2-y1)*(x-x1)/(x2-x1)
        elif(RIGHT&code)!=0:
            x = XR
            y = y1+(y2-y1)*(x-x1)/(x2-x1)
        elif(BOTTOM&code)!=0:
            y = YB
            x = x1+(x2-x1)*(y-y1)/(y2-y1)
        elif(TOP&code)!=0:
            y = YT
            x = x1 +(x2-x1)*(y-y1)/(y2-y1)
        if code == code1:
            x1 = x
            y1 = y
            code1 = encode(x1,y1)
        else:
            x2 = x
            y2 = y
            code2 = encode(x2,y2)
    return [x1,x2,y1,y2]



#中点分割裁剪算法  
def MidPointClip(line):
    x1 = line[0]
    x2 = line[1]
    y1 = line[2]
    y2 = line[3]
    xa,ya,xb,yb = x1,y1,x2,y2
    flag=0   #标志P1或者P2是否在区域内
    code1 = encode(x1,y1)
    code2 = encode(x2,y2)
    #两端点在外部同侧
    if (code1 & code2)!=0:
        return 
    #两端点同在内部
    if (code1==0 and code2 ==0):
        return [xa,xb,ya,yb]
    #P1在区域内部，不需要求P1的最近交点，此时flag=1
    if(code1==0):
        flag |= 1
    #P2在区域内部，此时flag=2
    if(code2==0):
        flag |=2
    #P1和P2都不在区域内部时flag=0，都在时flag=3
    #从P1出发找距离P1最近的交点
    while((abs(x1-x2)>1 or abs(y1-y2)>1) and (flag==0 or flag==2)):
        xmid = (x1+x2)/2
        ymid = (y1+y2)/2
        xa = xmid
        ya = ymid
        code = encode(xmid,ymid)
        #中点在区域内或与P2在外部同侧，用中点代替P2
        if(code == 0 or (code2 & code )!=0):
            x2,y2 = xmid,ymid
        #中点与P1外部同侧,用中点代替P1
        elif((code1 & code)!=0):
            x1,y1 = xmid,ymid
    #从P2出发找距离P2最近的交点
    x2 = line[1]
    y2 = line[3]
    while((abs(x1-x2)>1 or abs(y1-y2)>1)and (flag==0 or flag==1)):
        xmid = (x1+x2)/2
        ymid = (y1+y2)/2
        xb = xmid
        yb = ymid
        code = encode(xmid,ymid)
        #中点在区域内或与P1在外部同侧，用中点代替P1
        if(code == 0 or (code1 & code )!=0):
            x1,y1 = xmid,ymid
        #中点与P2外部同侧,用中点代替P2
        elif((code2 & code)!=0):
            x2,y2 = xmid,ymid
    return [xa,xb,ya,yb]

def ClipT(p,q,u1,u2):
    if(p<0):
        r=q/p
        if(r>u2):
            return u1,u2,False
        u1 = max(u1,q/p)
        return u1,u2,True
    elif(p>0):
        r = q/p
        if(r<u1):
            return u1,u2,False
        u2 = min(u2,q/p)
        return u1,u2,True
    else:
        return u1,u2,(q>=0)
    return u1,u2,True

#梁友栋-Barskey裁剪算法
def LB_LineClip(line):
    x1 = line[0]
    x2 = line[1]
    y1 = line[2]
    y2 = line[3]
    dx = x2-x1
    dy = y2-y1
    P = [0,-dx,dx,-dy,dy]
    Q = [0,x1-XL,XR-x1,y1-YB,YT-y1]
    u1 = 0
    u2 = 1
    u1,u2,flag = ClipT(P[1],Q[1],u1,u2)
    if(flag):
        u1,u2,flag = ClipT(P[2],Q[2],u1,u2)
        if(flag):
            u1,u2,flag = ClipT(P[3],Q[3],u1,u2)
            if(flag):
                u1,u2,flag = ClipT(P[4],Q[4],u1,u2)
                if(flag):
                    return [x1+u1*dx,x1+u2*dx,y1+u1*dy,y1+u2*dy]
            else:
                return 
        else:
            return 
    else:
        return 
     
#鼠标点击事件
def onclick(event):
    # #使用CS裁剪
    # if(CS_LineClip(line1)):
    #     clipedLine1 = CS_LineClip(line1)
    #     plt.plot([clipedLine1[0],clipedLine1[1]],[clipedLine1[2],clipedLine1[3]],color='black')
    # if(CS_LineClip(line2)):
    #     clipedLine2 = CS_LineClip(line2)
    #     plt.plot([clipedLine2[0],clipedLine2[1]],[clipedLine2[2],clipedLine2[3]],color='black')
    # if(CS_LineClip(line3)):
    #     clipedLine3 = CS_LineClip(line3)
    #     plt.plot([clipedLine3[0],clipedLine3[1]],[clipedLine3[2],clipedLine3[3]],color='black')
    # #使用中点分割裁剪
    # if(MidPointClip(line1)):
    #     clipedLine1 = MidPointClip(line1)
    #     plt.plot([clipedLine1[0],clipedLine1[1]],[clipedLine1[2],clipedLine1[3]],color='black')
    # if(MidPointClip(line2)):
    #     clipedLine2 = MidPointClip(line2)
    #     plt.plot([clipedLine2[0],clipedLine2[1]],[clipedLine2[2],clipedLine2[3]],color='black')
    # if(MidPointClip(line3)):
    #     clipedLine3 = MidPointClip(line3)
    #     plt.plot([clipedLine3[0],clipedLine3[1]],[clipedLine3[2],clipedLine3[3]],color='black')
    #L-Barskey
    if(LB_LineClip(line1)):
        clipedLine1 = LB_LineClip(line1)
        plt.plot([clipedLine1[0],clipedLine1[1]],[clipedLine1[2],clipedLine1[3]],color='black')
    if(LB_LineClip(line2)):
        clipedLine2 = LB_LineClip(line2)
        plt.plot([clipedLine2[0],clipedLine2[1]],[clipedLine2[2],clipedLine2[3]],color='black')
    if(LB_LineClip(line3)):
        clipedLine3 = LB_LineClip(line3)
        plt.plot([clipedLine3[0],clipedLine3[1]],[clipedLine3[2],clipedLine3[3]],color='black')
    fig.canvas.draw_idle()#重新绘制


if __name__ == "__main__":
    #绘制矩形
    fig = plt.figure()
    rect = patches.Rectangle((100,100),200,200)
    plt.gca().add_patch(rect)
    plt.plot([line1[0],line1[1]],[line1[2],line1[3]],color = 'r')
    plt.plot([line2[0],line2[1]],[line2[2],line2[3]],color = 'g')
    plt.plot([line3[0],line3[1]],[line3[2],line3[3]],color = 'y')

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
