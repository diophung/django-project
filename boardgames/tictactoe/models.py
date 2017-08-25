from django.db import models
from django.db.models import Q

from django.contrib.auth.models import User
GAME_STATUS_CHOICES = (
    ('A', 'Active'),
    ('F', 'First Player Wins'),
    ('S', 'Second Player Wins'),
    ('D', 'Draw')
)


class GamesManager(models.Manager):
    def games_for_user(self, user):
        """
        Return a queryset of games that the user participate in
        :param user:
        :return:
        """
        return super(GamesManager, self).get_queryset().filter(
            Q(first_player_id=user.id) | Q(second_player_id=user.id))


class InvitationManager(models.Manager):
    def invitation_for_user(self, user):
        """
        Return a queryset of invitation that user received
        :param user:
        :return:
        """
        return super(InvitationManager, self).get_queryset().filter(Q(to_user_id=user.id))


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="game_first_player")
    second_player = models.ForeignKey(User, related_name="game_second_player")
    next_to_move = models.ForeignKey(User, related_name="games_to_move")
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='A', choices=GAME_STATUS_CHOICES)
    objects = GamesManager()

    def __str__(self):
        return "{0} vs. {1}".format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300)
    game = models.ForeignKey(Game)


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent")
    to_user = models.ForeignKey(User, related_name="invitation_received")
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = InvitationManager()
