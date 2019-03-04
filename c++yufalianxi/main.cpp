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
//


//string
//#include <iostream>
//#include <string>
//using std::string;
//int main()
//{
//    string a1="niagnksdflk";
//    string a2("nihaoma");
//    string a3(10,'ni');
//    string a4=a1+a3;
//    std::cout<<a1<<std::endl;
//    std::cout<<a2<<std::endl;
//    std::cout<<a3<<std::endl;
//    std::cout<<"输出a4的值"<<a4<<std::endl;
//    if(a1.empty())
//    {
//        std::cout<<"a1为空"<<std::endl;
//    }
//    else
//    {
//        std::cout<<"a1不为空"<<std::endl;
//        std::cout<<"返回a1的长度"<<a1.size()<<std::endl;
//    }
//    return 0;
//}
//debug:
//niagnksdflk
//nihaoma
//iiiiiiiiii
//输出a4的值niagnksdflkiiiiiiiiii
//a1不为空
//返回a1的长度11

//读写string对象

//
//#include <iostream>
//#include <string>
//
//using namespace std;
//
//int main() {
//    string s;
//    cin >> s;
//    cout << s << endl;
//    return 0;
//
//}
//

//
//#include <iostream>
//#include <string>
//using namespace std;
//
//
//int main()
//{
//    string s1;
//    string s2;
//    cin>>s1>>s2;
//    cout<<s1<<s2<<endl;
//
//    return 0;
//
//
//}
//读取未知数量的string对象
//#include <iostream>
//#include <string>
//using namespace std;
//
//int main()
//{
//    string a;
//    while (cin>>a)
//    {
//        cout<<a<<endl;
//
//    }
//    return 0;
//}
////dubug:
////输入 ni hao madni
////输出 ni
////    hao
////    madni


//使用getline读取一整行
//#include <iostream>
//#include <string>
//using namespace std;
//
//int main()
//{
//    string s1;
//    while (getline(cin,s1))
//    {
//        cout<<s1<<endl;
//    }
//    return 0;
//
//}


//3.2.2 编程练习
//3.2
//#include <iostream>
//#include <string>
//using namespace std;
//int main()
//{
//    string a1;
////    while (getline(cin,a1))
////    {
////        cout<<a1<<endl;
////    }
//
//    while (cin>>a1)
//    {
//        cout<<"second"<<a1<<endl;
//    }
//
//    return 0;
//}
//
//


//习题3.4 判断输入的两个字符是否相等,以及长度是否相等。

//#include <iostream>
//#include <string>
//using namespace std;
//
//string s1;
//string s2;
//int main() {
//    cin >> s1 >> s2;
//    cout << s1 << endl;
//    cout << s2 << endl;
//    if (s1 == s2) {
//        cout << "两个字符相等" << endl;
//        cout << s1 << endl;
//
//    } else {
//        if (s1 < s2) {
//            cout << s2 << endl;
//        } else {
//            cout << s1 << endl;
//        }
//    }
//
//    if (s1.size() != s2.size()) {
//        if (s1.size() < s2.size()) {
//            cout << "输出较长的字符串" << endl;
//            cout << s2 << endl;
//
//        }
//    } else
//        {
//            cout<<"两个字符串长度相同"<<endl;
//        }
//}
//输入 ni ni
// ni
// ni
//两个字符相等
//ni
//两个字符串长度相同


//练习判断输入的字符串有几个小写字母
//#include <iostream>
//#include <string>
//using namespace std;
//
//string s1("hello girl");
//decltype(s1.size()) count=0;//将count的类型转为与s1.size()一样的 string::size_type类型 unsigned类型的
//int main()
//{
//    for (auto c :s1)
//    {
//        if (islower(c))
//        {
//            count++;
//        }
//        cout<<c<<endl;
//    }
//    cout<<"最终的小写字母个数"<<count<<endl;
//
//}


