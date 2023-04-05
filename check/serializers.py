from rest_framework import serializers

from check.models import emp_tbl

class emp_tbl_ser(serializers.ModelSerializer):
    class Meta:
        model=emp_tbl
        fields='__all__'