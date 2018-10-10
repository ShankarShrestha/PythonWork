def main ()
    #score = int(input('enter score'))
    #gradeCalculation(score)
    #gradeCalculationRange(score)
    phrase = input(Enter The Phrase )
    #findAcronym(phrase)
    #findCharacterstics(phrase)
    findCharactersticsFullName(phrase)
    
    
   
"""A certain CS professor gives 5-point quizzes that are 
graded on the scale 5-A, 4-B, 3,-C, 2-D, 1-F, 0-F. 
Write a program that accepts a quiz score as an input and prints out the 
corresponding grade."""
   
def gradeCalculation(score)
    scoreList = [5, 4, 3, 2, 1, 0]
    gradeList = ['A','B','C','D','F']

    if score in scoreList
        scoreIndex = scoreList.index(score)    
        grade = gradeList[scoreIndex]
	if scoreIndex == 4 or scoreIndex == 5:
		grade = gradelist[4] 
        print(Grade= {}.format(grade))
    
    else
        print(invalid input)
        
        
def gradeCalculationRange(score)
    gradeList = ['A','B','C','D','F']
    if (score = 90 and score = 100)
        index = 0
    elif (score = 80 and score = 89)
        index = 1
    elif (score = 70 and score = 79)
        index = 2
    elif (score = 60 and score = 99)
        index = 3
    elif (score  60)
        index = 4
        
    print(Grade = {} .format(gradeList[index]))
    
        
def findAcronym(phrase)
    wordList = phrase.split( )
    abb = 
    for word in wordList
      abb += word[01]
      
    print(Acronym {}  .format(abb.upper()))
    
def findCharacterstics(name)
    import string
    alpha = string.ascii_lowercase
    
    totalSum = 0
    
    for ch in name
        index = alpha.index(ch)
        totalSum += index+1      
        
    print ('Total Sum = {}'.format(totalSum))
    
def findCharactersticsFullName(fullname)
    import string
    alpha = string.ascii_lowercase
    
    totalSum = 0
    nameList = fullname.split( )
    for name in nameList
        for ch in name
            index = alpha.index(ch)
            totalSum += index+1      
        
    print ('Total Sum = {}'.format(totalSum))
               
    
    

   
    
main()    
    


