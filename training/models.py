import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    cud = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)


class Course(models.Model):
    title = models.CharField(max_length=100)
    cud = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.cud)])

    def __str__(self):
        return f"{self.title} ({self.cud})"


class LessonText(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson_texts',
                               related_query_name='lesson_text')

    class Meta:
        verbose_name = 'Текстовый урок'
        verbose_name_plural = 'Текстовые уроки'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('lesson_text_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.title} ({self.course.title})"

    def get_course_absolute_url(self):
        return self.course.get_absolute_url()


class LessonVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson_videos',
                               related_query_name='lesson_video')

    class Meta:
        verbose_name = 'Видеоурок'
        verbose_name_plural = 'Видеоуроки'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('lesson_video_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.title} ({self.course.title})"

    def get_course_absolute_url(self):
        return self.course.get_absolute_url()
