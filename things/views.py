from django.shortcuts import render
from .forms import ThingForm  # Import ThingForm

def home(request):
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = ThingForm(request.POST)
        if form.is_valid():
            # Save the valid form data to create a new Thing
            form.save()
            # You can also perform additional actions here
    else:
        # If it's a GET request, just display the empty form
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
