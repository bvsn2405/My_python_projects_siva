from django.contrib.auth.models import User
from django.db.models import F, Sum
from django.http import JsonResponse

from quiz_app.models.answered_questions import Answered_Questions


def get_ranks(request):
    """
    View function to retrieve rankings based on cumulative scores of participants.

    Accepts a GET request to retrieve rankings of participants based on their cumulative scores.
    Calculates the cumulative scores of participants using the 'Answered_Questions' model.
    Orders the participants in descending order of cumulative scores to determine the ranks.
    Returns a JSON response containing the rankings of participants along with their cumulative scores.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with a list of participants ranked by their cumulative scores.

    Example Usage:
        - Request URL: GET /ranks/
        - Response:
            {
                "Rank": [
                    {
                        "User": "siva",
                        "Total Score": 235,
                        "Rank": 1
                    },
                    {
                        "User": "Abhi",
                        "Total Score": 189,
                        "Rank": 2
                    },
                    ...
                ]
            }
    """

    if request.method == "GET":

        cumulative_scores = Answered_Questions.objects.values('user').annotate(
            cumulative_score=Sum(F('score'))).order_by('-cumulative_score')
        scores_list = []
        rank = 1
        for user_score in cumulative_scores:
            user = User.objects.get(id=user_score['user'])
            username = user.username
            scores_data = {"User": username,
                           "Total Score": user_score['cumulative_score'],
                           "Rank": rank}
            scores_list.append(scores_data)
            rank += 1
        return JsonResponse({"Rank": scores_list})
    return JsonResponse({"Message": "Invalid"})
