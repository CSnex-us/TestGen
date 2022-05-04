# Assessment Generator:
#   creates n assessment versions of m questions in random order along with corresponding answer key(s)

import random

# Temporary Data Structure for Assessment Content: Dictionary with Key as Question, value[0] correct answer and value[1:] false answers.
qBank = {
    'What is Git?': ('True', 'False'), 
    'Git is the same as GitHub?': ('A version control system', 'A remote repository platform', 'A nickname for GitHub', 'A programming language'), 
    'Boolean Values can be either True or False': ('True', 'False'), 
    'What is the command to get the installed version of Git?': ('git -version', 'getGitVersion', 'git help version', 'gitVersion'), 
    'What is the command to commit the stages changes for the Git repository?': ('git commit', 'git snapshot', 'git com', 'git save'),      
    }

print(qBank['What is Git?'])

numTests = int(input("How many tests need to be prepared? "))
#print(type(numTests))

for testNum in range(numTests):
    # Create the test and answer key files.
    quizFile = open(f'gitQuiz{testNum +1}.txt', 'w')
    answerKeyFile = open(f'gitQuizAnswers{testNum + 1}.txt', "w")

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((" " * 20) + f'Git and GitHub Quiz (version {testNum +1})')
    quizFile.write("\n\n")

    # TODO: Shuffle the order of the question bank.
    qBankShuffle = list(qBank.keys())
    random.shuffle(qBankShuffle)
    print(qBankShuffle)

    # TODO: Loop through the question bank, making a question for each.
    qBankLength = len(qBank)
    #for question in range(qBankLength):
    for index, (key, value) in enumerate(qBank.items()):
        print(f'Index: {index} :: {key}  -  {value[0]}')
        #   TODO: Get correct and incorrect answers - correct => qBank[]

    #print(qBankLength)


    quizFile.close()
    answerKeyFile.close()


#print(f"The question is: {qBank1['What is Git?']}")


