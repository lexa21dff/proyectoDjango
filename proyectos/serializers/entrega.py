from rest_framework import serializers
from proyectos.models import Entrega

class EntregaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrega
        fields = ['id','calificacion' ,'descripcion_entrega','respuesta_instructor','instructor','proyecto','tipo_revision','aprendiz','creado', 'editado']
