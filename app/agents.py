from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from app.scraping import buscar_info_basica, buscar_deep_search
from app.image_analysis import analisar_imagens

def run_agents(nome, telefone):
    info_basica = buscar_info_basica(nome, telefone)
    deep_search = buscar_deep_search(nome)
    imagens = buscar_imagens(nome)
    analise_imagens = analisar_imagens(imagens)

    resultado = {
        "nome": info_basica.get("nome_completo"),
        "telefone": telefone,
        "cpf": info_basica.get("cpf"),
        "localizacao": info_basica.get("localizacao"),
        "profissao": info_basica.get("profissao"),
        "redes_sociais": deep_search.get("redes_sociais"),
        "interesses": deep_search.get("interesses"),
        "noticias": deep_search.get("noticias"),
        "imagens": imagens,
        "analise_imagens": analise_imagens
    }

    return resultado