import streamlit as st
from PIL import Image

# Configurações da página
st.set_page_config(
    page_title="Adolfo Hugo Silva | Portfólio Profissional",
    page_icon="📋",
    layout="wide"
)

# Banner
banner = "https://i.imgur.com/FXzu6nE.jpg"  # Substituir pela imagem da capa personalizada

st.sidebar.image(banner,  width=250)  # Ajuste do tamanho da imagem
st.sidebar.header('Adolfo Hugo Silva')
    # Headline magnética
st.markdown("<h3 style='text-align: center; color: white;'>Contabilidade e Data-Driven • Eficiência Contábil • Automação com Python e Power BI e MySQL</h1>", unsafe_allow_html=True)

# Frase de posicionamento
st.markdown("---")
st.markdown("<h3 style='text-align: center; font-style: italic; color: white;'>\"Unindo tecnologia e finanças para gerar inteligência e precisão na tomada de decisões.\"</h3>", unsafe_allow_html=True)
st.markdown("---")

# Sobre mim
st.header("Sobre mim")
st.write("""
Sou Adolfo Hugo Silva, Bacharel contábil, apaixonado por dados, tecnologia e inovação. Minha missão é transformar a contabilidade tradicional por meio da inteligência de dados e automação de processos.

Atuo há mais de 5 anos na área contábil-financeira, conduzindo processos de fechamento, conciliações, apuração fiscal e análises financeiras. Mas foi ao integrar Python, Power BI e SQL que encontrei meu diferencial: transformar dados brutos em insights claros, reduzindo erros e otimizando a performance financeira das empresas.

Criei automações que aumentaram em até 60% a eficiência de processos operacionais e desenvolvi dashboards com Power BI para decisões estratégicas. Hoje, sou um contador do presente com visão de futuro: estratégia, dados e inovação.
""")

# Competências
st.header("Competências Técnicas")
st.markdown("""
- **Contabilidade e Finanças**: Fechamento contábil, DRE, CMV, SPED Contábil/ECF, IRPJ, conciliações.
- **Automação**: Python, automação web, otimização de processos.
- **Análise de Dados**: Power BI, Power Query, SQL, Pandas, Excel Avançado.
- **Softwares ERP**: Sankhya, Winthor, SIAGRI, Domínio Sistemas.
""")

# Projetos e Portfólio
st.header("📂 Projetos de Destaque")

st.markdown("**Chatbot Personalizado**")
with st.expander("Chatbot utilizando API DeepSeek e Streamlit"):
    st.write("Este projeto foi utilizado a API do DeepSeek para criar um chatbot personalizado, que pode ser utilizado para responder perguntas frequentes ou fornecer informações específicas. A interface foi desenvolvida com Streamlit, permitindo uma interação simples e intuitiva. O chatbot é capaz de entender e responder a perguntas em linguagem natural, tornando-o uma ferramenta útil para empresas que desejam melhorar o atendimento ao cliente.")
    st.write("A aplicação é simples e intuitiva, permitindo que os usuários façam perguntas e recebam respostas em tempo real. O chatbot pode ser treinado com dados específicos para fornecer informações relevantes e precisas.")
    st.markdown("https://hugochatbot.streamlit.app")
    st.video('https://youtu.be/bXvCGIe4i-M')

st.markdown('**Consulta CNPJ**')
with st.expander('CNPJ'):
    st.write('Este projeto consulta dados de CNPJ via API')
    st.markdown('https://consultascnpj.streamlit.app')

st.markdown("**Análise para Conciliação Automática: Domínio Sistemas**")
with st.expander("Automação de Conciliação Clientes/Fornecedores"):
    st.video("https://www.youtube.com/watch?v=BV9k3md9-QM")
    st.write("""
    Este projeto consiste em uma aplicação desenvolvida em Python para facilitar a conciliação de notas fiscais (NF) em processos financeiros. Com uma interface interativa no Streamlit, o sistema permite o upload de arquivos Excel, executa análises detalhadas dos lançamentos e exibe relatórios visuais que simplificam o monitoramento dos status de conciliação.

    ### Principais Funcionalidades
    - **Processamento de Dados**: Extração e identificação automática de NFs e devoluções a partir de descrições de lançamentos.
    - **Visualização de Resultados**: Geração de gráficos e tabelas detalhadas para análise de Tag status, como "Conciliado", "Valor a Pagar" ou "Falta NF".
    - **Download de Relatórios**: Possibilidade de baixar o relatório consolidado da conciliação em formato Excel.

    A análise contábil realizada tem o objetivo de identificar os pagamentos do mês e verificar se houve Nota Fiscal. Caso não haja o provisionamento e reconhecimento da NF, deve-se reclassificar diretamente para a conta de despesa de resultado.

    ### Tecnologias Utilizadas
    - **Linguagem**: Python
    - **Bibliotecas**: Streamlit, Pandas, Plotly
    - **Autenticação e Interface Gráfica**: Streamlit para criação de interface de login e exibição de resultados.
    - **Visualização de Dados**: Plotly Express para gráficos dinâmicos e interativos.

    Este projeto oferece uma solução robusta e prática para automatizar e simplificar o processo de conciliação de notas fiscais, sendo ideal para inclusão no portfólio pela sua aplicabilidade em cenários reais de contabilidade e finanças.

    [conciliador-nf.streamlit.app](https://conciliador-nf.streamlit.app)

    [GitHub](https://github.com/Adolfo-Hugo/streamlit_xml)
    """)
            

