from django.contrib import admin
from tests.forms import AnswerInlineFormSet
from tests.models import Test, Question, Answer, Results


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
    search_fields = ('question',)
    list_per_page = 20
    list_max_show_all = 100
    list_filter = ('test__test_name',)
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    """Display Answer model fields in admin panel"""
    list_display = ('answer', 'answer_image', 'question', 'is_correct')
    list_per_page = 20
    list_max_show_all = 100


class ResultsAdmin(admin.ModelAdmin):
    """Display Results model in admin panel"""
    list_display = ('user', 'category', 'test', 'correct_answer_count', 'wrong_answer_count',
                    'correct_answer_percent', 'created_at', 'updated_at')
    search_fields = ('user__email',)


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Results, ResultsAdmin)
