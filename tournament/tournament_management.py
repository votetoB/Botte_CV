from models import Tournament, Registration, Match
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# TODO: Free slots, add normal description
def start_tournament(tournament_id):
    """
    Starts a tournament
    :param tournament_id: Id of a tournament to start
    :return: True if success, False otherwise
    """

    try:
        the_tournament = Tournament.objects.get(id=tournament_id)
        t_users = [x.user for x in Registration.objects.filter(tournament=the_tournament)]

    except ObjectDoesNotExist:
        return False

    if len(t_users) < the_tournament.max_participants:
        ## Add free slots
        pass

    for i in range(the_tournament.max_participants - 1):
        m = Match()
        m.tournament = the_tournament
        m.code = i

        if i < the_tournament.max_participants / 2:
            m.left_user = t_users[i * 2]
            m.right_user = t_users[i * 2 + 1]
        m.save()

    # Let the game begin!
    the_tournament.has_started = True
    the_tournament.save()

    for reg in Registration.objects.filter(tournament=the_tournament):
        reg.delete()

    return True


# TODO: prises for winner
def end_tournament(tournament_id):
    """
    Ends a tournament
    :param tournament_id: Id of a tournament to end
    :return: None
    """
    the_tournament = Tournament.objects.get(id=tournament_id)

    ## Give prises to the winner.
    ## winner = Match.objects.filter(tournament=the_tournament, code=the_tournament.max_participants - 2)[0].winner

    the_tournament.has_ended = True
    the_tournament.save()


def register_user(user_id, tournament_id):
    """
    Registers a user into a tournament
    :param user_id: Id of a user
    :param tournament_id: Id of a tournament
    :return: True if user is registered and false otherwise
    """

    the_tournament = Tournament.objects.get(id=tournament_id)
    if the_tournament.current_participants < the_tournament.max_participants:
        the_user = User.objects.get(id=user_id)

        reg = Registration()
        reg.user = the_user
        reg.tournament = the_tournament
        reg.save()

        return True
    else:
        return False


def cancel_user_registration(user_id, tournament_id):
    """
    Cancel user registration in a tournament
    :param user_id: Id of a user
    :param tournament_id: Id of a tournament
    :return: True if user is unregistered successfully and false otherwise
    """
    if check_user_registration(user_id, tournament_id):
        Registration.objects.get(user__id=user_id, tournament__id=tournament_id).delete()
        return True
    else:
        return False


def check_user_registration(user_id, tournament_id):
    """
    Checks if user is registered in a tournament
    :param user_id: Id of a user
    :param tournament_id: Id of a tournament
    :return: True if user is registered and false otherwise
    """

    the_array = Registration.objects.filter(user__id=user_id, tournament__id=tournament_id)
    if the_array:
        assert len(the_array) == 1, "SOMETHING WENT WRONG: Two registration for same user in the same tournament!"
        return True
    else:
        return False


def report_result(match_id, winner_id):
    """
    Sets up a winner of a match
    :param match_id: Id of a match
    :param winner_id: Id of the winner
    :return: False, if wrong parameters and true otherwise
    """
    try:
        match = Match.objects.get(id=match_id)
        winner = User.objects.get(id=winner_id)
    except ObjectDoesNotExist:
        return False

    match.winner = winner
    match.save()

    if match.code == match.tournament.max_participants - 2:  # Last match
        end_tournament(match.tournament.id)
        return True

    next_match_code = match.tournament.max_participants + (match.code // 2)
    next_match = Match.obejct.get(tournament=match.tournament, code=next_match_code)

    if match.code % 2:
        next_match.right_user = winner
    else:
        next_match.left_user = winner

    next_match.save()
    return True
