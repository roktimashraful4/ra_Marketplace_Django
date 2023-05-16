from atexit import register
from datetime import date
from django import template
register = template.Library()

@register.filter
def days_until(d):
    delta = d - date.today()
    # delta +=1
    return delta.days+1
register.filter("days_until", days_until)

@register.filter
def cet_count(d):
    delta = len(d)
    e = 0
    for i in range(len(d)):
        if d[i].is_expir == False : 
            e +=1

    # delta +=1
    return e
register.filter("cet_count", cet_count)