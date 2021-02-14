from hemlock import Branch, Page, Label, route
from hemlock.tools import Assigner

assigner = Assigner({
    'set0': ['A', 'B', 'C', 'D'],
    'set1': ['E', 'F', 'G', 'H']
})

@route('/survey')
def start():
    conditions = assigner.next()
    return Branch(
        Page(
            Label('Page '+conditions['set0'])
        ),
        Page(
            Label('Page '+conditions['set1'])
        ),
        Page(
            Label('The end!'), 
            terminal=True
        )
    )