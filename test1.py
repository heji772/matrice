import cv2
import numpy as np 
import time
from skimage.metrics import structural_similarity

cap = cv2.VideoCapture(0)


def nothing(x):
    pass

def srch():
    pass
    

#Controler setup
img = np.zeros((128,255), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('x','image',0,320*2-64,nothing)
cv2.createTrackbar('y','image',0,480-64,nothing)
cv2.createTrackbar('Thresh','image',0,255,nothing)
cv2.createTrackbar('Thresh2','image',0,255,nothing)
cv2.createTrackbar('ksize','image',0,15,nothing) 

def controler():
    
    x = cv2.getTrackbarPos('x','image')
    y = cv2.getTrackbarPos('y','image')
    Thr = cv2.getTrackbarPos('Thresh','image')
    Thr2 = cv2.getTrackbarPos('Thresh2','image')
    krnlsize = cv2.getTrackbarPos('ksize','image')
    
    return x,y,Thr,Thr2,krnlsize

def cagedraw(frame):
    
    
    [x,y,_,_,_]=controler()
    line_thickness=2
    size=128
    x1a, y1a= -640,0+y
    x2a, y2a= 640, 0+y
    
    x1b, y1b= -640,0+size+y
    x2b, y2b= 640, 0+size+y
    
    x1c, y1c= x-0,-480
    x2c, y2c= x+0, 480
    
    x1d, y1d= x+size, -480
    x2d, y2d= x+size, 480
    
    framecop=frame.copy()
    cv2.line(framecop, (x1a,y1a), (x2a,y2a), (255,255,255),thickness=line_thickness) 
    cv2.line(framecop, (x1b,y1b), (x2b,y2b), (255,255,255),thickness=line_thickness) 
    cv2.line(framecop, (x1c,y1c), (x2c,y2c), (255,255,255),thickness=line_thickness)
    cv2.line(framecop, (x1d,y1d), (x2d,y2d), (255,255,255),thickness=line_thickness)
    box=framecop[y:y+size,x:x+size]

    
    return framecop,box

def show(frame):
    
    
    #cv2.imshow("Frame",frame)
    [framecop,box]=cagedraw(frame)
    cv2.imshow("Frame+cage",framecop)
    #cv2.imshow("Box",box)
    if cv2.waitKey(1) == ord('w'):
        yesyes=1
        cage=box.copy()
        grayboxpic=cv2.cvtColor(cage, cv2.COLOR_BGR2GRAY)
        cv2.imshow("grayboxpic", grayboxpic)
        
        while yesyes:
            ret, frame = cap.read()
            [framecop,box]=cagedraw(frame)
            cv2.imshow("Frame+cage",framecop)
            if cv2.waitKey(1) == ord('t'):
                glavni()
            if cv2.waitKey(1) == ord('e'):
                [x,y,Thr,_,_]=controler()
                xx=x
                yy=y
                size=128
                highscore=1
                r=8
                step=4
                ro=r
                line_thickness=2
                xxc=0
                while highscore <= 75:
                    
                    ret, frame = cap.read() #original picture
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ##RGB to gray
                    newgray = gray.copy()
                    cv2.imshow('all',newgray)
                    if cv2.waitKey (1) == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        glavni()
                        break
                    for yyc in range(-r,r+ro,step):
                        
                        
                        newgraycage = gray.copy()
                        
                        x1a, y1a= -640,0+yy-yyc
                        x2a, y2a= 640, 0+yy-yyc
                        
                        x1b, y1b= -640,0+size-yyc+yy
                        x2b, y2b= 640, 0+size-yyc+yy
                        
                        x1c, y1c= xxc-0+xx,-480
                        x2c, y2c= xxc+0+xx, 480
                        
                        x1d, y1d= xxc+size+xx, -480
                        x2d, y2d= xxc+size+xx, 480
                        
                        newgray = gray.copy()
                        cv2.line(newgray, (x1a,y1a), (x2a,y2a), (255,255,255),thickness=line_thickness) 
                        cv2.line(newgray, (x1b,y1b), (x2b,y2b), (255,255,255),thickness=line_thickness) 
                        cv2.line(newgray, (x1c,y1c), (x2c,y2c), (255,255,255),thickness=line_thickness)
                        cv2.line(newgray, (x1d,y1d), (x2d,y2d), (255,255,255),thickness=line_thickness)
                        
                        ret, frame = cap.read() #original picture
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('all',newgray)
                        
                        if cv2.waitKey (1) == ord('q'):
                            cap.release()
                            cv2.destroyAllWindows()
                            glavni()
                            break
                        ret, frame = cap.read() #original picture
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        
                        for xxc in range(-r,r+ro,step):
                            
                            
                            newgraycage = gray.copy()
                            
                            x1a, y1a= -640,0+yy-yyc
                            x2a, y2a= 640, 0+yy-yyc
                            
                            x1b, y1b= -640,0+size-yyc+yy
                            x2b, y2b= 640, 0+size-yyc+yy
                            
                            x1c, y1c= xxc-0+xx,-480
                            x2c, y2c= xxc+0+xx, 480
                            
                            x1d, y1d= xxc+size+xx, -480
                            x2d, y2d= xxc+size+xx, 480
                            
                            newgray = gray.copy()
                            cv2.line(newgray, (x1a,y1a), (x2a,y2a), (255,255,255),thickness=line_thickness) 
                            cv2.line(newgray, (x1b,y1b), (x2b,y2b), (255,255,255),thickness=line_thickness) 
                            cv2.line(newgray, (x1c,y1c), (x2c,y2c), (255,255,255),thickness=line_thickness)
                            cv2.line(newgray, (x1d,y1d), (x2d,y2d), (255,255,255),thickness=line_thickness)
                            
                            #Filter box
                            graybox=newgray[yy-yyc:yy-yyc+size,xx+xxc:xx+xxc+size]
                            
                            ret,thresh1new = cv2.threshold(graybox,Thr,255,0)
                            cv2.imshow("Grayuncage",graybox)
                            cv2.imshow('all',newgray)
                            #cv2.imshow('Grayboxpic',grayboxpic)
                            
                            
                            (score, diff) = structural_similarity(graybox, grayboxpic, full=True)
                            if score*100 > 75:
                                print("Found a match")
                                highscore=score*100
                                yesyes=0
                                cv2.imshow("Grayuncagefinal",graybox)
                            print(score*100)
                            #diff = 255 - (diff * 255).astype("uint8")q
                            #print("Image Similarity: {:.4f}%".format(score * 100))
                            
                                
                                
                    
                    r=r+step
                yesyes=0
            
        
        

def glavni():
    while True:
        ret, frame = cap.read()
        show(frame)

        if cv2.waitKey (1) == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
        
                
        
        



glavni()

cap.release()
cv2.destroyAllWindows()