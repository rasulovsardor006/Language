from modeltranslation.translator import register, TranslationOptions

from apps.blog.models import Category, Post


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
