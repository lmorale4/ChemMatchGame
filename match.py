'''
Linda Morales and Mitchell Coffin
lmorale4@binghamton.edu
mcoffin1@binghamton.edu
'''
'''
Analysis:

This class matches the two entries by the user according to a dictionary
'''
# ----------------------------------------------------------------------------
# Constants

# Collab
# Dictionary that matches the molecules to the name
CHEMDICT = {'CH4':'Methane', 'H2O':'Water', 'C2H6':'Ethane', 'C3H8':'Propane',\
            'C2H2':'Ethyne', 'C6H6':'Benzene', 'C8H10':'P-xylene'}

# Class that matches molecule chosen by the user to
# a name chosen by the user
class Match:
  # Linda
  # Constructor----------------------------
  # param aDict (dict) - Dictionary
  def __init__(self, aDict):
    self.__dict = aDict
    self.__molecule = ''
    self.__name = ''

  # Mitchell
  # Predicate------------------------------
  # compares the entries by the user to the
  # content of the dictionary
  def matchEntries(self):
    return self.__dict[self.__molecule] == self.__name

  # Accessors------------------------------

  # Linda
  # returns a list of the dictionary keys
  def getDictKeys(self):
    return list((self.__dict).keys())

  # returns a list of the dictionary values
  def getDictValues(self):
    return list((self.__dict).values())

  # Mutators-------------------------------

  # Mitchell
  # param molecule (str) - molecule
  # takes in a molecule and assigns it to a new variable
  def setMolecule(self, molecule):
    self.__molecule = molecule

  # param name (str) - name
  # takes in a name and assigns it to a new variable
  def setName(self, name):
    self.__name = name

  
  
'''
# Test

def main():
  userMol = input('What is the molecular formula? ')
  userMolName = input('What is the name of this molecule? ')

  instance = Match(CHEMDICT, userMol, userMolName)
  if instance.matchEntries():
    print('Correct: %s is named %s' %(userMol, userMolName))
  else:
    print('Incorrect: %s does not match with %s' %(userMol, userMolName))
      

main()
'''
