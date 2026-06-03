from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


router = DefaultRouter()

router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'alunos', views.AlunoViewSet)
router.register(r'professores', views.ProfessorViewSet)
router.register(r'coordenadores', views.CoordenadorViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'vagas', views.VagaViewSet)
router.register(r'candidaturas', views.CandidaturaViewSet)
router.register(r'estagios', views.EstagioViewSet)
router.register(r'documentos', views.DocumentoViewSet)
router.register(r'relatorios', views.RelatorioViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('empresa/dashboard/', views.empresa_dashboard, name='empresa_dashboard'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
