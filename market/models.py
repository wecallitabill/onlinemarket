from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.o

#按地址分类名称
class Location_Cate(models.Model):
	Location_name=models.CharField(max_length=20,verbose_name='地址目录名称')
	
	def __str__(self):
		return self.Location_name

	class Meta:
		verbose_name='地址分类名称'
		verbose_name_plural=verbose_name

#按产品种类分类名称
class Brands_Cate(models.Model):
	Brands_name=models.CharField(max_length=20,verbose_name='产品目录名称')
	
	def __str__(self):
		return self.Brands_name

	class Meta:
		verbose_name='产品分类名称'
		verbose_name_plural=verbose_name


#查找商品链接
def get_brand_path(instance,filename):
	return 'video/{0}/{1}'.format(instance.name,filename)

#查找商品图片链接
def get_img_path(instance,filename):
	return 'video_img/{0}/{1}'.format(instance.name,filename)

#产品名称
class Brand(models.Model):
	name=models.CharField(verbose_name='产品名称',max_length=20)
	link=models.FileField(verbose_name='产品链接',upload_to=get_brand_path)
	img=models.ImageField(verbose_name='产品图片',upload_to=get_img_path)
	introduce=models.TextField(verbose_name='产品介绍')
	price=models.IntegerField(verbose_name='产品价格')
	connect=models.TextField(verbose_name='联系方式')
	brand_cate=models.ForeignKey(Brands_Cate,verbose_name='产品目录分类')
	location_cate=models.ForeignKey(Location_Cate,verbose_name='产品地址分类')
#	brand_cate=models.ManyToManyField(Brands_Cate,verbose_name='产品目录分类')
#	location_cate=models.ManyToManyField(Location_Cate,verbose_name='产品地址分类')
	views=models.IntegerField(verbose_name='观看次数',default=0)
	create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
	create_date=models.DateField(verbose_name='创建日期',auto_now_add=True)
	status=models.CharField(verbose_name='状态',choices=(('上线','上线'),('下线','下线')),max_length=10,default='上线')
	
	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name='产品名称'
		verbose_name_plural=verbose_name

#产品详细信息
class Set(models.Model):
	name=models.CharField(verbose_name='产品详细信息',max_length=20)
	brand=models.ForeignKey(Brand,verbose_name='产品名称')
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name='产品详细信息'
		verbose_name_plural=verbose_name


#标签名称
class Label(models.Model):
	name=models.ForeignKey(Brand,verbose_name='产品')
	label=models.CharField(verbose_name='标签名',max_length=10)

	def __str__(self):
		return self.label

	class Meta:
		verbose_name='标签'
		verbose_name_plural=verbose_name

#点赞数
#class Likes(models.Model):
#	name = models.ForeignKey(Brand,verbose_name='产品')
#	user = models.ForeignKey(User,verbose_name='用户')
#	time = models.DateTimeField(verbose_name='时间',auto_now_add=True)
#
#	def __str__(self):
#		return str(self.name)
#	
#	class Meta:
#		verbose_name='点赞'
#		verbose_name_plural=verbose_name

class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True,unique=True)

    class Meta(AbstractUser.Meta):
        pass

#浏览历史
class History(models.Model):
	name = models.ForeignKey(Brand)
	user = models.ForeignKey(User)
	view_date = models.DateTimeField(verbose_name='浏览时间',auto_now_add=True)
	def __str__(self):
		return str(self.user)

	class Meta:
		verbose_name = '浏览历史'
		verbose_name_plural = verbose_name

#关于
class About(models.Model):
	text=models.TextField(verbose_name='关于')
	email=models.EmailField(max_length=20)
	qq=models.CharField(max_length=20,verbose_name='qq')
	def __str__(self):
		return self.qq
	
	class Meta:
		verbose_name='关于'
		verbose_name_plural=verbose_name






		
