from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    subject_selection_view,
    level_selection_view,
    level_detail_view,
    quiz_view,
    submit_quiz_view,
    quiz_result_view,
    question_view,
    # menu_view, 
    phone_menu_view, desktop_menu_view,
    leaderboard_view
)

urlpatterns = [
    # Quiz Game URLs
    path('subject-selection/', subject_selection_view, name='subject_selection'),
    path('level-selection/<int:subject_id>/', level_selection_view, name='level_selection'),
    path('level-detail/<int:level_id>/', level_detail_view, name='level_detail'),
    path('quiz/<int:quiz_id>/', quiz_view, name='quiz'),
    path('submit-quiz/<int:quiz_id>/', submit_quiz_view, name='submit_quiz'),
    path('game/quiz-result/<int:quiz_id>/<int:point_id>/', quiz_result_view, name='quiz_result'),

    # path('quiz-result/<int:point_id>/', quiz_result_view, name='quiz_result'),
    path('quiz/<int:quiz_id>/question/<int:question_index>/', question_view, name='question'),
    # path('menu/', menu_view, name='menu'),
    path('phone-menu/', phone_menu_view, name='phonemenu'),
    path('desktop-menu/', desktop_menu_view, name='desktopmenu'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),

]
