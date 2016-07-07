#coding=utf-8
class Recipe:
    def __init__(self):
        self.set_default_recipes()
        return
    def set_default_recipes(self):
        self.recipes = {'cheese':{'eggs':1,'milk':1,'cheese':1},'mushroom':{'eggs':2,'milk':1,'cheese':1,'mushroom':2},'onion':{'eggs':2,'milk':1,'cheese':1,'onion':1}}
    def get(self,name):
        try:
            recipe = self.recipes[name]
            return recipe
        except KeyError:
            return False

    def create(self,name,ingredients={}):
        self.recipes[name] = ingredients

    def display(self):
        print ('this class Recipe has a def named display')

class Test():
	def test_print():
		print('Recipe.py/class test/def test_print')

if __name__ == '__main__':
    print('test recipe')
