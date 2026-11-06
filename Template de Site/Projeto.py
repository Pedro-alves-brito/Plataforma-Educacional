import cherrypy
import os

local_dir = os.path.dirname(__file__)

class Principal():
    topo = open("html/cabecalho.html").read()
    rodape = open("html/rodape.html").read()
    @cherrypy.expose()
    def index(self):
        html = self.topo
        html = html + '''<br/>
        <p class="fonte">Aqui vai o conteúdo central da página inicial do projeto...</p>
        <p class="cor1 fonte">Home do Sistema Pet</p><br/>
        '''
        html = html + self.rodape

        return html

server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 81
}
cherrypy.config.update(server_config)

#Para que o cherrypy possa encontrar os arquivos dentro do diretório da aplicação
local_config = {
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":local_dir},
}

#objetos utilizados para rota de navegação
root = Principal() #rota principal
cherrypy.quickstart(root,config=local_config)
