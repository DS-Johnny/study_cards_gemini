from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
API_KEY= os.getenv("GEMINI_API_KEY")

# Cria o Client do Gemini
client = genai.Client(api_key=API_KEY)

class Gerador:
    def __init__(self):
        self.model = "gemini-3.5-flash"
    
    def gerar_perguntas(self, tema: str) -> dict:
        prompt = {
            "role" : f"Você é um especialista no tema: {tema}.",
            "tone" : ["Educado", "Didático"],
            "context" : f"Alunos da universidade precisam de ajuda para estudar o tema: {tema} através de um aplicativo de perguntas e respostas.",
            "task" : f"Você deve gerar 10 perguntas e respostas didáticas para sobre o tema: {tema}.",
            "constraints" : ["O output deve ser uma json string com 10 pares {pergunta : resposta}", 
                            "Não retorne nenhum texto à mais, apenas a json string respeitando o formato explícito em output_format", 
                            "Todas as perguntas devem se parecer com uma pergunta de prova.",
                            "Cada chave da json string deve ser uma pergunta sobre o tema, e cada valor deve ser a resposta correspondente à pergunta",
                            "As chaves não devem ser: Pergunta_1, Pergunta_2 etc... elas devem ser perguntas reais"],
            "example" : "{'Ao que o tema se refere?' : 'O tema se refere à...', 'Onde aplicamos o conceito...? : 'O conceito é aplicado quando...' }",
            "output_format": """{"pergunta_1": "resposta_1", "pergunta_2":"resposta_2"}""",
        }
    
        try:
            resposta = client.models.generate_content(model="gemini-3.5-flash", contents=str(prompt))
            return resposta
        
        except Exception as e:
            print(e)
            return e