from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from training.forms import CourseCreateForm, LessonTextFormSet
from training.models import Course


def index(request):
    title = 'Онлайн курсы'
    course = Course.published.all()
    context = {
        'title': title
    }
    return render(request, 'templates_course/course/home.html', context)


class CourseListView(ListView):
    model = Course
    template_name = 'templates_course/course/home.html'
    context_object_name = 'courses'
    queryset = Course.published.all()


class CourseCreateView(CreateView):
    model = Course
    template_name = 'templates_course/course/create.html'
    context_object_name = 'course'
    success_url = reverse_lazy('course_detail')
    form_class = CourseCreateForm

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'cid': self.object.cid})


    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #
    #     # сохраняем уроки
    #     lesson_texts = form.cleaned_data.get('lesson_texts')
    #     for lesson_text in lesson_texts:
    #         if lesson_text:
    #             lesson_text.course = self.object
    #             lesson_text.save()

        # # сохраняем видеоуроки
        # lesson_videos = form.cleaned_data.get('lesson_videos')
        # for lesson_video in lesson_videos:
        #     if lesson_video:
        #         lesson_video.course = self.object
        #         lesson_video.save()

        # return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_text_formset'] = LessonTextFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        lesson_text_formset = context['lesson_text_formset']
        if lesson_text_formset.is_valid():
            self.object = form.save()
            lesson_text_formset.instance = self.object
            lesson_text_formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, lesson_text_formset=lesson_text_formset))
class CourseDetailView(DetailView):
    model = Course
    template_name = 'templates_course/course/detail.html'
    context_object_name = 'course'
    slug_field = 'cid'
    slug_url_kwarg = 'cid'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view += 1
        obj.save()
        return obj
