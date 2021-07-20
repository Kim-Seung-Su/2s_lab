from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  #UserCreationForm상속, 받는 모든 인자들을 선택적으로 받고 슈퍼매서드로 부모클래스를 가져옴

        self.fields['username'].disabled = True