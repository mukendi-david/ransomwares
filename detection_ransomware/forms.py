from django import forms


class PCAPUploadForm(forms.Form):
    pcap_file = forms.FileField(label='Fichier PCAP')


class EmailFilterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(
        label='Mot de passe', widget=forms.PasswordInput)
