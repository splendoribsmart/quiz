from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Level, Subject, Quiz, Question, Choice, Answer, Point
from .forms import SubjectSelectionForm
from django.db.models import Sum
import random
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Point, User


def home_view(request):
    return render(request, 'home.html', {})

def main_phone_view(request):
    return render(request, 'main_phone.html', {})

def main_desktop_view(request):
    return render(request, 'main_desktop.html', {})

@login_required
def subject_selection_phone_view(request):
    if request.method == 'POST':
        form = SubjectSelectionForm(request.POST)
        if form.is_valid():
            selected_subject = form.cleaned_data['subject']
            sub_id = selected_subject.id
            request.session['sid'] = sub_id
            # levels = Level.objects.filter(subject=selected_subject)
            context = {}    # {'levels': levels}
            return redirect('menu')
    else:
        form = SubjectSelectionForm()

    context = {'form': form}
    return render(request, 'gameplay/subject_selection_phone.html', context)

@login_required
def subject_selection_desktop_view(request):
    # if request.method == 'POST':
    #     selection = request.POST.get('selectedImage')

    #     if selection == "Mathematics":
    #         subject_id = 1
    #     elif selection == "English":
    #         subject_id = 2
    #     elif selection == "Computer":
    #         subject_id = 3
    #     elif selection == "Science":
    #         subject_id = 4
    #     elif selection == "French":
    #         subject_id = 5
    #     elif selection == "Social Studies":
    #         subject_id = 6
        
    #     context = {'subject_id' : subject_id}

    #     selected_subject = Subject.objects.get(name=selection)
    #     sub_id = selected_subject.id
    #     request.session['sid'] = sub_id
    #     levels = Level.objects.filter(subject=selected_subject)
    #     context = {'levels' : levels}
    #     return redirect('menu')
    #     form = SubjectSelectionForm(request.POST)
    #     if form.is_valid():
    #         selected_subject = form.cleaned_data['subject']
    #         sub_id = selected_subject.id
    #         request.session['sid'] = sub_id
    #         # levels = Level.objects.filter(subject=selected_subject)
    #         context = {}    # {'levels': levels}
    #         return redirect('menu')
    # else:
    #     form = SubjectSelectionForm()

    context = {}
    return render(request, 'gameplay/subject_selection_desktop.html', context)


@login_required
def menu_view(request):
    subject_id = request.session['sid']
    print(subject_id)
    context = {'subject_id' : subject_id}
    return render(request, 'gameplay/menu.html', context)

@login_required
def phone_menu_view(request):
    # subject_id = request.session['sid']
    # print(subject_id)
    # context = {'subject_id' : subject_id}
    return render(request, 'gameplay/menu_phone.html', {})

@login_required
def desktop_menu_view(request):
    # subject_id = request.session['sid']
    # print(subject_id)
    # context = {'subject_id' : subject_id}
    return render(request, 'gameplay/menu_desktop.html', {})

# @login_required
# def level_selection_view(request, subject_id):
#     subject = get_object_or_404(Subject, pk=subject_id)
#     levels = Level.objects.filter(subject=subject)
#     context = {'subject': subject, 'levels': levels}
#     return render(request, 'gameplay/level_selection.html', context)

@login_required
def level_selection_view(request, subject_id):
    # subject_id = request.session['sid']
    subject = get_object_or_404(Subject, pk=subject_id)
    levels = Level.objects.filter(subject=subject)
    context = {'subject': subject, 'levels': levels}
    return render(request, 'gameplay/level_selection.html', context)

@login_required
def level_selection_phone(request, subject_id):
    # subject_id = request.session['sid']
    subject = get_object_or_404(Subject, pk=subject_id)
    levels = Level.objects.filter(subject=subject)
    context = {'subject': subject, 'levels': levels}
    return render(request, 'gameplay/level_selection_phone.html', context)

@login_required
def level_selection_desktop(request, subject_id):
    # subject_id = request.session['sid']
    subject = get_object_or_404(Subject, pk=subject_id)
    levels = Level.objects.filter(subject=subject)
    print(levels)
    context = {'subject': subject, 'levels': levels}
    return render(request, 'gameplay/level_selection_desktop.html', context)