//改变字符串中的内容
//
//#include <iostream>
//#include <string>
//using namespace std;
//
//string a1("hello how are you");
//
//int main()
//{
//    for (auto &c: a1)
//    {
//        c=toupper(c);
//        cout<<c<<endl;
//    }
//    cout<<"改变后的字符串"<<endl;
//    cout<<a1<<endl;
//}


//用下标运算符号
//下标运算符号[]是string::size_type类型
//#include <iostream>
//#include <string>
//using namespace std;
//
//string b1="never give up";
//
//decltype(b1.size()) index=0;
//int main()
//{
//
//    while (b1.size()!=0&& index!=b1.size())
//    {
//        cout<<b1[index]<<endl;
//        index++;
//    }
//
//    return 0;
//}


//向vector对象中添加元素
//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//vector<int > a;
//int main()
//{
//
//    for (int i = 0; i < 10; ++i) {
//        a.push_back(i);
//    }
//
//    return 0;
//
//}


//用cin读入一组整数或者字符串串,并存放入一个vector对象中

//#include <iostream>
//#include <string>
//#include <vector>
//using namespace std;
//
//
//vector<int> a;
//vector<string> s;
//
//string s1;
//
//int i;
//int main()
//{
//
//    if (cin>>i,i==0)
//    {
//
//        for (s1;cin>>s1;s.push_back(s1));
//
//    }
//    else
//    {
//        for (int j ; cin>>j ; a.push_back(j));
//    }
//    return 0;
//
//}


//#include <iostream>
//#include <vector>
//#include <string>
//using namespace std;
//string word;
//vector<string> s1;
//int main()
//{
//    while (cin>>word)
//    {
//        s1.push_back(word);
//
//    }
//    return 0;
//}

//输入成绩，将输入的成绩归分段，并统计每个分段的个数
//#include <iostream>
//#include <vector>





//对容器的访问(使用范围for语句)
//#include <iostream>
//#include <vector>
//#include <string>
//using namespace std;
//vector<int> a{1,2,3,4,5,6,7,8,9};
//
//int main()
//{
//    for(auto &a1:a)
//    {
//        a1*=a1;
//    }
//    for (auto a2:a)
//    {
//        cout<<a2<<endl;
//    }
//
//    return 0;
//
//}
//debug:
//1
//4
//9
//16
//25
//36
//49
//64
//81

//创建一个含有10个整数的vector，使用迭代器，将所有元素的值变为原来的两倍。输出vector对象的内容，检验程序是否正确。
//#include <iostream>
//#include <vector>
//#include <string>
//using namespace std;
//
//
//int main()
//{
//    vector<int > a{1,2,3,4,5,6,7,8,9};
//    for (auto it=a.begin();it!=a.end();++it)
//    {
//        *it*=2;
//    }
//    for (auto i:a)
//    {
//        cout<<i<<"";
//
//    }
//    return 0;
//
//
//}
//debug:
//24681012141618


//指针数组练习
//#include <iostream>
//using namespace std;
//
//int a[]={1,2,3,4,5};
//int *p=a;
//int main()
//{
//    int b=*(a+3);
//    int c=*(p+3);
//    cout<<b<<endl;
//    cout<<c<<endl;
//
//    return 0;
//
//}



// 练习4.10 while 循环写一个条件，使其从标准输入中读取整数，遇到23时候，停止。
//方法一
//#include <iostream>
//using namespace std;
//
//
//int main()
//{
//    int a;
//    while (cin>>a)
//    {
//        if (a!=23)
//        {
//            continue;
//        } else
//        {
//            cout<<"输入为23号"<<endl;
//            break;
//        }
//    }
//    cout<<a<<endl;
//    return 0;
//}
//
//方法二
//#include <iostream>
//using namespace std;
//int main()
//{
//
//    int a;
//
//    while (cin>>a && a!=23)
//    {
//        continue;
//    }
//    return 0;
//
//}
//


