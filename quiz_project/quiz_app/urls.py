from django.urls import path
from quiz_app.views.activate_user_account import activate_account
from quiz_app.views.add_questions import add_questions
from quiz_app.views.delete_question import delete_question
from quiz_app.views.display_all_questions import display_all_questions, display_question
from quiz_app.views.display_answered_questions import display_answered_questions
from quiz_app.views.get_feedbacks import get_feedbacks, get_feedback_by_id, get_feedback_by_user_id
from quiz_app.views.login import login_view
from quiz_app.views.logout import logout_view
from quiz_app.views.participants_registration import participants_reg
from quiz_app.views.participants_update import update_participant_data
from quiz_app.views.ranking import get_ranks
from quiz_app.views.scoring import get_scores
from quiz_app.views.submit_answer_to_question import submit_answer_to_question
from quiz_app.views.submit_feedback import submit_feedback
from quiz_app.views.update_question import update_question
from quiz_app.views.forgot_password import forgot_password,forgot_password_otp_validation
from quiz_app.views.password_reset import password_reset


urlpatterns = [
    path('participants/reg/', participants_reg),
    path('login/', login_view),
    path('logout/', logout_view),
    path('add_questions/', add_questions),
    path('participants/update/', update_participant_data),
    path('questions/', display_all_questions),
    path('question/<int:id>/', display_question),
    path('questions/submit_answer/<int:id>/', submit_answer_to_question),
    path('answered_questions/', display_answered_questions),
    path('scores/', get_scores),
    path('ranks/', get_ranks),
    path('submit_feedback/', submit_feedback),
    path('feedbacks/', get_feedbacks),
    path('feedback/<int:id>/', get_feedback_by_id),
    path('feedback/user/<int:user_id>/', get_feedback_by_user_id),
    path('question/update/<int:id>/', update_question),
    path('question/delete/<int:id>/', delete_question),
    path('activate/<int:id>/<str:token>/', activate_account),
    path('forgot_password/', forgot_password),
    path('forgot_password/otp_validation/', forgot_password_otp_validation),
    path('password_reset/', password_reset),




]