# @login_required
# def level_detail_view(request, level_id):
#     level = get_object_or_404(Level, pk=level_id)
#     quizzes = Quiz.objects.filter(level=level)
#     context = {'level': level, 'quizzes': quizzes}
#     return render(request, 'gameplay/level_detail.html', context)

@login_required
def quiz_view_phone(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    request.session['result_quiz_id'] = quiz_id
    print("Quiz ID:  ",request.session['result_quiz_id'])
    user = request.user
    level = quiz.level

    # Reset the quiz points to zero
    quiz_point, created = Point.objects.get_or_create(user=user, level=level)
    quiz_point.quiz_score = 0
    quiz_point.save()

    # Randomly select four questions from the quiz
    questions = list(quiz.question_set.all())
    random.shuffle(questions)
    questions = questions[:4]     # Selecting only 4 questions randomly

    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'questions': questions,
        'question_count': len(questions),
    }
    return render(request, 'gameplay/htp_phone.html', context)

@login_required
def quiz_view_desktop(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    request.session['result_quiz_id'] = quiz_id
    print("Quiz ID:  ",request.session['result_quiz_id'])
    user = request.user
    level = quiz.level

    # Reset the quiz points to zero
    quiz_point, created = Point.objects.get_or_create(user=user, level=level)
    quiz_point.quiz_score = 0
    quiz_point.save()

    # Randomly select four questions from the quiz
    questions = list(quiz.question_set.all())
    random.shuffle(questions)
    questions = questions[:4]     # Selecting only 4 questions randomly

    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'questions': questions,
        'question_count': len(questions),
    }
    return render(request, 'gameplay/htp_desktop.html', context)
# def quiz_view(request, quiz_id):
#     quiz = get_object_or_404(Quiz, pk=quiz_id)
#     user = request.user
#     level = quiz.level

#     # Reset the quiz points to zero
#     quiz_point, created = Point.objects.get_or_create(user=user, level=level)
#     quiz_point.quiz_score = 0
#     quiz_point.save()

#     questions = Question.objects.filter(quiz=quiz)

#     context = {
#         'quiz': quiz,
#         'quiz_point': quiz_point,
#         'questions': questions,
#     }
#     return render(request, 'gameplay/quiz.html', context)



# def quiz_view(request, subject_id):
#     subject = get_object_or_404(Subject, pk=subject_id)
#     user = request.user
#     level = Level.objects.filter(subject=subject).first()
#     quiz_point, created = Point.objects.get_or_create(user=user, level=level)
#     quiz = Quiz.objects.filter(level=level).first()
#     questions_count = quiz.questions_count

#     context = {
#         'subject': subject,
#         'quiz': quiz,
#         'quiz_point': quiz_point,
#         'questions_count': questions_count,
#     }
#     return render(request, 'quiz.html', context)

@login_required
def question_view(request, quiz_id, question_index):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    print("Quiz ID:  ",request.session['result_quiz_id'])
    user = request.user
    level = quiz.level
    quiz_point = get_object_or_404(Point, user=user, level=level)

    # Reset the quiz score to zero if starting a new quiz
    if question_index == 0:
        quiz_point.quiz_score = 0
        quiz_point.save()

        # Clear the stored question IDs from the session
        request.session.pop('question_ids', None)

    # Retrieve the stored question IDs from the session
    question_ids = request.session.get('question_ids')

    # If no question IDs are stored, randomly select four questions and store their IDs in the session
    if not question_ids:
        all_questions = list(Question.objects.filter(quiz=quiz).values_list('id', flat=True))
        random.shuffle(all_questions)
        question_ids = all_questions[:4]
        request.session['question_ids'] = question_ids

    # Get the current question based on the stored IDs and question_index
    current_question_id = question_ids[question_index]
    current_question = get_object_or_404(Question, id=current_question_id)
    choices = current_question.choice_set.all()

    if request.method == 'POST':
        selected_choice_id = request.POST.get('selected_choice')

        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

            if selected_choice.is_correct:
                quiz_point.quiz_score += 1

            quiz_point.save()

        next_question_index = question_index + 1
        if next_question_index < len(question_ids):
            return redirect('question', quiz_id=quiz_id, question_index=next_question_index)
        else:
            return redirect('quiz_result', quiz_id=quiz.id, point_id=quiz_point.id)

    # Adjust the question numbering for display
    question_number = question_index + 1
    total_questions = len(question_ids)

    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'question': current_question,
        'choices': choices,
        'selected_choice': None,
        'question_number': question_number,
        'total_questions': total_questions,
    }
    return render(request, 'gameplay/question.html', context)

