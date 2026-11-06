import cherrypy

class PaginaEquipe():
    topo = open("html/cabecalho.html").read()
    rodape = open("html/rodape.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += '''<h2 class="fonte">Membros da Equipe... Dados do projeto de vcs!!</h2>'''
        html += self.rodape

        return html