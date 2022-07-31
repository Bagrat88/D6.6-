from django import template
from django.db.models import Count, F
from News_Portal.models import Category

register = template.Library()

SWEAR_WORDS = ['триндец', 'сволочь', 'редиска']


@register.filter()
def censor(text: str):
    text.lower()
    text.split()
    for word in text:
        if word in SWEAR_WORDS:
            return f'{word[0]}|{"*"*(len(word)-1)}'
        else:
            return word


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('News_Portal/list_categories.html')
def show_categories(arg1='Hello', arg2='word'):
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories, "arg1":arg1, "arg2":arg2}
