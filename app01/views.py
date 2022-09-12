from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app01.models import UserInfo


# from app01.models import Department

# 必带参数request
def index(request):
    return HttpResponse("欢迎使用！")


def user_list(request):
    return render(request, "user_list.html")


def tpl(request):
    var = "韩超"
    lst = [28, "单身", "管理员"]
    dit = {"name": "韩超", "salary": 12000}
    # 获取变量引入html页面
    return render(request, "tpl.html", {"x1": var, "x2": lst, "x3": dit})


def news(request):
    # 1.定义一些新闻内容（列表或者字典）：数据库调取、网络请求、数据库等
    # 2.向某个地址发送请求
    # 3.使用第三方模块 requests
    # import requests

    # 要抓取的目标页码地址
    # url = 'https://www.chinaunicom.com.cn/news/list202202.html'
    # 抓取页码内容，返回响应对象
    # data_lst = requests.get(url).json()
    # 假设爬取的json格式数据
    data_lst = [{"a": "床前明月光，", "b": "疑似地上霜。"},
                {"c": "举头望明月，", "d": "低头思故乡。"}]
    return render(request, "news.html", {"data_lst": data_lst})


def something(request):
    # request是一个对象，封装了用户发送过来所有请求相关数据
    # 1.请求 请求方式获取显示：GET或者POST  输出结果显示：GET
    print(request.method)
    # 2.请求 请求获取 在URL上的传递值 /somthing/?n1=123&n2=999  输出结果显示 <QueryDict: {'n1': ['123'], 'n2': ['999']}>
    print(request.GET)
    # 3.请求 在请求体中提交数据
    print(request.POST)
    # 4.响应 HttpResponse字符串内容返回给请求者
    # return HttpResponse("字符串内容反馈响应。")
    # 5.响应 读取HTML内容 + 渲染（替换） -> 字符串 返回用户浏览器显示
    # return render(request, "something.html", {"title": "标题测试"})
    # 6.响应 重定向页面
    return redirect("https://www.baidu.com")


from app01.utils.usedform import Login


def login(request):
    # 进入界面默认GET请求
    # 当数据提交，则获取到POST请求，对接数据判断
    # username = request.POST.get("user")
    # password = request.POST.get("pwd")
    form = Login(data=request.POST)
    if form.is_valid():
        if form.cleaned_data.get("user") == "chc" and form.cleaned_data.get("pwd") == "cc123":
            return HttpResponse("登陆成功！")
    form = Login()
    return render(request, "login_captcha.html", {"form": form})


def orm(request):
    # 测试ORM方式 注意使用时每次进入页面就会执行一次
    # 1 增加数据
    # UserInfo.objects.create(name="岑鸿昌", password="cc158854", age="27")
    # UserInfo.objects.create(name="吴佩琦", password="12345678")
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="网络部")
    # Department.objects.create(title="IT部")
    #
    # # 2 删除数据
    # # 2.1 以id删除;  filter表示筛选
    # UserInfo.objects.filter(id=1).delete()
    # Department.objects.filter(id=6).delete()
    # # 2.2 删除表全部数据
    # UserInfo.objects.all().delete()
    # Department.objects.all().delete()

    # 3 获取数据
    # 3.1 获取全部数据
    # data_list = UserInfo.objects.all()  # 获取QuerySet类型数据[行1, 行2, 行3]，可以按照列表处理。
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)
    #
    # # 3.2 以id获取数据
    # data_list = UserInfo.objects.filter(id=1)  # 获取QuerySet类型数据[行1,]，仍然是列表。
    # row_obj = data_list.first()  # 取出列表中存储的第一个对象的方法
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)

    # 4 更新数据
    # 4.1 全部更新
    # UserInfo.objects.all().update(password="12345")
    # # 4.2 部分更新
    # UserInfo.objects.filter(id=2).update(name="小莫莫")
    # UserInfo.objects.filter(name="吴佩琦").update(age="30")

    return HttpResponse("数据操作成功！")


def info_list(request):
    data_list = UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    # 获取post请求传入的数据
    name = request.POST.get("user")
    password = request.POST.get("password")
    age = request.POST.get("age")
    # 添加到数据库
    UserInfo.objects.create(name=name, password=password, age=age)
    return HttpResponse("添加用户成功！")


def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list")  # 重定向至本页
