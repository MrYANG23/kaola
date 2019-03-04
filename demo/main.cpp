#include <iostream>
#include <iostream>
#include <opencv2/opencv.hpp>
#include "../kl-person-rt-api.h"


int main(int argc, char **argv)
{
    IKLPersonDetect* yoloRT = IKLPersonDetect::createIKLPersonDetect("../models/serial/");;
    cv::Mat input = cv::imread("0.jpg");
    yoloRT->predictImg(input);
    std::vector<cv::Rect> rectangles = yoloRT->rectangles();
    for(auto &rect: rectangles)
    {
        cv::rectangle(input,rect,cv::Scalar(0, 238, 238),2);
    }
    cv::imshow("test",input);
    cv::waitKey(0);

    return 0;
}

//
//int main() {
//    std::cout << "Hello, World!" << std::endl;
//    return 0;
//}