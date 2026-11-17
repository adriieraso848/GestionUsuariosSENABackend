from database import db

class Usuario(db.Model):
    __tablename__='usuarios'
    
    idUsuario = db.Column(db.Interger, primary_key=True, autoincrement=True)
    idPersona = db.Column(db.Interger, db.ForeignKey('personas.idPersona'), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.Enum('Aprendiz', 'Instructor', name='tipo_enum'), nullable=False)
    estado = db.Column(db.Enum('Activo', 'Inactivo', name='estado_enum'), nullable=False, default='Activo')
    
    
    def to_dict(self):
        return{
            "idUsuario": self.idUsuario,
            "idPersona": self.idPersona,
            "username": self.username,
            "password": self.password,
            "estado": self.estado,
            "tipo": self.tipo,
            "persona": self.foto.to_dict() if self.persona else None
        }
    
    