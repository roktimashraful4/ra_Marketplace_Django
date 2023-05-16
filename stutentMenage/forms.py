# //////////// Devoloped by Roktim  ashrafull \\\\\\\\

from django import forms
from django.forms import ImageField, ModelForm
from .models import AddTask, TaskCetagory
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# class WorkDetailsForm(forms.ModelForm):
    
    # class Meta:
    #     model = WorkDetails
    #     fields = ("title","body")
    #     labels ={
    #         'title': "Title",
    #         'body':"Enter full descriptions"
    #     }

    #     widgets = {
    #         'title':forms.TextInput(attrs={'class':'form-control',  'placeholder':"Enter Title here"}),
            
            
    #     }

class TaskCetagoryForm(forms.ModelForm):
    
    class Meta:
        model = TaskCetagory
        fields = ( 'title', 'slug', 'shortdis' , 'img')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',  'placeholder':"Enter Name "}),
            'slug':forms.TextInput(attrs={'class':'form-control',  'placeholder':"  (Optional) "}),
            'shortdis':forms.Textarea(attrs={'class':'form-control',  'placeholder':"Write somthing .. "}),
            'img': forms.FileInput(attrs={'class':'form-control'}),
            
            
        }
class AddTaskForm(forms.ModelForm):
    
    class Meta:
        model = AddTask
        fields ="__all__"
        widgets = {
            'cetid':forms.Select(attrs={'class':'form-control',  }),
            'title':forms.TextInput(attrs={'class':'form-control',  'placeholder':" Title "}),
            'slug':forms.TextInput(attrs={'class':'form-control',  'placeholder':"(Optional)"}),
            'shortdis':forms.Textarea(attrs={'class':'form-control',  'placeholder':"sort discriptions "}),
            'budget':forms.TextInput(attrs={'class':'form-control',  'placeholder':" Budget "}),
           
            'expdate':forms.DateInput(attrs={'class':'form-control', 'type':"date" }),
            'exptime':forms.TimeInput(attrs={'class':'form-control',  'type':"time" }),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            
            
            
        }

# //////////// Devoloped by Roktim  ashrafull \\\\\\\\
