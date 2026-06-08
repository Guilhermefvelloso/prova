from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()

    data = []

    for t in tarefas:
        data.append({
            "id": t.id,
            "titulo": t.titulo,
            "descricao": t.descricao,
            "concluida": t.concluida,
            "usuario_responsavel": t.usuario_responsavel.nome if t.usuario_responsavel else None
        })

    return JsonResponse(data, safe=False)