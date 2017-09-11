from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Invitation
from .forms import InvitationForm


@login_required
def new_invitation(request):
    if request.method == 'POST':
        form = InvitationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_home")
    else:  # GET
        form = InvitationForm()
    return render(request, "tictactoe/new_invitation.html", {'form': form})


@login_required
def view_invitation(request):
    invites = Invitation.objects.invitation_for_user(request.user)
    return render(request, "tictactoe/view_invitation.html", {'invites': invites})
