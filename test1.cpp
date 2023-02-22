#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
VideoCapture cap(0);
if (!cap.isOpened())
{
cout << "Error opening video stream or file" << endl;
return -1;
}
namedWindow("image", WINDOW_NORMAL);
createTrackbar("x", "image", 0, 320 * 2 - 64, NULL);
createTrackbar("y", "image", 0, 480 - 64, NULL);
createTrackbar("Thresh", "image", 0, 255, NULL);
createTrackbar("Thresh2", "image", 0, 255, NULL);
createTrackbar("ksize", "image", 0, 15, NULL);

while (1)
{
    Mat frame;
    cap.read(frame);

    int x = getTrackbarPos("x", "image");
    int y = getTrackbarPos("y", "image");
    int Thr = getTrackbarPos("Thresh", "image");
    int Thr2 = getTrackbarPos("Thresh2", "image");
    int krnlsize = getTrackbarPos("ksize", "image");

    line_thickness = 2;
    size = 128;
    int x1a, y1a = -640, 0 + y;
    int x2a, y2a = 640, 0 + y;

    int x1b, y1b = -640, 0 + size + y;
    int x2b, y2b = 640, 0 + size + y;

    int x1c, y1c = x - 0, -480;
    int x2c, y2c = x + 0, 480;

    int x1d, y1d = x + size, -480;
    int x2d, y2d = x + size, 480;

    Mat framecop = frame.clone();
    line(framecop, Point(x1a, y1a), Point(x2a, y2a), Scalar(255, 255, 255), line_thickness);
    line(framecop, Point(x1b, y1b), Point(x2b, y2b), Scalar(255, 255, 255), line_thickness);
    line(framecop, Point(x1c, y1c), Point(x2c, y2c), Scalar(255, 255, 255), line_thickness);
    line(framecop, Point(x1d, y1d), Point(x2d, y2d), Scalar(255, 255, 255), line_thickness);
    Mat box = framecop(Rect(x, y, size, size));

    imshow("image", framecop);
    imshow("box", box);

    char c = (char)waitKey(25);
    if (c == 27)
        break;
}

cap.release();
destroyAllWindows();

return 0;
}
void show(Mat frame) {
Mat framecop, box;
vector<Mat> res = cagedraw(frame);
framecop = res[0];
box = res[1];

imshow("Frame+cage", framecop);

if (waitKey(1) == 'w') {
    int yesyes = 1;
    Mat cage = box.clone();
    Mat grayboxpic;
    cvtColor(cage, grayboxpic, COLOR_BGR2GRAY);
    imshow("grayboxpic", grayboxpic);
    
    while (yesyes) {
        Mat frame;
        cap >> frame;
        
        vector<Mat> res = cagedraw(frame);
        framecop = res[0];
        box = res[1];
        
        imshow("Frame+cage", framecop);
        
        if (waitKey(1) == 't') {
            glavni();
        }
        if (waitKey(1) == 'e') {
            vector<int> control = controler();
            int x = control[0], y = control[1], Thr = control[2];
            int xx = x, yy = y;
            int size = 128;
            int highscore = 1;
            int r = 8, step = 4, ro = r, line_thickness = 2, xxc = 0;
            while (highscore <= 75) {
                Mat frame;
                cap >> frame;
                Mat gray;
                cvtColor(frame, gray, COLOR_BGR2GRAY);
                Mat newgray = gray.clone();
                imshow("all", newgray);
                if (waitKey(1) == 'q') {
                    cap.release();
                    destroyAllWindows();
                    glavni();
                    break;
                }
                for (int yyc = -r; yyc <= r + ro; yyc += step) {
                    Mat newgraycage = gray.clone();
                    int x1a = -640, y1a = 0 + yy - yyc;
                    int x2a = 640, y2a = 0 + yy - yyc;
                    int x1b = -640, y1b = 0 + size - yyc + yy;
                    int x2b = 640, y2b = 0 + size - yyc + yy;
                    int x1c = xxc - 0 + xx, y1c = -480;
                    int x2c = xxc + 0 + xx, y2c = 480;
                    int x1d = xxc + size + xx, y1d = -480;
                    int x2d = xxc + size + xx, y2d = 480;
                    newgray = gray.clone();
                    line(newgray, Point(x1a, y1a), Point(x2a, y2a), Scalar(255, 255, 255), line_thickness);
                    line(newgray, Point(x1b, y1b), Point(x2b, y2b), Scalar(255, 255, 255), line_thickness);
                    line(newgray, Point(x1c, y1c), Point(x2c, y2c), Scalar(255, 255, 255), line_thickness);
                    line(newgray, Point(x1d, y1d), Point(x2d, y2d), Scalar(255, 255, 255), line_thickness);
                    Mat frame;
                    cap >> frame;
                    cvtColor(frame, gray, COLOR_BGR2GRAY);
                    imshow("all", newgray);
                    void glavni() {
while (true) {
Mat frame;
cap.read(frame);
show(frame);
    if (waitKey(1) == 'q') {
        cap.release();
        destroyAllWindows();
        break;
    }
}
}

glavni();

cap.release();
destroyAllWindows();





                   
