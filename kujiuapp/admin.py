from django.contrib import admin
from .models import Post, Category, Tag

# 设置页面头部显示内容和页面标题
class MyAdminSite(admin.AdminSite):
    site_header = 'kujiu后台管理'
    site_title = 'kujiu'

# 设置页面头部显示内容和页面标题
admin.site = MyAdminSite(name='admin')

# 采用装饰器的方法来注册绑定，装饰器(Django1.7版本新增功能)自动注册，就不需要单独在下方注册了，避免新增模型时遗漏掉。
#@admin.register(Post, Category, Tag)
class PostAdmin(admin.ModelAdmin):
    # list_display设置要显示在列表中的字段(id字段是Django模型的默认主键)。
    list_display = ['id', 'title', 'created_time', 'modified_time', 'category', 'author']

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'author', 'title')

    # list_display设置每页显示多少条记录，默认是100条。
    list_per_page = 10

    # ordering设置默认排序字段，负号表示降序排列。
    ordering = ('-created_time', 'modified_time',)

    # list_editable设置默认可编辑字段
    list_editable = ['category']

    # fk_fields 设置显示外键字段
    fk_fields = ('category',)

    # 设置筛选器
    # list_filter设置过滤器
    list_filter = ('title', 'category', 'author')

    # search_fields设置搜索字段
    search_fields = ('title', 'category', 'author')


# 若想要将APP应用显示在后台管理中，需要再admin.py中注册，下面是注册绑定过程，若有新的模型，需要同步添加下方。
# 2019-8-31曾实验过装饰器的方法，但始终报错，所以最终仍然采用普通的注册方法。
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)


# Register your models here.
