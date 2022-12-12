from django.contrib import admin
from tests.form import AnswerInlineFormSet
from tests.models import Test, Question, Answer


class AnswerInline(admin.TabularInline):
    """Display answer fields inline Question model"""
    formset = AnswerInlineFormSet
    model = Answer
    extra = 0


class QuestionInline(admin.TabularInline):
    """Display question fields inline Test model"""
    model = Question
    extra = 0
    show_change_link = True


class TestAdmin(admin.ModelAdmin):
    """Display Test model fields in admin panel"""
    list_display = ('test_name', 'category', 'modified_date', 'created_date')
    search_fields = ('test_name', 'category__category_name')
    list_per_page = 20
    list_max_show_all = 100
    list_filter = ('category__category_name',)
    prepopulated_fields = {"slug": ("test_name",)}
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    """Display Question model fields in admin panel"""
    list_display = ('question', 'test')
    list_per_page = 20
    list_max_show_all = 100
    list_filter = ('test__test_name',)
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    """Display Answer model fields in admin panel"""
    list_display = ('answer', 'question', 'is_true')
    list_per_page = 20
    list_max_show_all = 100


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
