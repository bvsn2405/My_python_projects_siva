from django.contrib.auth.models import User
from django.db.models import F, Sum, Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from quiz_app.models.answered_questions import Answered_Questions


@csrf_exempt
def get_scores(request):
    """
    View function to retrieve scores and attempted questions for each participant.

    Accepts a GET request to retrieve the total scores and the number of attempted questions for each participant.
    Calculates the cumulative scores of participants using the 'Answered_Questions' model and counts the number
    of questions attempted by each participant.
    Returns a JSON response containing the scores and the number of attempted questions for each participant.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: JSON response with a list of participants along with their scores and attempted questions.

    Example Usage:
        - Request URL: GET /scores/
        - Response:
            {
                "Scores Data": [
                    {
                        "User": "Abhi",
                        "Total Score": 235,
                        "Attempted Questions": 15
                    },
                    {
                        "User": "Siva",
                        "Total Score": 189,
                        "Attempted Questions": 12
                    },
                    ...
                ]
            }
    """
    try:
        if request.method == "GET":

            # cumulative_scores = Answered_Questions.objects.values('user').annotate(cumulative_score=Sum(F('score')))

            cumulative_scores = Answered_Questions.objects.values('user').annotate(cumulative_score=Sum(F('score')),
                                                                                   count=Count('score'))
            scores_list = []
            for user_score in cumulative_scores:
                user = User.objects.get(id=user_score['user'])
                username = user.username
                cumulative_score = user_score['cumulative_score']
                scores_data = {"User": username,
                               "Total Score": cumulative_score,
                               "Attempted Questions": user_score['count']}
                scores_list.append(scores_data)
            return JsonResponse({"Scores Data": scores_list})
    except:
        return JsonResponse({"Message": "Invalid Method"}, status=400)
    return JsonResponse({"Message": "Invalid Method"}, status=400)
