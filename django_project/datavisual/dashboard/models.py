# from django.db import models

# # Create your models here.
# class StudentsData(models.Model):
#      username = models.CharField(max_length=100)
#      percentage = models.IntegerField()
      

# class Meta:
#         verbose_name_plural = 'username percentage Data'

# def __str__(self):
#         return f'{self.name}-{self.percentage}'

# dashboard/models.py

# from django.db import models

# class OfficeData(models.Model):
#     file = models.FileField(upload_to='files/')  # Add this line if you need a 'file' field
#     file = models.FileField(upload_to='office_data.csv')
# # class file(models.Model):
# #     file = models.FileField(upload_to="files")
# #     file = models.FileField(upload_to='your_upload_directory/')

#     date = models.DateTimeField()
#     username = models.CharField(max_length=255)
#     system_id = models.FloatField()
#     test_tab_ref = models.CharField(max_length=255)
#     set_power = models.FloatField()
#     pos_angle = models.FloatField()
#     signal_cat = models.CharField(max_length=255)
#     pw = models.FloatField()
#     pri = models.FloatField()
#     ampl = models.FloatField()
#     rms_error = models.FloatField()
#     test_status = models.CharField(max_length=255)
#     remarks = models.TextField()


# class Meta:
#           verbose_name_plural = 'username office Data'

# def __str__(self):
#         return f"{self.date} - {self.username}"

from django.db import models


class OfficeData(models.Model):
    file = models.FileField(upload_to='office_data/')  # Specify the upload directory for the 'file' field

    date = models.DateTimeField()
    username = models.CharField(max_length=255)
    system_id = models.FloatField()
    test_tab_ref = models.CharField(max_length=255)
    set_power = models.FloatField()
    pos_angle = models.FloatField()
    signal_cat = models.CharField(max_length=255)
    pw = models.FloatField()
    pri = models.FloatField()
    ampl = models.FloatField()
    rms_error = models.FloatField()
    test_status = models.CharField(max_length=255)
    remarks = models.TextField()

    class Meta:
        verbose_name_plural = 'Username Office Data'

    def __str__(self):
        return f'{self.username} - {self.date}'  # You can customize this representation as needed

