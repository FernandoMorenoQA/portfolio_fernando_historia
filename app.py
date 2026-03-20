import streamlit as st

# Configurações iniciais
st.set_page_config(page_title="Fernando Moreno | Uma Trajetória de Superação", layout="centered")

# Estilo Visual Sóbrio e Profissional
st.markdown("""
    <style>
    .jornada-container {
        background-color: #f8fafc;
        padding: 30px;
        border-radius: 20px;
        border-left: 10px solid #0077B5;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    h1 { color: #01467e; font-weight: bold; }
    h2 { color: #01467e; margin-top: 20px; }
    h3 { color: #01467e; margin-top: 15px; margin-bottom: 10px;}
    .stMarkdown { font-size: 1.15rem; line-height: 1.8; color: #1f2937; }
    
    .link-simples {
        color: #0077B5 !important;
        font-weight: bold;
        text-decoration: none;
        font-size: 1.1rem;
    }
    .link-simples:hover {
        text-decoration: underline !important;
    }

    .badge {
        background-color: #0077B5;
        color: white;
        padding: 5px 15px;
        border-radius: 15px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    try:
        # Certifique-se de que sua foto está na pasta com este nome:
        st.image("foto_fernando.png", width=250)
    except:
        st.error("📷 Foto não encontrada. Verifique o nome 'foto_fernando.png' na pasta.")

with col2:
    st.title("Fernando Celso S. M de Souza")
    st.subheader("Especialista em QA | 18 Anos de TI")
    
    st.markdown("""
    <span class="badge">Mestre em TI</span>
    <span class="badge">MBA</span>
    <span class="badge">Sistemas de Informação</span>            
    <span class="badge">ISTQB</span>
    """, unsafe_allow_html=True)
    
    st.markdown('<br><a href="https://www.linkedin.com/in/fernandocelsomoreno/" target="_blank" class="link-simples">LinkedIn</a>', unsafe_allow_html=True)

st.divider()

# --- A NARRATIVA DE SUPERAÇÃO ---
st.header("Minha Jornada de Superação")

st.markdown("""
<div class="jornada-container">
    Minha história com o silêncio começou cedo. Aos <b>10 anos de idade</b>, recebi o diagnóstico de deficiência auditiva. 
    Naquela época, eu não sabia que o som que me faltava seria substituído por uma visão de mundo muito mais profunda e focada.
    <br><br>
    Aos <b>25 anos</b>, decidi ingressar na faculdade de Tecnologia da Informação. O desafio era imenso: as aulas eram 
    ambientes complexos, onde entender o que os professores diziam exigia um <b>esforço físico para compreender a leitura labial</b>. 
    Muitas vezes a dificuldade de compreensão parecia um muro, mas eu nunca aceitei o "não consigo" como resposta.
    <br><br>
    Com uma persistência que moldou meu caráter, <b>me formei</b>. Mas eu queria mais. Sabia que a educação era minha maior 
    ferramenta de inclusão. Após alguns anos de mercado, especializei-me com uma <b>Pós-graduação</b> e, por último, 
    alcancei o título de <b>Mestre em Direção Estratégica em TI</b>.
    <br><br>
    Hoje, olho para trás e vejo que cada aula não compreendida me ensinou a ler nas entrelinhas, a focar no detalhe 
    e a desenvolver uma resiliência que aplico diariamente nos meus 18 anos de carreira em Quality Assurance.
</div>
""", unsafe_allow_html=True)

st.divider()

# --- PILARES PROFISSIONAIS ---
st.header("Expertise Profissional")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### O Diferencial do Silêncio")
    st.write("""
    - **Foco Analítico:** Concentração absoluta no detalhe visual e lógico.
    - **Resiliência de Entrega:** Problemas complexos resolvidos com a calma de quem superou grandes barreiras.
    """)

    st.markdown("### Visão Estratégica")
    st.write("""
    - Gestão da Qualidade de Software.
    - Metodologias Ágeis (Scrum, Kanban).
    """)

with col_b:
    st.markdown("### Expertise Técnica")
    st.write("""
    - Automação com **Cypress, Selenium e Robot Framework**.
    - Testes de Performance com **JMeter**.
    - Testes de API (Insomnia, Postman).
    """)

    st.markdown("### Inovação e Inteligência Artificial")
    st.write("""
    - **Agentes de IA:** Implementação de fluxos autônomos para automação inteligente.
    - **Orquestradores:** Coordenação de múltiplos agentes e modelos de linguagem (LLMs).
    """)

st.divider()

# Mensagem Final (Limpa, sem ícones)
st.info("Minha trajetória prova que o conhecimento não conhece limitações sensoriais, apenas a força da determinação.")

# Rodapé
st.markdown("<center>Fernando Moreno | Qualidade, Persistência e Resiliência</center>", unsafe_allow_html=True)