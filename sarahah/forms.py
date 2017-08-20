from django import forms


class MessageForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'w3-card-4',
                                                        'placeholder':'পরিচয় গোপন করে আমাকে যেকোনো কথা যদি বলতে চান এখানে বলতে পারেন।',
                                                        }), required=True)