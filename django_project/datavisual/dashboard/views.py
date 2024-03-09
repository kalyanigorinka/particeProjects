# from django.shortcuts import render, redirect
# from .models import OfficeData
# from .forms import OfficeDataFrom

# # Create your views here.


# def index(request):
#     data =  OfficeData.objects.all()
#     if request.method == 'POST':
#         form =  OfficeDataFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form =  OfficeDataFrom()
#     context = {
#         'data': data,
#         'form': form,
#     }
#     return render(request, 'dashboard/index.html', context)

# views.py
from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
# from .views import index 

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            df = pd.read_csv(uploaded_file)

            # Process the DataFrame as needed, e.g., save to the database
            # ...

            return render(request, 'success_page.html', {'data': df.to_html()})
    else:
        form = UploadFileForm()

    return render(request, 'upload_file.html', {'form': form})



'''
from django.shortcuts import render, redirect
from .models import OfficeData  # Import the OfficeData model
from .forms import OfficeDataFrom
import pandas as pd

# dashboard/views.py
from .models import OfficeData  # Import the OfficeData model

def main(request):
    if request.method == 'POST':
        form = OfficeDataFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Create a new instance of the OfficeData model
            obj = OfficeData.objects.create(file=form.cleaned_data['file'],  # Assuming file is a FileField in OfficeData
                                            date=form.cleaned_data['date'],
                                            username=form.cleaned_data['username'],
                                            system_id=form.cleaned_data['system_id'],
                                            test_tab_ref=form.cleaned_data['test_tab_ref'],
                                            pos_angle=form.cleaned_data['pos_angle'],
                                            signal_cat=form.cleaned_data['signal_cat'],
                                            pw=form.cleaned_data['pw'],
                                            ampl=form.cleaned_data['ampl'],
                                            rms_error=form.cleaned_data['rms_error'],
                                            test_status=form.cleaned_data['test_status'],
                                            remarks=form.cleaned_data['remarks'],
                                            )

            # Rest of your code
    else:
        form = OfficeDataFrom()

    return render(request, 'dashboard/main.html', {'form': form})'''


''''
def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    print(df.values)
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        OfficeData.objects.create(
            date=l[0],
            username=l[1],
            system_id=float(l[2]),
            test_tab_ref=l[3],
            set_power=float(l[4]),
            pos_angle=float(l[5]),
            signal_cat=l[6],
            pw=float(l[7]),
            pri=float(l[8]),
            ampl=float(l[9]),
            rms_error=float(l[10]),
            test_status=l[11],
            remarks=l[12],
            # Add fields accordingly
        )

def main(request):
    if request.method == 'POST':
        form = OfficeDataFrom(request.POST, request.FILES)
        form = OfficeDataFrom() 
        file = request.FILES['file']
        obj = file.objects.create(file = file)
        create_db(obj.file)
        form = OfficeData(request.POST, request.FILES)
         
    return render(request, 'dashboard/main.html')  # Pass the 'form' variable to the template context
'''









