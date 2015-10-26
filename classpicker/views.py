from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.core.signing import BadSignature
from django.core.exceptions import PermissionDenied
from django.core import signing
from classpicker.models import Pick, PickUser, HearthstoneClass
from classpicker.forms import PickStartForm, PickForm
import ast
from django.http import JsonResponse


def start(request):
    if request.method == 'POST':
        # no_bans = bool(request.POST.get('no_bans'))
        # picks_first = bool(request.POST.get('picks_first'))
        first_user = PickUser()
        second_user = PickUser()
        first_user.battle_tag = request.POST.get('battle_tag')
        second_user.battle_tag = request.POST.get('opponent_battle_tag')
        first_user.save()
        second_user.save()
        new_pick = Pick(first_user=first_user, second_user=second_user)
        # new_pick.no_bans = no_bans
        # new_pick.picks_first = picks_first
        # if no_bans:
        #     new_pick.picks_first = True
        #     new_pick.first_bans_finished = True
        #     new_pick.second_bans_finished = True

        new_pick.save()

        # Create urlsafe sha1 signed base64 string
        data_container = dict()  # Contains info about database object and user role
        data_container['pk'] = new_pick.pk
        data_container['role'] = 'first'

        first_link = signing.dumps(data_container)

        return redirect(reverse('classpicker:main', kwargs={'code': first_link}))

    pick_start_form = PickStartForm
    return render(request, 'classpicker/start.html', {'pick_start_form': pick_start_form})


def main(request, code):
    try:
        value = signing.loads(code)
    except BadSignature:
        return Http404
    if 'pk' not in value.keys() or 'role' not in value.keys():
            return Http404

    the_pick = get_object_or_404(Pick, id=value['pk'])

    if request.method == 'GET':
        second_link = ''
        if value['role'] == 'first':
            new_value = value.copy()
            new_value['role'] = 'second'
            second_link = request.get_host() + reverse('classpicker:main',
                                                       kwargs={'code': signing.dumps(new_value)})

        # if the_pick.picks_first:
        #     form = PickForm
        # else:
        #     form = BanForm
        form = PickForm

        return render(request, 'classpicker/main.html', {'pick': the_pick, 'role': value['role'],
                                                         'second_link': second_link, 'form': form})
    elif request.is_ajax():

        if request.POST.get('ping') == 'false':
            pick_result = ast.literal_eval(request.POST.get('result'))

            if value['role'] == 'first':
                the_user = the_pick.first_user
            else:
                the_user = the_pick.second_user
            if not the_user.finished:
                print 'here'
                for pick in pick_result:
                    the_user.choices.add(get_object_or_404(HearthstoneClass, title=pick.title()))
                    the_user.finished = True
                    the_user.save()

                response_data = dict()
                response_data['redirect'] = the_pick.first_user.finished and the_pick.second_user.finished
                return JsonResponse(response_data)

            else:
                raise PermissionDenied

        else:
            response_data = dict()
            response_data['redirect'] = the_pick.first_user.finished and the_pick.second_user.finished
            return JsonResponse(response_data)

    else:
        raise PermissionDenied


def result(request, code):
    try:
        value = signing.loads(code)
    except BadSignature:
        return Http404
    if 'pk' not in value.keys() or 'role' not in value.keys():
            return Http404

    the_pick = get_object_or_404(Pick, id=value['pk'])

    if not (the_pick.first_user.finished and the_pick.second_user.finished):
        raise PermissionDenied
    else:
        return render(request, 'classpicker/result.html', {'pick': the_pick})