@login_required
def question_view_phone(request, quiz_id, question_index):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    print("Quiz ID:  ",request.session['result_quiz_id'])
    user = request.user
    level = quiz.level
    quiz_point = get_object_or_404(Point, user=user, level=level)

    # Reset the quiz score to zero if starting a new quiz
    if question_index == 0:
        quiz_point.quiz_score = 0
        quiz_point.save()

        # Clear the stored question IDs from the session
        request.session.pop('question_ids', None)

    # Retrieve the stored question IDs from the session
    question_ids = request.session.get('question_ids')

    # If no question IDs are stored, randomly select four questions and store their IDs in the session
    if not question_ids:
        all_questions = list(Question.objects.filter(quiz=quiz).values_list('id', flat=True))
        random.shuffle(all_questions)
        question_ids = all_questions[:20]
        request.session['question_ids'] = question_ids

    # Get the current question based on the stored IDs and question_index
    current_question_id = question_ids[question_index]
    current_question = get_object_or_404(Question, id=current_question_id)
    choices = current_question.choice_set.all()

    first_choice = choices[0]
    second_choice = choices[1]
    third_choice = choices[2]
    fourth_choice = choices[3]
    print('first_choice: ', first_choice)
    print('first_choice ID: ', first_choice.id)

    if request.method == 'POST':
        selected_choice_id = request.POST.get('selected_choice')

        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

            if selected_choice.is_correct:
                quiz_point.quiz_score += 1

            quiz_point.save()

        next_question_index = question_index + 1
        if next_question_index < len(question_ids):
            return redirect('questionphone', quiz_id=quiz_id, question_index=next_question_index)
        else:
            return redirect('quiz_result_phone', quiz_id=quiz.id, point_id=quiz_point.id)

    # Adjust the question numbering for display
    question_number = question_index + 1
    total_questions = len(question_ids)

    percent_question = ((question_number - 1) / 20) * 100

    progress = f'<div class="w3-green" style="height:24px;width:{percent_question}%"></div>'

    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'question': current_question,
        'choices': choices,
        'first_choice' : first_choice,
        'second_choice' : second_choice,
        'third_choice' : third_choice,
        'fourth_choice' : fourth_choice,
        'selected_choice': None,
        'question_number': question_number,
        'total_questions': total_questions,
        'percent_quetion' : percent_question,
        'progress' : progress,
    }
    return render(request, 'gameplay/question_phone.html', context)

