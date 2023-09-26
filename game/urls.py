from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    subject_selection_phone_view,
    subject_selection_desktop_view,
    level_selection_view,
    # level_detail_view,
    # quiz_view,
    submit_quiz_view,
    quiz_result_view, quiz_result_phone, quiz_result_desktop,
    question_view, question_view_desktop, question_view_phone,
    menu_view, 
    phone_menu_view, desktop_menu_view,
    leaderboard_view,
    wlc_phone_view, wlc_desktop_view, 
    htp_phone_view, htp_desktop_view, 
    quiz_view_phone, quiz_view_desktop,
    level_selection_desktop, level_selection_phone,
)

urlpatterns = [
    # Quiz Game URLs
    path('subject-selection-phone/', subject_selection_phone_view, name='subject_selection_phone'),
    path('subject-selection-desktop/', subject_selection_desktop_view, name='subject_selection_desktop'),
    # path('level-selection/<int:subject_id>/', level_selection_view, name='level_selection'),
    path('level-selection-desktop/<int:subject_id>/', level_selection_desktop, name='level_selection_desktop'),
    path('level-selection-phone/<int:subject_id>/', level_selection_phone, name='level_selection_phone'),
    # path('level-detail/<int:level_id>/', level_detail_view, name='level_detail'),
    # path('quiz/<int:quiz_id>/', quiz_view, name='quiz'),
    path('submit-quiz/<int:quiz_id>/', submit_quiz_view, name='submit_quiz'),
    path('game/quiz-result/<int:quiz_id>/<int:point_id>/', quiz_result_view, name='quiz_result'),
    path('game/quiz-result-phone/<int:quiz_id>/<int:point_id>/', quiz_result_phone, name='quiz_result_phone'),
    path('game/quiz-result-desktop/<int:quiz_id>/<int:point_id>/', quiz_result_desktop, name='quiz_result_desktop'),

    # path('quiz-result/<int:point_id>/', quiz_result_view, name='quiz_result'),
    path('quiz/<int:quiz_id>/question/<int:question_index>/', question_view, name='question'),
    path('quiz/<int:quiz_id>/question-phone/<int:question_index>/', question_view_phone, name='questionphone'),
    path('quiz/<int:quiz_id>/question-desktop/<int:question_index>/', question_view_desktop, name='questiondesktop'),
    path('menu/', menu_view, name='menu'),
    path('phone-menu/', phone_menu_view, name='phonemenu'),
    path('desktop-menu/', desktop_menu_view, name='desktopmenu'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('wlc-phone/', wlc_phone_view, name='wlcphone'),
    path('wlc-desktop/', wlc_desktop_view, name='wlcdesktop'),
    path('htp-phone/<int:quiz_id>/', quiz_view_phone, name='htpphone'),
    path('htp-desktop/<int:quiz_id>/', quiz_view_desktop, name='htpdesktop'),
]
