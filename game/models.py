from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Level(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"Level {self.number} ({self.subject.name}) (id:{self.id})"


from django.db import models

class Quiz(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    questions_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Quiz level {self.level.number} {self.level.subject.name} (id:{self.id})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update the questions_count based on the number of questions related to the quiz
        self.questions_count = self.question_set.count()
        super().save(update_fields=['questions_count'])



class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s answer to {self.question.text}"


# class Point(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     level = models.ForeignKey(Level, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.user.username}'s score in Level {self.level.number} ({self.level.subject.name})"


class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    general_score = models.PositiveIntegerField(default=0)
    quiz_score = models.PositiveIntegerField(default=0)
    total_score = models.PositiveIntegerField(default=0)
    school = models.CharField(max_length=120, default="")

    def update_total_score(self):
        # Check if the total score exists for the user
        total_score, created = TotalScore.objects.get_or_create(user=self.user)

        # Retrieve the current total score for the level
        level_total_score = total_score.level_scores.get(str(self.level_id), 0)

        # Update the total score if the quiz score is higher
        if self.quiz_score > level_total_score:
            total_score.level_scores[str(self.level_id)] = self.quiz_score
            total_score.save()

        # Calculate the new total score by summing the quiz scores for all levels
        total_score.total_score = sum(total_score.level_scores.values())
        total_score.save()


# Countdown Timer
class CountdownTimer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)