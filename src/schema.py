"""Arquivo de Schema de  funcionarios"""

from pydantic import BaseModel, EmailStr, PositiveInt
from datetime import datetime


class ContratoFuncionarios(BaseModel):
    """Casse responsavel pelo contrato de dados de Funcionarios"""

    id: PositiveInt
    nome: str
    idade: PositiveInt
    datanascimento: datetime
    email: EmailStr
    cargo: str
    departamento: str
