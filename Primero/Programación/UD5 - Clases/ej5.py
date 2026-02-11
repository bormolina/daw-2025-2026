from dataclasses import dataclass

@dataclass
class Alumno:
    id_alumno: int
    nombre: str
    email: str

@dataclass
class Asignatura:
    id_asignatura: int
    nombre: str
    horas_semanales: float

@dataclass
class Matricula:
    id_alumno: int
    id_asignatura: int