from django.urls import path

from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.teste, name='teste'),
    path('print', views.print_em_html, name='print'),

    path('listar_curso', views.listarCursos, name='listarCurso'),
    path('listar_professor', views.listarProfessores, name='listarProfessor'),
    path('listar_alunos', views.listarAlunos, name='listarAluno'),

    path('incluir_professor', views.incluirProfessor, name='incluirProfessor'),
    path('incluir_curso', views.incluirCurso, name='incluirCurso'),
    path('incluir_aluno', views.incluirAluno, name='incluirAluno'),
    path('editar_curso/<int:id>', views.editarCurso, name='editarCurso'),
    path('excluir_curso/<int:id>', views.excluirCurso, name='excluirCurso'),
    path('editar_professor/<int:id>', views.editarProfessor, name='editarProfessor'),
    path('excluir_professor/<int:id>', views.excluirProfessor, name='excluirProfessor'),
    path('editar_aluno/<int:id>', views.editarAluno, name='editarAluno'),
    path('excluir_aluno/<int:id>', views.excluirAluno, name='excluirAluno'),
    path('listar_turma', views.listarTurmas, name='listarTurmas'),
    path('inclur_turma', views.incluirTurma, name='incluirTurma'),
    path('editar_turma/<int:id>', views.editarTurma, name='editarTurma'),
    path('excluir_turma/<int:id>', views.excluirTurma, name='excluirTurma')
]