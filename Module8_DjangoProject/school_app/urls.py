from django.urls import path
from school_app.views import students
from school_app.views import login
from school_app.views import logout
from school_app.views import forgot_password


urlpatterns = [
    path('students/create/',students.student_registration_data ),
    path('students/',students.get_all_student_data ),
    path('students/<int:id>/', students.get_student_data),
    path('student/update/<int:id>/', students.update_student_data),
    path('student/delete/<int:id>/', students.delete_student_data),
    path('login/',login.login_view),
    path('logout/',logout.logout_view),
    path('students/activate/<str:token>/', students.activate, name='activate'),
    path('students/forgot_password/',forgot_password.forgot_password),
    path('students/forgot_password_reset/',forgot_password.forgot_password_otp_validation),

    

]