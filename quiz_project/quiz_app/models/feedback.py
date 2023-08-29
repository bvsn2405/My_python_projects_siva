from django.contrib.auth.models import User
from django.db import models
from quiz_app.models.base_model import BaseModel


class Feedback(BaseModel):
    """
    Model representing user feedback.

    The Feedback model stores user feedback along with the user who submitted the feedback,
    the feedback text, and other common fields like creation and update timestamps.

    Fields:
        user (ForeignKey to User): The user who submitted the feedback.
        feedback (TextField): The text of the feedback.

    Inheritance:
        The Feedback model inherits from BaseModel, which provides common fields like 'created_on',
        'created_by', 'updated_on', 'updated_by', and 'is_deleted'.

    Example Usage:
        # Create a new feedback entry
        user = User.objects.get(username='john_doe')
        feedback = Feedback.objects.create(
            user=user,
            feedback="The app is excellent, but it could use some more features."
        )

        # Retrieve feedback and related information
        feedback = Feedback.objects.get(pk=1)
        print(feedback.feedback) # Output: "The app is excellent, but it could use some more features."
        print(feedback.user)     # Output: <User: john_doe>
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
