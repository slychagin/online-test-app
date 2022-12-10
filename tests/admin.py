from django.contrib import admin
from tests.models import Test, Question


class QuestionInline(admin.TabularInline):
    """Display question fields inline Test model"""
    model = Question
    extra = 1


class TestAdmin(admin.ModelAdmin):
    """Display Test model fields in admin panel"""
    list_display = ('test_name', 'category', 'modified_date', 'created_date')
    search_fields = ('test_name', 'category__category_name')
    list_per_page = 20
    list_max_show_all = 100
    prepopulated_fields = {"slug": ("test_name",)}
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    """Display Question model fields in admin panel"""
    list_display = ('question', 'test')
    list_per_page = 20
    list_max_show_all = 100


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
