import requests
import os
from serpapi import GoogleSearch

def buscar_info_basica(nome, telefone):
    params = {
        "engine": "google", 
        "q": '{}'.format(nome),  
        "api_key": os.getenv("SERPAPI_API_KEY")
    }

    search = GoogleSearchResults(params)
    results = search.get_dict()

    info = {
        "nome_completo": nome,
        "cpf": "Não encontrado",  # alterar posteriormente
        "profissao": "Não encontrado",  # alterar posteriormente
        "localizacao": "Não encontrado",  # alterar posteriormente
    }

    return info

def buscar_deep_search(nome):
    """Simula uma busca aprofundada na internet por menções ao nome do cliente"""
    url = f"https://some-news-api.com/search?q={nome}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"noticias": [], "redes_sociais": {}, "interesses": []}

    soup = BeautifulSoup(response.text, 'html.parser')
    noticias = [noticia.text for noticia in soup.find_all("h2")]

    return {
        "noticias": noticias,
        "redes_sociais": {
            "linkedin": f"https://linkedin.com/in/{nome.replace(' ', '').lower()}",
            "instagram": f"https://instagram.com/{nome.replace(' ', '').lower()}",
            "facebook": f"https://facebook.com/{nome.replace(' ', '').lower()}"
        },
        "interesses": ["tecnologia", "esportes"]
    }