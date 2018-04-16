from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.template import loader
from datetime import date

# Create your views here.


# http://127.0.0.1:8000/app01/index
from app01.models import Department


def index(request):
    """进入首页"""
    # 调用模型
    # 模板界面要显示的动态数据(字典)
    context = {
        'name': 'django',
        'sex': '男',
        'age': 25,
        'salary': 10000,
        'hobby': ['python', 'c/c++', 'java']
    }

    # # 方式一:
    # # 调用模板
    # # 加载模板,得到一个Template对象
    # # alt + enter: 导包
    # template = loader.get_template('index.html')
    # # 模板渲染, 生成标准的html界面内容
    # html_str = template.render(context, request)
    # # 响应请求,返回html界面给浏览器显示
    # return HttpResponse(html_str)

    # 方式二: ctrl + p: 查看参数
    return render(request, 'app01/index.html', context)


def show_deps(request):
    """显示所有的部门"""
    # 查询所有的部门信息
    # QuerySet对象
    departments = Department.objects.all()
    # 定义模板显示的数据
    context = {
        'departments': departments
    }
    # 调用模板,请求请求
    # HttpResponse
    return render(request, 'app01/show_deps.html', context)


def show_dep(request, dep_id):
    """
    显示部门下所有的员工
    :param request:
    :param dep_id: 部门id
    :return:
    """
    # 查询部门下所有的员工
    d = Department.objects.get(id=dep_id)
    employees = d.employee_set.all()

    context = {
        'department': d,
        'employees': employees
    }
    # 响应请求
    return render(request, 'app01/show_dep.html', context)

def add_dep(request):
    d = Department()
    d.name = '人事部'
    d.create_date = date(2018, 1, 1)
    d.save()

    return redirect('/show_deps')

def del_dep(request, dep_id):
    Department.objects.filter(id=dep_id).update(is_delete=True)

    return redirect('/show_deps')


def json(request):
    """进入JsonResponse案例演示界面"""
    response = render(request, 'json.html')
    response.set_cookie('xxx', 'xxx')
    return response




def getemployee(request):
    context = {
        'name' : '青蛙',
        'sex' : '男',
        'length': 1.8,
    }

    return JsonResponse(context)



