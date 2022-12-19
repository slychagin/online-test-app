from django import forms
from tests.models import Answer


class AnswerInlineFormSet(forms.BaseInlineFormSet):
    """
    Validation for entered answers in admin panel.
    Raise exception if admin mark all answers like correct,
    or all like incorrect
    """
    class Meta:
        model = Answer
        fields = ('answer', 'is_correct')

    def clean(self):
        """
        Check entered answers in admin panel.
        If all answers is correct or all answers is incorrect raise error.
        """
        super(AnswerInlineFormSet, self).clean()
        data = [item['is_correct'] for item in self.cleaned_data]
        if all(data):
            raise forms.ValidationError('Хотя бы один ответ должен быть неверным!')
        if not any(data):
            raise forms.ValidationError('Хотя бы один ответ должен быть верным!')
