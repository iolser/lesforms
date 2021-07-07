from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='get_user_name') 
def get_user_name(id):
    try:
        user = User.objects.get(id=id)
        nome = user.first_name+" "+user.last_name
        return nome  
    except :
        return "Esta notificação foi gerada automáticamente"


@register.filter(name='get_email') 
def get_email(id):
    try:
        user = User.objects.get(id=id)
        email = user.email
        return email  
    except :
        return ""


@register.filter(name='get_user_type') 
def get_user_type(id):
    try:
        user = User.objects.get(id=id)

        if user.groups.filter(name="Proponent").exists():
            result = "Proponent"  
        elif user.groups.filter(name="Participant").exists():
            result =  "Participant"   
        elif user.groups.filter(name="Administrator").exists():
            result =  "Administrator"
        else: 
            result = ""
        return result
    except :
        return 0             
