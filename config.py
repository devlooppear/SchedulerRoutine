DATABASE = 'mensagensrotina'
PORTA = '5432'
SENHA = '<sua senha aqui>'

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "efdhaqerhaertunterterdgv"
SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{SENHA}@localhost:{PORTA}/{DATABASE}"