st.markdown("**Análise das Empresas de Maior Capital no Brasil**")

with st.expander("Power BI: Dashboard Financeiro"):
    st.components.v1.iframe(
    src="https://app.powerbi.com/view?r=eyJrIjoiNzg0MGI3YzYtMDRjYi00YzFjLTk2ZTQtZDkxYWExMjkwNWFiIiwidCI6ImUyMGE0YWNmLWY4MDgtNDI1Mi05YWUyLTEwMzEyOTFlZTUxNSJ9",
    width=1000,
    height=700,
    scrolling=True
)    
    st.write("Este estudo visa analisar as 100 empresas com maior capital social no Brasil, segmentando-as por regiões e atividades empresariais. O objetivo é entender quais segmentos empresariais de maior capital estão alocados nas diferentes regiões brasileiras, compreender o montante total desse capital social no país e como ele está distribuído. Base de dados extraída do site https://empresasbrasileiras.com.br ")


    st.markdown("**Automação Webscraping Diário Oficial AL**")
with st.expander("Automação Webscraping Diário Oficial AL"):
    st.video("https://www.youtube.com/watch?v=l8HsOcC35jc",
)
    st.write("""
Este projeto é um web scraper automatizado desenvolvido em Python para extrair informações do Diário Oficial do Estado de Alagoas. 
O script busca dados de clientes com base em códigos CACEAL e um intervalo de datas especificado pelo usuário, armazenando os resultados em arquivos Excel.
                
[GitHub]https://github.com/Adolfo-Hugo/webscraping_doeal
""")
    
st.markdown("**Validador de CPFs**")
with st.expander("Validador de CPFs"):
    st.write("Este projeto é um validador de CPF desenvolvido em Python, utilizando a biblioteca Streamlit para criar uma interface web interativa. O objetivo principal é permitir que os usuários verifiquem a validade de números de CPF informados.")
    st.markdown("https://validador-cpf.streamlit.app")
# Experiência profissional
st.header("Experiência Profissional")
with st.expander("Pretorian Contabilidade | Assistente de Contabilidade"):
    st.write("""
    - Automatização de processos contábeis com Python, reduzindo tempo de execução em até 60%.
    - Desenvolvimento de dashboards com Excel e Power BI para visualização de KPIs financeiros.
    - Análises de balanços patrimoniais, conciliações e apoio na gestão estratégica.
    """)
with st.expander("Coagro | Assistente Contábil"):
    st.write("""
    - Aplicação de BI no agronegócio: Power BI + SIAGRI para análise de estoques e folha de pagamento.
    - Implementação de rotinas eficientes de fechamento e conciliações.
    """)

with st.expander("Outras Experiências"):
    st.write("""
    - Autoforte Toyota, Paes & Andrade, Contato Contabilidade, Monte e Soares, JUCEAL.
    """)


# Formação acadêmica
st.header("🎓 Formação Acadêmica")
st.markdown("""
- **MBA em Análise de Dados e Big Data – PUC Minas** *(2024 – 2026)*
- **Bacharelado em Ciências Contábeis – SEUNE** *(2016 – 2019)*
""")

# Certificações
st.header("Certificações")
st.markdown("""
- Python Mundo 1, 2 e 3 - Cursos em Vídeo
- Formação Power BI e SQL Udemy
- Pandas - Udemy
""")

# Contato
st.sidebar.header("Contato:")
st.sidebar.markdown("""
- 📧 Email: adolfohugosilva@gmail.com  
- 📞 WhatsApp: (82) 99683-8463  
- 🔗 [LinkedIn](https://www.linkedin.com/in/adolfo-hugo-silva-a298751aa)  
- 📂 [GitHub](https://github.com/Adolfo-Hugo)
- 📄 [Baixar Currículo em PDF](https://drive.google.com/file/d/1Rodf_389YdafdWk6KtJKLjirmitxsa81/view?usp=sharing)

""")

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Adolfo Hugo Silva | Todos os direitos reservados</p>", unsafe_allow_html=True)
