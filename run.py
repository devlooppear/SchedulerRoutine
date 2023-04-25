from app import app
from threading import Thread
from config import *
from app.routes import *

if __name__ == '__main__':
    app.debug = True
    agendar_tarefas()
    scheduler_thread = Thread(target=iniciar_scheduler)
    scheduler_thread.start()
    app.run()