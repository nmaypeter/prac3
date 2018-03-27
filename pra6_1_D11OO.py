class Ironman:
    '''這是一個叫做 Ironman 的類別'''  # Doc string
    def __init__(self, group, participants):
        self.group = group
        self.participants = participants

    def print_info(self):
        print(self.group, 'has', self.participants, 'people.')

# Articles 類別繼承 Ironman 類別
class Articles(Ironman):
    def print_articles(self):
        print(self.group, 'has', self.participants * 30, 'articles.')
'''
print(Ironman)
print(type(Ironman))
'''
# 根據 Ironmen 類別建立一個物件 modern_web
modern_web = Ironman('Morden Web', 54)
# 根據 Ironmen 類別建立一個物件 dev_ops
dev_ops = Ironman('DevOps', 8)
company_group = Articles('Company Group', 2)
'''
print(modern_web)
print(type(modern_web))
'''
'''
print(modern_web.group)
print(modern_web.participants)
print(modern_web.__doc__)
'''
modern_web.print_info()
dev_ops.print_info()
company_group.print_info()
company_group.print_articles()