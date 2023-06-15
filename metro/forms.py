from django import forms
from . models import Member


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Member
        #fields=["user_name","review_text","rating"]# if  we want  some  fields only we can use exclude also if we want to exclude
        fields = '__all__'
        exclude=["card","topup"]
        labels = {"firstname": "First Name",
                  "lastname": "Last Name",
                  
                  "topup":"Card Value",
                  "phonenumber":"Adhar Number"}
        error_messages = {
            "firstname": {"required": "Your name must not be empty!",
                          "max_length": "Please enter a shorter name!"
                          }
        }
