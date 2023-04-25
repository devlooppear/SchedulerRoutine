from app import db
import schedule

class Rotina(db.Model):
    __tablename__ = "rotina"
    
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(10), nullable=False)

    def __init__(self, mensagem, horario):
        self.mensagem = mensagem
        self.horario = horario
        schedule.every().day.at(horario).do(self.imprimir_mensagem)

    def imprimir_mensagem(self):
        print(self.mensagem)
        schedule.run_pending()
