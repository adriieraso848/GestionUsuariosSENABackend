from database import db

class Persona(db.Model):
    __tablename__='personas'
    
    idPersona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identificacion = db.Column(db.String(20), nullable=False, unique=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    foto = db.Column(db.String(250), nullable=True)
    
    
    usuarios = db.relationship('Usuarios', backref = 'persona', lazy=True)
    
    def to_dict(self):
        return{
            "idPersona": self.idPersona,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "correo": self.correo,
            "foto":self.foto,
        }