@login_required
def question_view_desktop(request, quiz_id, question_index):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    print("Quiz ID:  ",request.session['result_quiz_id'])
    user = request.user
    level = quiz.level
    quiz_point = get_object_or_404(Point, user=user, level=level)

    # Reset the quiz score to zero if starting a new quiz
    if question_index == 0:
        quiz_point.quiz_score = 0
        quiz_point.save()

        # Clear the stored question IDs from the session
        request.session.pop('question_ids', None)

    # Retrieve the stored question IDs from the session
    question_ids = request.session.get('question_ids')

    # If no question IDs are stored, randomly select four questions and store their IDs in the session
    if not question_ids:
        all_questions = list(Question.objects.filter(quiz=quiz).values_list('id', flat=True))
        random.shuffle(all_questions)
        question_ids = all_questions[:20]
        request.session['question_ids'] = question_ids

    # Get the current question based on the stored IDs and question_index
    current_question_id = question_ids[question_index]
    current_question = get_object_or_404(Question, id=current_question_id)
    choices = current_question.choice_set.all()
    print('Choices: ', choices )

    first_choice = choices[0]
    second_choice = choices[1]
    third_choice = choices[2]
    fourth_choice = choices[3]
    print('first_choice: ', first_choice)
    print('first_choice ID: ', first_choice.id)

    if request.method == 'POST':
        selected_choice_id = request.POST.get('selected_choice')
        print('Selected Choice: ', request.POST.get('selected_choice'))

        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

            if selected_choice.is_correct:
                quiz_point.quiz_score += 1

            quiz_point.save()

        next_question_index = question_index + 1
        if next_question_index < len(question_ids):
            return redirect('questiondesktop', quiz_id=quiz_id, question_index=next_question_index)
        else:
            return redirect('quiz_result_desktop', quiz_id=quiz.id, point_id=quiz_point.id)

    # Adjust the question numbering for display
    question_number = question_index + 1
    total_questions = len(question_ids)

    percent_question = ((question_number - 1) / 20) * 100

    progress = f'<div class="w3-green" style="height:24px;width:{percent_question}%"></div>'


    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'question': current_question,
        'choices': choices,
        'first_choice' : first_choice,
        'second_choice' : second_choice,
        'third_choice' : third_choice,
        'fourth_choice' : fourth_choice,
        'selected_choice': None,
        'question_number': question_number,
        'total_questions': total_questions,
        'progress' : progress
    }
    return render(request, 'gameplay/question_desktop.html', context)
# def question_view(request, quiz_id, question_index):
#     quiz = get_object_or_404(Quiz, pk=quiz_id)
#     user = request.user
#     level = quiz.level
#     quiz_point = get_object_or_404(Point, user=user, level=level)
#     questions = Question.objects.filter(quiz=quiz)

#     if question_index >= questions.count():
#         return redirect('quiz_result', point_id=quiz_point.id)

#     current_question = questions[question_index]
#     choices = current_question.choice_set.all()

#     if request.method == 'POST':
#         selected_choice_id = request.POST.get('selected_choice')

#         if selected_choice_id:
#             selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

#             if selected_choice.is_correct:
#                 quiz_point.quiz_score += 1

#             quiz_point.save()

#         next_question_index = question_index + 1
#         if next_question_index < questions.count():
#             return redirect('question', quiz_id=quiz_id, question_index=next_question_index)
#         else:
#             return redirect('quiz_result', point_id=quiz_point.id)

#     # Adjust the question numbering for display
#     question_number = question_index + 1
#     total_questions = questions.count()

#     context = {
#         'quiz': quiz,
#         'quiz_point': quiz_point,
#         'question': current_question,
#         'choices': choices,
#         'selected_choice': None,
#         'question_number': question_number,
#         'total_questions': total_questions,
#     }
#     return render(request, 'gameplay/question.html', context)



@login_required
def submit_quiz_view(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        total_questions = questions.count()
        correct_answers = 0

        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    correct_answers += 1

        user = request.user
        level = quiz.level

        # Update quiz-specific point count
        quiz_point, created = Point.objects.get_or_create(user=user, level=level)

        if total_questions >= 3:
            if not created:
                # Reset quiz-specific point count to zero if the point object already exists
                quiz_point.quiz_score = 0

            quiz_point.quiz_score += correct_answers
            quiz_point.save()

            if quiz_point.quiz_score >= quiz.passing_score:
                next_level = Level.objects.filter(subject=level.subject, number=level.number + 1).first()
                if next_level:
                    return redirect('level_selection', subject_id=level.subject.id)
                else:
                    request.session['start_countdown'] = True
                    return redirect('quiz_result', point_id=quiz_point.id)
            else:
                return redirect('level_selection', subject_id=level.subject.id)
        else:
            # Redirect to an error page if the quiz does not have at least three questions
            return render(request, 'quiz_error.html')


@login_required
def quiz_result_view(request, quiz_id, point_id):
    quiz_point = get_object_or_404(Point, id=point_id)
    level = quiz_point.level
    print("Current Level: ", level)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    next_level = Level.objects.filter(subject=level.subject, number=level.number+1).first()

    total_questions = 20
    my_score = total_questions - quiz_point.quiz_score
    can_proceed = my_score <= 3

    # Update the total score if the current quiz score is higher
    if can_proceed:
        if my_score > quiz_point.total_score:
            quiz_point.total_score = quiz_point.quiz_score
            quiz_point.save()

    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'can_proceed': can_proceed,
        'total_questions': total_questions,
        'next_level': next_level,
    }
    return render(request, 'gameplay/quiz_result.html', context)

