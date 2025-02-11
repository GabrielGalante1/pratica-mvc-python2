from database import Database

class Tarefa:
    def __init__(self, id, titulo, data_conclusao):
        self.id = None
        self.titulo = None
        self.data_conclusao = data_conclusao

    def salvarTarefa(self, tarefa):
        db = Database()
        db.conectar()
        sql = "INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s, %s)"
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    def listarTarefa():
        db = Database()
        db.conectar()
        sql = "SELECT id, titulo, data_conclusao FROM tarefa"
        result = db.consultar(sql, None)
        db.desconectar()
        return result if result else []
    
    def apagarTarefa(self):
        db = Database()
        db.conectar()
        sql = "DELETE FROM tarefa WHERE id = %s"
        params = (self.id)
        db.executar(sql, params)
        db.desconectar()

#coisamento
tarefa = Tarefa(1, 'Teste de tarefa', None)
tarefa.apagarTarefa()