//测试前置与后置递增或递减运算符
//前置先进行自加或者自减后，再付值
//后置先进行赋值后在自加或者自减。
//前置后置的优先级高于解引用。
//#include <iostream>
//using namespace std;
//
//int main()
//{
//    int i=0,j;
//    j=i++;
//    cout<<j<<endl;
//}
//dubug
//0

//练习4.21编写一段程序,使用条件运算符从vector<int>中找到哪些元素的值是奇数，然后将其翻倍。
//#include <iostream>
//#include <vector>
//using namespace std;
//
//vector<int> a{1,2,3,4,5,6,7,8,9};
//
//int main()
//{
//    for(auto &a1 :a)
//    {
//        a1=(a1/2)!=0? a1*2 : a1;
//    }
//    for(auto a2: a)
//    {
//        cout<<a2<<endl;
//    }
//
//    return 0;
//}


//size of 的用法
//编写一段程序，输出每一种内置类型所占用的空间大小。

//#include <iostream>
//using namespace std;
//
//int a;
//double b;
//char c;
//long d;
//long long e;
//float f;
//
//int main()
//{
//    cout<< sizeof(a)<<endl;
//    cout<< sizeof(b)<<endl;
//    cout<< sizeof(c)<<endl;
//    cout<< sizeof(d)<<endl;
//    cout<< sizeof(e)<<endl;
//    cout<< sizeof(f)<<endl;
//}
//dubug:
//4
//8
//1
//8
//8
//4


//练习6.4 编写一个与用户交互的函数，要求用胡输入一个数字，计算生成该数字的阶乘
//#include <iostream>
//
//using namespace std;
//
//
//int myfunc(int a)
//{
//    int sum=1;
//    while (a>1)
//    {
//        sum*=a;
//        --a;
//
//    }
//    return sum;
//}
//int main() {
//
//
//    int b;
//    int input;
//    cin>>input;
//    cout<<input<<endl;
//    b = myfunc(input);
//    cout<<b<<endl;
//    return 0;
//}
//dubug:
//6
//6
//720

//局部静态对象
//#include <iostream>
//using namespace std;
//
//int count_call()
//{
//    static int a=0;
//    return ++a;
//}
//int main()
//{
//    for (int i = 0; i <10 ; ++i)
//    {
//        cout<<"调用计数函数"<<count_call()<<endl;
//    }
//
//    return 0;
//}
//debug:
//调用计数函数1
//调用计数函数2
//调用计数函数3
//调用计数函数4
//调用计数函数5
//调用计数函数6
//调用计数函数7
//调用计数函数8
//调用计数函数9
//调用计数函数10


//练习6.6 说明形参，局部变量以及局部静态变量的区别。编写一个函数u，同时用到这三种形式。


//6.2.1
//编写一个函数，使用指针形参交换两个整数的值。在代码中调用该函数并输出交换后的结果，以此验证函数的正确性。

//#include <iostream>
//using namespace std;
//
//int jioahuan(int *p1,int *p2)
//{
//    int a=*p1;
//    int b=*p2;
//    *p1=b;
//    *p2=a;
//
//}
//
//int main()
//{
//    int a=23;
//    int b=24;
//    cout<<"交换前的a"<<a<<endl;
//    cout<<"交换前的b"<<b<<endl;
//
//    jioahuan(&a,&b);
//
//    cout<<"交换后的a"<<a<<endl;
//    cout<<"交换后的b"<<b<<endl;
//
//    return 0;
//
//}
//debug
//交换前的a23
//交换前的b24
//交换后的a24
//交换后的b23


