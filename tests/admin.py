from django.contrib import admin
from tests.models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'category', 'modified_date', 'created_date')
    search_fields = ('test_name', 'category__category_name')
    list_per_page = 20
    list_max_show_all = 100
    prepopulated_fields = {"slug": ("test_name",)}


admin.site.register(Test, TestAdmin)