@login_required
def quiz_result_phone(request, quiz_id, point_id):
    quiz_point = get_object_or_404(Point, id=point_id)
    level = quiz_point.level
    quiz = get_object_or_404(Quiz, id=quiz_id)
    next_level = Level.objects.filter(subject=level.subject, number=level.number+1).first()

    total_questions = 20
    my_score = total_questions - quiz_point.quiz_score
    can_proceed = my_score <= 3

    # Update the total score if the current quiz score is higher
    if can_proceed:
        if my_score > quiz_point.total_score:
            quiz_point.total_score = quiz_point.quiz_score
            quiz_point.save()

    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'can_proceed': can_proceed,
        'total_questions': total_questions,
        'next_level': next_level,
        'level' : level,
    }
    return render(request, 'gameplay/quiz_result_phone.html', context)

@login_required
def quiz_result_desktop(request, quiz_id, point_id):
    quiz_point = get_object_or_404(Point, id=point_id)
    level = quiz_point.level
    quiz = get_object_or_404(Quiz, id=quiz_id)
    next_level = Level.objects.filter(subject=level.subject, number=level.number+1).first()

    total_questions = 20
    my_score = total_questions - quiz_point.quiz_score
    can_proceed = my_score <= 3

    # Update the total score if the current quiz score is higher
    if can_proceed:
        if my_score > quiz_point.total_score:
            quiz_point.total_score = quiz_point.quiz_score
            quiz_point.save()

    context = {
        'quiz': quiz,
        'quiz_point': quiz_point,
        'can_proceed': can_proceed,
        'total_questions': total_questions,
        'next_level': next_level,
        'level' : level,
    }
    return render(request, 'gameplay/quiz_result_desktop.html', context)

# def quiz_result_view(request, quiz_id, point_id):
#     quiz_point = get_object_or_404(Point, id=point_id)
#     # my_id = request.session['result_quiz_id']
#     # print("This is my Quiz ID:  ", my_id)
#     level = quiz_point.level
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     next_level = Level.objects.filter(subject=level.subject, number=level.number+1).first()

#     total_questions = 4
#     can_proceed = (total_questions - quiz_point.quiz_score) <= 3

#     print(can_proceed)

#     context = {
#         'quiz': quiz,
#         'quiz_point': quiz_point,
#         'can_proceed': can_proceed,
#         'total_questions' : total_questions,
#         'next_level': next_level,
#     }
#     return render(request, 'gameplay/quiz_result.html', context)



@login_required
def leaderboard_view(request):
    # Calculate the leaderboard score by summing up all total scores
    leaderboard_score = Point.objects.aggregate(Sum('total_score'))['total_score__sum'] or 0

    # Fetch all points ordered by total score in descending order
    all_points = Point.objects.order_by('-total_score')

    leaderboard = []
    rank = 1

    for point in all_points:
        total_score = point.total_score

        # Check if the user is already in the leaderboard
        if point.user not in [entry['user'] for entry in leaderboard]:
            leaderboard.append({'user': point.user, 'total_score': total_score, 'rank': rank})
            rank += 1

    first_position = leaderboard[0]
    second_position = leaderboard[1]
    third_position = leaderboard[2]
    fourth_position = leaderboard[3]
    fifth_position = leaderboard[4]
    
    print(first_position)

    context = {
        'leaderboard_score': leaderboard_score,
        'leaderboard': leaderboard,
        'first_position' : first_position,
        'second_position' : second_position,
        'third_position' : third_position,
        'fourth_position' : fourth_position,
        'fifth_position' : fifth_position,
    }

    return render(request, 'gameplay/leaderboard.html', context)


