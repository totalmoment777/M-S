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