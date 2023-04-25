from datetime import datetime
from flask import render_template, request, url_for,  redirect
import schedule
from app.models import Rotina
from time import sleep
from app import app, db

HORARIO = '18:52'

def iniciar_scheduler():
    agendar_tarefas()
    while True:
        schedule.run_pending()
        sleep(1)

def carregar_mensagens(app):
    with app.app_context():
        mensagens = {r.horario: r.mensagem for r in Rotina.query.all()}
        return mensagens

def imprimir_mensagem(mensagem):
    return lambda: print(mensagem)

def agendar_tarefas():
    mensagens = carregar_mensagens(app)
    for horario, mensagem in mensagens.items():
        schedule.every().day.at(horario).do(imprimir_mensagem(mensagem))

@app.route('/')
def index():
    agora = datetime.now().strftime('%H:%M')
    mensagens = carregar_mensagens(app)
    mensagem = mensagens.get(agora, 'Ainda não deu o horário')
    return render_template('index.html', mensagem=mensagem)

@app.route('/configurar-tarefa', methods=['POST'])
def configurar_tarefa():
    horario = request.form['horario']
    mensagem = request.form['mensagem']
    rotina = Rotina(mensagem, horario)
    db.session.add(rotina)
    db.session.commit()
    schedule.clear()
    agendar_tarefas()
    return redirect(url_for('index'))
