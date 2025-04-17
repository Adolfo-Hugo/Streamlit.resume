import streamlit as st
from PIL import Image

# Configurações da página
st.set_page_config(
    page_title="Adolfo Hugo Silva | Portfólio Profissional",
    page_icon="📊",
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
Sou Adolfo Hugo Silva, contador apaixonado por dados, tecnologia e inovação. Minha missão é transformar a contabilidade tradicional por meio da inteligência de dados e automação de processos.

Atuo há mais de 5 anos na área contábil-financeira, conduzindo processos de fechamento, conciliações, apuração fiscal e análises financeiras. Mas foi ao integrar Python, Power BI e SQL que encontrei meu diferencial: transformar dados brutos em insights claros, reduzindo erros e otimizando a performance financeira das empresas.

Criei automações que aumentaram em até 60% a eficiência de processos operacionais e desenvolvi dashboards com Power BI para decisões estratégicas. Hoje, sou um contador do presente com visão de futuro: estratégia, dados e inovação.
""")

# Competências
st.header("📌 Competências Técnicas")
st.markdown("""
- **Contabilidade e Finanças**: Fechamento contábil, DRE, CMV, SPED Contábil/ECF, IRPJ, conciliações.
- **Automação**: Python, automação web, otimização de processos.
- **Análise de Dados**: Power BI, Power Query, SQL, Pandas, Excel Avançado.
- **Softwares ERP**: Sankhya, Winthor, SIAGRI, Domínio Sistemas.
""")

# Projetos e Portfólio
st.header("📂 Projetos de Destaque")

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
EWeb Scraper de Diário Oficial
Este projeto é um web scraper automatizado desenvolvido em Python, utilizando Selenium para interação com páginas web e Pandas/Openpyxl para manipulação e armazenamento de dados em arquivos Excel.
Descrição
O script realiza a extração de informações de uma página específica do Diário Oficial do Estado de Alagoas. Ele busca informações relacionadas a clientes com base em um código CACEAL e um intervalo de datas especificado pelo usuário.
Funcionalidades
Busca automatizada: O script realiza buscas no site do Diário Oficial com base no código CACEAL de cada cliente.
Manipulação de dados: Os resultados das buscas são armazenados em uma lista e, posteriormente, salvos em arquivos Excel.
Relatórios detalhados: O script salva os resultados tanto utilizando Pandas quanto Openpyxl, gerando arquivos Excel com os dados extraídos.
Interface de linha de comando: Permite que o usuário insira o período de busca diretamente pela linha de comando.
Tecnologias Utilizadas
Python: Linguagem principal do projeto.
Selenium: Utilizado para automatizar a navegação e extração de informações da web.
Pandas: Utilizado para manipulação e salvamento de dados em arquivos Excel.
Openpyxl: Utilizado para manipulação de planilhas Excel.
Tqdm: Utilizado para exibir uma barra de progresso durante a execução do script.
Como Usar
Instale as dependências: Utilize pip para instalar as bibliotecas necessárias: pip install selenium pandas openpyxl tqdm webdriver_manager

Execute o script: Certifique-se de ter o arquivo clientes_caceal.xlsx no mesmo diretório que o script. Esse arquivo deve conter uma coluna chamada caceal e outra chamada Razao_social. Execute o script e insira o período inicial e final quando solicitado: python nome_do_script.py

Resultados: Os resultados serão salvos automaticamente em arquivos Excel, com o nome dados_encontrados_dd-mm-YYYY.xlsx, onde dd-mm-YYYY representa a data de execução do script.
Observações
Certifique-se de ter o Chrome instalado e atualizado, pois o webdriver_manager será utilizado para gerenciar o driver do Chrome automaticamente.
O script foi desenvolvido para ser executado em uma máquina local com Python instalado.
Adicionei a planilha clientes_caceal.xlsx onde é necessário alterar as informações de acordo com o modelo.
                
[GitHub]https://github.com/Adolfo-Hugo/webscraping_doeal
""")
    

# Experiência profissional
st.header("💼 Experiência Profissional")
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
st.header("📜 Certificações")
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
- 📂 [GitHub](https://github.com/adolfohugosilva)
""")

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Adolfo Hugo Silva | Todos os direitos reservados</p>", unsafe_allow_html=True)
