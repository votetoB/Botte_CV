from django.db import models
from django.contrib.auth.models import User


# TODO: check-in's
class Tournament(models.Model):
    title = models.CharField(max_length=200, unique=True)
    start_time = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    current_participants = models.PositiveIntegerField(default=0)
    comment = models.TextField(max_length=1000, blank=True, null=True)
    has_started = models.BooleanField(default=False)  # True ONLY after start_tournament() ends its work
    has_ended = models.BooleanField(default=False)    # True ONLY after end_tournament() ends its work

    def __str__(self):
        return self.title


class Registration(models.Model):
    tournament = models.ForeignKey('Tournament')
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("tournament", "user")


class Match(models.Model):
    tournament = models.ForeignKey('Tournament')
    left_user = models.ForeignKey(User, null=True, blank=True, related_name='left_user')
    right_user = models.ForeignKey(User, null=True, blank=True, related_name='right_user')
    code = models.PositiveIntegerField()  # code: 0 for the first match
                                          # tournament__max_participants - 2 for the last one
                                          # (code // 2 + tournament__max_participants) is the code for the next match
    winner = models.ForeignKey(User, null=True, blank=True, related_name='winner')

    def __str__(self):
        return 'Match #' + str(self.code) + ' of ' + self.tournament.__str__()

