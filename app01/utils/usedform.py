"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 2022/3/17
 * @Environment: Anaconda3
"""
from django import forms
from captcha.fields import CaptchaField


class Login(forms.Form):
    user = forms.CharField(
        label='用户名',  # 在表单里表现为 label 标签
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control'})  # 添加 css 属性
    )

    pwd = forms.CharField(
        label='密码',  # 在表单里表现为 label 标签
        max_length=64,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # 添加 css 属性
    )

    captcha = CaptchaField(
        label='验证码',
        required=True,
        error_messages={'required': '验证码不能为空'},
    )