@login_required
def leaderboard_desktop_view(request):
    # Calculate the leaderboard score by summing up all total scores
    leaderboard_score = Point.objects.aggregate(Sum('total_score'))['total_score__sum'] or 0

    # Fetch all points ordered by total score in descending order
    all_points = Point.objects.order_by('-total_score')

    leaderboard = []
    rank = 1

    for point in all_points:
        total_score = point.total_score

        # Check if the user is already in the leaderboard
        if point.user not in [entry['user'] for entry in leaderboard]:
            leaderboard.append({'user': point.user, 'total_score': total_score, 'rank': rank})
            rank += 1

    first_position = leaderboard[0]
    second_position = leaderboard[1]
    third_position = leaderboard[2]
    fourth_position = leaderboard[3]
    fifth_position = leaderboard[4]
    
    # print(first_position)

    context = {
        'leaderboard_score': leaderboard_score,
        'leaderboard': leaderboard,
        'first_position' : first_position,
        'second_position' : second_position,
        'third_position' : third_position,
        'fourth_position' : fourth_position,
        'fifth_position' : fifth_position,
    }

    return render(request, 'gameplay/leaderboard_desktop.html', context)

@login_required
def leaderboard_phone_view(request):
    # Calculate the leaderboard score by summing up all total scores
    leaderboard_score = Point.objects.aggregate(Sum('total_score'))['total_score__sum'] or 0

    # Fetch all points ordered by total score in descending order
    all_points = Point.objects.order_by('-total_score')

    leaderboard = []
    rank = 1

    for point in all_points:
        total_score = point.total_score

        # Check if the user is already in the leaderboard
        if point.user not in [entry['user'] for entry in leaderboard]:
            leaderboard.append({'user': point.user, 'total_score': total_score, 'rank': rank})
            rank += 1

    first_position = leaderboard[0]
    second_position = leaderboard[1]
    third_position = leaderboard[2]
    fourth_position = leaderboard[3]
    fifth_position = leaderboard[4]
    
    # print(first_position)
    # print(first_position['user']['first_name'])

    context = {
        'leaderboard_score': leaderboard_score,
        'leaderboard': leaderboard,
        'first_position' : first_position,
        'second_position' : second_position,
        'third_position' : third_position,
        'fourth_position' : fourth_position,
        # 'fifth_position' : fifth_position,
    }

    return render(request, 'gameplay/leaderboard_phone.html', context)
# def leaderboard_view(request):
#     # Calculate the leaderboard score by summing up all total scores
#     leaderboard_score = Point.objects.aggregate(Sum('total_score'))['total_score__sum'] or 0

#     # Fetch unique users associated with the points
#     users = User.objects.filter(point__total_score__gt=0).distinct().order_by('-point__total_score')

#     leaderboard = []
#     rank = 1

#     for user in users:
#         user_points = Point.objects.filter(user=user)
#         total_score = user_points.aggregate(Sum('total_score'))['total_score__sum'] or 0

#         leaderboard.append({'user': user, 'total_score': total_score, 'rank': rank})
#         rank += 1

#     context = {
#         'leaderboard_score': leaderboard_score,
#         'leaderboard': leaderboard,
#     }

#     return render(request, 'gameplay/leaderboard.html', context)
# def leaderboard_view(request):
#     # Query all users and calculate their total scores using the Sum aggregation function
#     leaderboard = Point.objects.values('user').annotate(total_score=Sum('total_score')).order_by('-total_score')

#     context = {
#         'leaderboard': leaderboard,
#     }
#     return render(request, 'gameplay/leaderboard.html', context)

@login_required
def custom_logout(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the URL name of your home page view

@login_required
def custom_logout_phone(request):
    logout(request)
    return redirect('mainphone')  # Replace 'home' with the URL name of your home page view

@login_required
def custom_logout_desktop(request):
    logout(request)
    return redirect('maindesktop')  # Replace 'home' with the URL name of your home page view




# Welcome and How to play
@login_required
def wlc_desktop_view(request):
    return render(request, 'gameplay/wlc_desktop.html', {})

@login_required
def wlc_phone_view(request):
    return render(request, 'gameplay/wlc_phone.html', {})

@login_required
def htp_desktop_view(request):
    return render(request, 'gameplay/htp_desktop.html', {})

@login_required
def htp_phone_view(request):
    return render(request, 'gameplay/htp_phone.html', {})