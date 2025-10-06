from django.shortcuts import render

# Create your views here.
def SequencerView(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        pass
def SequencesListView(request):
    if request.method == 'GET':
        return render(request, 'sequences.html')
    if request.method == 'POST':
        pass
def ProfileView(request, id):
    if request.method == 'GET':
        return render(request, 'profile.html', {'id': id})
    if request.method == 'POST':
        pass
def LoginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        pass
def RegisterView(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        pass
def SequencerWithIDView(request, id):
    if request.method == 'GET':
        return render(request, 'info.html', {'id': id})
    if request.method == 'POST':
        pass    