from django import forms
from django.forms import inlineformset_factory

from training.models import Course, LessonText

class LessonTextForm(forms.ModelForm):
    class Meta:
        model = LessonText
        fields = ['title', 'description']

LessonTextFormSet = inlineformset_factory(Course, LessonText, form=LessonTextForm, extra=1, can_delete=True)

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ['title', 'cid', 'description', 'publish', 'status', 'view', 'l']
        widgets = {
            'cid': forms.HiddenInput(),
            'view': forms.HiddenInput(),
        }
