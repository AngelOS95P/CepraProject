from django.urls import path, include 
from . import views
from dashboard.views import EstChartView, PeluChartView, EstuTableView, EvalTableView, PelTableView, EstuChartView, SesiTableView
urlpatterns = [
    #path('',views.dashboard),
    path('',EstChartView.as_view(),name='dashboard'),
    path('estudiantes/',EstuTableView.as_view(), name='estudiantes'),
    path('evaluaciones/',EvalTableView.as_view(), name='eval'),
    path('sesiones/',SesiTableView.as_view(), name='ses'),
    path('peluche/',PelTableView.as_view(), name='pel'),
    path('charts/',views.graficas, name='charts'),
    path('chartsEst/<nombre>',EstuChartView.as_view(), name='graEst'),
    path('chartsPel/<nombre>',PeluChartView.as_view(), name='graPelu'),
    
]