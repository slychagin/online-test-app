from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from tests.models import Test, Question, Answer, Results


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

        request.session['correct_answers'] = 0
        request.session['wrong_answers'] = 0

    except Exception as e:
        raise e

    context = {
        'single_test': single_test,
        'first_question_id': question_list[0].pk,
        'test_question_amount': len(question_list)
    }
    return render(request, 'tests/test_description.html', context)


def question_details(request, category_slug, test_slug, question_id):
    """Render question_details.html file. Show questions with answers one by one on separate page"""
    if request.user.is_authenticated:
        try:
            single_test = Test.objects.get(category__slug=category_slug, slug=test_slug)
            question_list = Question.objects.filter(test__slug=test_slug)
            id_list = [question.pk for question in question_list]

            pk_idx = id_list.index(int(request.GET.get('id')))

            if pk_idx == len(question_list) - 1:
                last_question = True
                next_question_id = question_list[pk_idx].pk
            else:
                last_question = False
                next_question_id = question_list[pk_idx + 1].pk

            question = get_object_or_404(Question, pk=question_id)
            answers = Answer.objects.filter(question__pk=question_id)

            context = {
                'single_test': single_test,
                'question': question,
                'answers': answers,
                'next_question_id': next_question_id,
                'last_question': last_question,
                'current_question_number': pk_idx + 1,
                'test_question_amount': len(question_list),
                'category_slug': category_slug,
                'test_slug': test_slug
            }

            if request.method == 'POST':
                previous_question_id = request.META.get('HTTP_REFERER').split('=')[1]
                answers = Answer.objects.filter(question__pk=int(previous_question_id))

                id_list = request.POST.getlist('boxes')
                checked_answers = [Answer.objects.get(pk=int(answer_id)) for answer_id in id_list]
                correct = all([answer.is_correct for answer in checked_answers])
                unchecked_answers = [answer.is_correct for answer in answers if answer not in checked_answers]

                if correct and True not in unchecked_answers:
                    request.session['correct_answers'] += 1
                else:
                    request.session['wrong_answers'] += 1

                if 'last' in request.POST:
                    return redirect('results', category_slug=category_slug, test_slug=test_slug)
                else:
                    return render(request, 'tests/question_details.html', context)
            else:
                return render(request, 'tests/question_details.html', context)

        except Exception as e:
            raise e
    else:
        return redirect('login')


def results(request, category_slug=None, test_slug=None):
    """Show test results on separate page. Save results to database."""
    question_list = Question.objects.filter(test__slug=test_slug)
    test_question_amount = len(Question.objects.filter(test__slug=test_slug))

    data = Results()
    data.user = request.user
    data.category = Category.objects.get(slug=category_slug)
    data.test = Test.objects.get(slug=test_slug)
    data.correct_answer_count = request.session.get("correct_answers")
    data.wrong_answer_count = request.session.get("wrong_answers")
    data.correct_answer_percent = f'{round(request.session.get("correct_answers") * 100 / test_question_amount)}%'
    data.save()

    context = {
        'category_slug': category_slug,
        'test_slug': test_slug,
        'test_question_amount': test_question_amount,
        'data': data,
        'question_list': question_list,
    }
    return render(request, 'tests/results.html', context)
