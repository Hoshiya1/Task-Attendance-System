from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(label='任务标题', max_length=100)
    secret_lv = forms.ChoiceField(label='保密等级', choices=(('1', '仅限本部门查看'), ('2', '所有人可查看')), initial='1')
    detail = forms.CharField(label='具体内容', strip=False, widget=forms.Textarea)
    completed = forms.BooleanField(label='是否完成')
    