from django.contrib import admin

from cadastro.models import Curso, Turma, Professor, Aluno

# Register your models here.
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Professor)