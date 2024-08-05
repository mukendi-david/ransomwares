from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .utils import create_backup
from .models import BackupData
# from .forms import PCAPUploadForm, EmailFilterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import json


def index(request):
    return render(request, "ransomwares/index.html")


@login_required
def Capture_Traffic(request):
    with open("C:\\Users\\admin\\Documents\\Memoire_L2\\ransomwares\\detection_ransomware\\templates\\json\\traffic_data.json", 'r') as f:
        traffic_data = json.load(f)
    return render(request, 'ransomwares/capture_trafic.html', {'traffic_data': traffic_data})


@login_required
def Filter_Emails(request):
    with open("C:\\Users\\admin\\Documents\\Memoire_L2\\ransomwares\\detection_ransomware\\templates\\json\\email_data.json", 'r') as f:
        email_data = json.load(f)
    return render(request, 'ransomwares/filter_emails.html', {'email_data': email_data})


@login_required
def backup_data(request):
    backup_file = create_backup()
    BackupData.objects.create(
        user=request.user,
        file_path=backup_file
    )
    return render(request, "ransomwares/backup_data.html", {"backup_file": backup_file})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ransomwares:login')
    else:
        form = UserCreationForm()

    return render(request, 'auth/creation_auth.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ransomwares:home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('ransomwares:login')


# @login_required
# def capture_traffic(request):
#     packets = []
#     if request.method == "POST":
#         form = PCAPUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             pcap_file = form.cleaned_data["pcap_file"]
#             packets = parse_pcap(pcap_file.temporary_file_path())
#             for pkt in packets:
#                 TrafficCapture.objects.create(
#                     user=request.user,
#                     source_ip=pkt['source_ip'],
#                     destination_ip=pkt['destination_ip'],
#                     protocol=pkt['protocol'],
#                     length=pkt['length'],
#                     info=pkt['info']
#                 )
#             return redirect("ransomwares:capture_traffic")
#     else:
#         form = PCAPUploadForm()
#     return render(request, "ransomwares/capture_traffic.html", {"form": form, "packets": packets})


# @login_required
# def filter_emails(request):
#     if request.method == "POST":
#         form = EmailFilterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             emails = fetch_emails(username, password)
#             for email in emails:
#                 EmailFilter.objects.create(
#                     user=request.user,
#                     sender=email['sender'],
#                     subject=email['subject'],
#                     content=email['content']
#                 )
#             return redirect("ransomwares:filter_emails")
#     else:
#         form = EmailFilterForm()
#     return render(request, "ransomwares/filter_emails.html", {"form": form, "emails": emails})
