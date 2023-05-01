from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.translation import gettext_lazy as _

from training.models import LessonText, LessonVideo, Course


class LessonTextInline(admin.TabularInline):
    model = LessonText
    extra = 1
    verbose_name = _("Текстовый урок")
    verbose_name_plural = _("Текстовые уроки")
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':40})},
    }

class LessonVideoInline(admin.TabularInline):
    model = LessonVideo
    extra = 1
    verbose_name = _("Видеоурок")
    verbose_name_plural = _("Видеоуроки")

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonTextInline, LessonVideoInline]

admin.site.register(Course, CourseAdmin)
