import xadmin
from .models import TypeInfo,GoodsInfo


# Register your models here.
class TypeInfoAdmin(object):
    list_display = ['id','ttitle']

class GoodsInfoAdmin(object):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gkucun','gcontent','gtype']

xadmin.site.register(TypeInfo,TypeInfoAdmin)
xadmin.site.register(GoodsInfo,GoodsInfoAdmin)