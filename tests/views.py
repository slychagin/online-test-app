from django.shortcuts import render, get_object_or_404
from category.models import Category
from tests.models import Test, Question


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
    """Render test_description.html file"""
    try:
        single_test = Test.objects.get(category__slug=category_slug, slug=test_slug)
        question_list = Question.objects.filter(test__slug=test_slug)
    except Exception as e:
        raise e

    context = {
        'single_test': single_test,
        'first_question_id': question_list[0].pk

    }
    return render(request, 'tests/test_description.html', context)


def question_details(request, category_slug, test_slug, question_id):
    """Render question_details.html file"""
    try:
        single_test = Test.objects.get(category__slug=category_slug, slug=test_slug)
        question_list = Question.objects.filter(test__slug=test_slug)
        id_list = [question.pk for question in question_list]

        pk_idx = id_list.index(int(request.GET.get('id')))

        if pk_idx == len(question_list) - 1:
            next_question_id = question_list[pk_idx].pk
        else:
            next_question_id = question_list[pk_idx + 1].pk

        question = get_object_or_404(Question, pk=question_id)

        context = {
            'single_test': single_test,
            'question': question,
            'next_question_id': next_question_id
        }
        return render(request, 'tests/question_details.html', context)
    except Exception as e:
        raise e


