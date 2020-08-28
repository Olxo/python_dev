from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence

@singledispatch
def htmlize(a):
    return escape(str(a))

print('htmlize registry: ', htmlize.registry)
print('htmlize dispatch: ', htmlize.dispatch)

@htmlize.register(Integral)
def htmlize_integral_number(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print('htmlize 10 - ', htmlize(10))

print('htmlize True - ', htmlize(True))

@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item) for item in l))
    return '<ul>\n' + '\n'.join(items) + '</ul>'

print('htmlize [1, 2, 3] - ', htmlize([1, 2, 3]))

@htmlize.register(str)
def htmlize_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

htmlize('python')

#another way
#---------------------------------------------------------
@htmlize.register(Integral)
def _(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

@htmlize.register(Sequence)
def _(l):
    items = ('<li>{0}</li>'.format(htmlize(item) for item in l))
    return '<ul>\n' + '\n'.join(items) + '</ul>'

@htmlize.register(str)
def _(s):
    return html_escape(s).replace('\n', '<br/>\n')
#---------------------------------------------------------

