from matchers import And, HasAtLeast, PlaysIn, All, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All):
        self._matcher = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))

    def build(self):
        return self._matcher
