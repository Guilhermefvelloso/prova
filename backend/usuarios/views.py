from django.http import JsonResponse, Http404
from .models import Usuario


# 6 - listar usuários
def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    data = [
        {
            "id": u.id,
            "nome": u.nome,
            "email": u.email,
            "ativo": u.ativo,
        }
        for u in usuarios
    ]

    return JsonResponse(data, safe=False)


# 7 - buscar usuário por ID
def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
    except Usuario.DoesNotExist:
        raise Http404("Usuário não encontrado")

    data = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "ativo": usuario.ativo,
    }

    return JsonResponse(data)