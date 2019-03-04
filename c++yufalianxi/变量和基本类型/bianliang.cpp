//
// Created by yh on 19-2-26.
//

//#include <iostream>
//
//int main() {
//    std::cout << "Hello, World!" << std::endl;
//    return 0;
//}

//#include <iostream>
//int main()
//{
//    for (int i =10;i>=0;i--)
//    {
//        std::cout<<i<<std::endl;
//    }
//
//
//}


//#include <iostream>
//
//int main()
//{
//    for (unsigned i=12;i>=0;--i)
//    {
//        std::cout<<i<<std::endl;
//    }
//
//    return 0;
//}


//#include <iostream>
//int main()
//{
//    unsigned u=12;
//    while (u>0)
//    {
//        --u;
//        std::cout<<u<<std::endl;
//
//    }
//    return 0;
//
//}


//无符号在遇到小于0的值时，会变为无符号数
//#include <iostream>
//int main()
//{
//    for (int i=12;i>=0;--i)
//    {
//        std::cout<<i<<std::endl;
//    }
//    return 0;
//}
//


//切勿混用带符号类型和无符号类型
//#include <iostream>
//
//int main()
//{
//    unsigned u1=10 ,u2=45;
//
//    std::cout<<u2-u1<<std::endl;
//    std::cout<<u1-u2<<std::endl;
//    int i1=5,i2=11;
//    std::cout<<i2-i1<<std::endl;
//    std::cout<<i1-i2<<std::endl;
//    std::cout<<u2-i1<<std::endl;
//    std::cout<<u1-i2<<std::endl;
//    return 0;
//}
//debug:
//35
//4294967261
//6
//-6
//40
//4294967295

//变量作用域
//#include <iostream>
//
//int main()
//{
//    int sum=0;
//    for (int i=0;i<=10;i++)
//    {
//        sum+=i;
//        std::cout<<sum<<std::endl;
//    }
//    return 0;
//
//}

//嵌套的作用域
//#include <iostream>
//
//int a=28;
//int main()
//{
//    int b=4;
//    std::cout<<a<<b<<std::endl;
//    int a=16;
//    std::cout<<a<<b<<std::endl;
//    std::cout<<::a<<""<<b<<std::endl;
//
//    return 0;
//}



//
//#include <iostream>
//int i=42,sum=0;
//int main()
//{
//    for (i=0;i!=10;i++)
//    {
//        sum+=i;
//        std::cout<<i<<'\n'<<'-'<<sum<<std::endl;
//    }
//
//    std::cout<<"-----------------------"<<std::endl;
//    std::cout<<i<<sum<<std::endl;
//}

//变量作用域的复合类型
//指针和引用
//引用中的左值引用与右值引用

//空指针的定义
//int *p=0,*t=NULL,*H= nullptr;


//改变指针的值和指针所指对象的值
//#include <iostream>
//
//int a=1,b=2;
//int *p1=&a,*p2=&b;
//
//int main()
//{
//
//    std::cout<<"改变之前的值"<<p1<<'\n'<<*p2<<std::endl;
//    p1=&b;
//    *p2=1;
//
//    std::cout<<p1<<'\n'<<*p2<<std::endl;
//    return 0;
//}
//debug:
//
//改变之前的值0x601078
//2
//0x60107c
//1



////指向指针的引用
//#include <iostream>
//int a=1,*p1=&a;
//int main()
//{
//    int *&p2=p1;
//}
//
//

////对常量的引用
//#include <iostream>
//const int a=1;
//const int &b=a;

