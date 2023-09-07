# Defining the User class
class User:
    def __init__(self, name):
        self.name= name


# Defining the Subclasses of class user
class Student(User):
    def __init__(self, name ,rollno):
        super().__init__(name)
        self.rollno=rollno

class Teacher(User):
    def __init__(self, name, ID):
        super().__init__(name)
        self.ID=ID

class Parent(User):
    def __init__(self, name,contact,child):
        super().__init__(name)
        self.contact=contact
        self.child=child


#Adding the Quiz class
class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
        self.participants = []
        self.submissions = {}

    #Adding Questions to thed Quiz
    def add_question(self, question):
        self.questions.append(question)

    #Inviting the participants to the quiz
    def invite_participant(self, user):
        self.participants.append(user)

    def enable_submissions(self):
         for participant in self.participants:
           self.submissions[participant] = {}

    #Adding the Participant
    def add_participant(self, user):
        if user in self.participants:
            print(f"{user.name} is already a participant.")
        else:
            self.participants.append(user)

    #submitting the Quiz
    def submit_quiz(self, user, answers):
        if user in self.submissions:
            self.submissions[user] = answers
            print(f"{user.name}'s submission is recorded.")
        else:
            print(f"{user.name} is not a participant in this quiz.")

    #getting the Results
    def get_quiz_results(self):
        results = {}
        for user, answers in self.submissions.items():
            score = 0
            for q, correct_answer in self.questions.items():
                if q in answers and answers[q] == correct_answer:
                    score += 1
            results[user] = score
        return results


#Adding the Quiz
class QuizManagementSystem:
    def __init__(self):
        self.questions=[]

    def create_quiz(self, title, questions):
        quiz = Quiz(title, questions)
        self.questions.append(quiz)
        return quiz

#Driver Code#
if __name__ == "__main__":
      #initialize the student, teacher and parent
      stud=Student("Ankit", 12345)
      stud2=Student("Abhishek", 12346)
      stud3=Student("Aashika", 98765)

      #add the Questions
      quiz_questions = {
        "What kind of language is Python?": "interpreted",
        "Which can be changed once declared in python, List or Tuple?": "List",
      }
      quizzess=QuizManagementSystem()
      quiz=quizzess.create_quiz("Programming with Python",quiz_questions)


      #inviting the users to the Quiz
      quiz.invite_participant(stud)
      quiz.invite_participant(stud2)
      quiz.invite_participant(stud3)
      quiz.enable_submissions()
     
      #Recording the Answers of the Students
      studanswers= {
              "What kind of language is Python?": "interpreted",
              "Which can be changed once declared in python, List or Tuple?": "List",
                 }

      stud2answers= {
                "What kind of language is Python?": "compiled",
                "Which can be changed once declared in python, List or Tuple?": "List",
                }

      stud3answers= {
                "What kind of language is Python?": "compiled",
                "Which can be changed once declared in python, List or Tuple?": "Tuple",
                }
 
      # Submitting the answers of the participants
      quiz.submit_quiz(stud, studanswers)
      quiz.submit_quiz(stud2,stud2answers)
      quiz.submit_quiz(stud3,stud3answers)
      
      #generating the Results according to the answers of the student
      results = quiz.get_quiz_results()
      for user, score in results.items():
        print(f"{user.name}'s score: {score}")