//使用引用形参，返回额外信息
//输入一个字符串，判断某个字母在字符串中第一次出现的位置以及在字符串中总共出现的次数。
//
//#include <iostream>
//#include <string>
//using namespace std;
//
//
//string s1="nihaomagirlsniajajkdkjfhaniahadn";
//string::size_type find_char_count(const string &s, char c,string::size_type &counts)
//{
//    auto begin_numbers =s.size();
//    for (string::size_type i = 0; i <s.size() ; ++i) {
//
//        if (s[i]==c)
//        {
//
//            if (begin_numbers==s.size())
//            {
//                begin_numbers=i;
//
//            }
//
//            ++counts;
//        }
//
//    }
//    return begin_numbers;
//}
//
//int main()
//{
//    string::size_type first_id;
//    string::size_type counts_number=0;
//    string::size_type counts_number1=0;
//    first_id=find_char_count(s1,'h',counts_number);
//    cout<<"该字母第一次出现的位置"<<first_id<<endl;
//    cout<<"总共出现的次数"<<counts_number<<endl;
//    cout<<"使用常量引用的好处，传值的时候可以传递字面值"<<endl;
//    cout<<"传字面字符的时候第一次出现某个字母的位置"<<find_char_count("nihaoyanghan",'a',counts_number1)<<endl;
//    cout<<"传字面字符的时候某个字符出现的次数"<<counts_number1<<endl;
//
//}
//debug;
//该字母第一次出现的位置2
//总共出现的次数3
//使用常量引用的好处，传值的时候可以传递字面值
//传字面字符的时候第一次出现某个字母的位置3
//传字面字符的时候某个字符出现的次数3

//练习6.17 编写一个函数，判断string对象中是否含有大写字母。编写另一个函数，把string对象全部都改写成小写形式

//#include <iostream>
//#include <string>
//using namespace std;
//
////对于内容不需要改变的字符串，可以使用const
//bool is_bigalpha(const string &s)
//{
//    for (decltype(s.size()) i = 0; i <s.size() ; ++i)
//    {
//        if (isupper(s[i]))
//        {
//            return true;
//        }
//
//
//    }
//}
//
////对于内容需要改变的不使用const
//void change(string &s)
//{
//    for (decltype(s.size()) i = 0; i <s.size() ; ++i)
//
//    {
//        s[i]= tolower(s[i]);
//    }
//
//}
//
//int main()
//{
//
//    string s1="HELLOgirl";
//
//    cout<<"检查输入字符串有没有大写字母"<<endl;
//
//    cout<<is_bigalpha(s1)<<endl;
//    change(s1);
//    cout<<"将字符串中的大写字母改为小写字母"<<endl;
//    cout<<s1<<endl;
//
//}

//总结指向常量的引用不能通过操作改变指向对象的值，只可有对象本身自我改变，类似于指向常量的指针，但是需要区别常量指针




//练习6.21 编写一个函数，令其接受两个参数：一个int型的数，另一个是int指针。函数比较int的值和指针所指的值，返回较大的那个



//#include <iostream>
//using namespace std;
//int compare(int a, int *b)//写法1
//{
//    if (a<*b)
//    {
//
//        return *b;
//    } else
//    {
//        return a;
//
//    }
//
//}
//
//int jiandanc_compare(int a1,int *b1)
//{
//    return (a1>*b1)? a1:*b1;
//}
//
//
//int main()
//{
//    int a1=3;
//    int a2=6;
//
//    cout<<"输入比较后较大的值"<<endl;
//    cout<<compare(a1,&a2)<<endl;
//    cout<<"简单写法"<<endl;
//    cout<<jiandanc_compare(a1,&a2)<<endl;
//
//}

//debug:
//输入比较后较大的值
//6
//简单写法
//6


//练习6.27 编写一个函数，它的参数是initializer_list<int>类型的对象，函数的功能是计算列表中所有元素的和。

#include <iostream>
#include <initializer_list>//含有initializer_list形参的函数也可以同时拥有其他形参。
using namespace std;

int compute_all(initializer_list<int > l1)
{
    int sum=0;
    for (auto a:l1) {
        sum+=a;
    }

    return sum;

}


int main()
{
 cout<<"计算表1所有元素的和"<<compute_all({1,2,3,4,5,55})<<endl;
 cout<<"计算表2所有元素的和"<<compute_all({2,3,4,2,12,45,78,9})<<endl;

}



