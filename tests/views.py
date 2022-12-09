from django.shortcuts import render, get_object_or_404
from category.models import Category
from tests.models import Test


def tests(request, category_slug=None):
    """Render tests.html file"""
    categories = None
    all_tests = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        all_tests = Test.objects.filter(category=categories)
        test_count = all_tests.count()
    else:
        all_tests = Test.objects.all()
        test_count = all_tests.count()

    context = {
        'all_tests': all_tests,
        'test_count': test_count
    }
    return render(request, 'tests/tests.html', context)


def test_description(request, category_slug, test_slug):
    try:
        single_test = Test.objects.get(category__slug=category_slug, slug=test_slug)
    except Exception as e:
        raise e

    context = {
        'single_test': single_test
    }
    return render(request, 'tests/test_description.html', context)
