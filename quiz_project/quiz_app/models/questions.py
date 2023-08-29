from django.db import models
from quiz_app.models.base_model import BaseModel
from django.contrib.auth.models import User

class Questions(BaseModel):
    
    """
    Model representing a question.

    The Questions model stores information about a question, including its text, options, scores,
    weightage, and the user who created it.

    Fields:
        user (ForeignKey to User): The user who created the question.
        question (TextField): The text of the question.
        options (TextField): The options for the question, stored as a JSON-formatted list of strings.
        scores (TextField): The scores corresponding to each option, stored as a JSON-formatted list of integers.
        weightage (FloatField): The weightage or importance of the question.

    Inheritance:
        The Questions model inherits from BaseModel, which provides common fields like 'created_on',
        'created_by', 'updated_on', 'updated_by', and 'is_deleted'.

    Example Usage:
        # Create a new question
        question = Questions.objects.create(
            user=User.objects.get(username='john_doe'),
            question="What is the capital of France?",
            options='["Paris", "London", "Berlin"]',
            scores='[10, 0, 0]',
            weightage=5.0
        )

        # Retrieve questions and related information
        question = Questions.objects.get(pk=1)
        print(question.question)  # Output: "What is the capital of France?"
        print(question.options)   # Output: '["Paris", "London", "Berlin"]'
        print(question.scores)    # Output: '[10, 0, 0]'
        print(question.weightage) # Output: 5.0
        print(question.user)      # Output: <User: john_doe>
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.TextField()
    options = models.TextField()
    scores =models.TextField()
    weightage = models.FloatField()

