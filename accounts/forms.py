from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'username'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'password'}
        )
    )


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'username'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'password'}
        )
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'confirm password'}
        )
    )

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm:
            if password != password_confirm:
                msg = "The two password fields must match."
                self.add_error('password_confirm', msg)
        return cleaned_data