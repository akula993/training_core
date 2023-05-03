import random
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Category(models.Model):
    title = models.CharField(max_length=100)
    caid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet='abcdefgh12345')


class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    )
    title = models.CharField(max_length=100)
    cid = ShortUUIDField(unique=True,
                         length=7,
                         max_length=30,
                         prefix="cid",
                         alphabet='1234567890cou')
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    view = models.IntegerField(default=0)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'cid': str(self.cid)})

    def __str__(self):
        return f"{self.title} ({self.cid})"


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
