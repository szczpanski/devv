import streamlit as st
import random
import time

# Definir estilos personalizados
st.markdown(
    """
    <style>
    
    .stApp {
        background-color: #FEDC01; /* Cor de fundo amarelo */
    }

    /* .css-1n76uvr {
        background-color: #FEDC01; /* Cor do prompt de entrada amarelo */
        color: black; /* Cor da letra do prompt de entrada */
    } */

    h2 {
        font-size: 2.0em; /* Tamanho do título h2 */
        color: #FEDC01;
    }

    h4 {
        font-size: 1.0em; /* Tamanho do título h4 */
        color: #FEDC01;
    }

    /* .appview-container{
        background-color: #002168; / *azul */
    } */

    .title-container {
        display: flex;
        align-items: center;
    }

    header{
        display: none !important;
    }

    textarea:focus{

        border-color: green;
        /* background-color: #002168;
        color: white; */
    }

    .st-emotion-cache-uhkwx6{
        background-color: #002168;    
    }

    </style>
    """,
    unsafe_allow_html=True
)

#st.title("PoC BBTS Connect - 2024")
st.markdown(
    """
    <div class="title-container">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9TJi1vv-1pI4YduLmOW3J7Kt8LwfJzCB5kw&s" width="65%" height="65%">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h2>PoC Connect - 2024</h2>", unsafe_allow_html=True)

# Emulador de resposta transmitida
def response_generator():
    response = random.choice(
        [
            "Olá, como posso ajudar hoje com informações sobre os Normativos da BBTS?",
            "Oi, humano! Posso te ajudar em alguma coisa em relação à BBTS?",
            "Olá, como a BBTS pode te ajudar?",
            "Oi, posso te ajudar em alguma coisa relacionado às Normas Internas?",
            "Você precisa de ajuda com Normativos Internos?",
            "Olá, como posso ajudar hoje de acordo com as Normas Internas da BBTS?",
            "Oi, humano! Posso te ajudar em alguma coisa relacionada aos Normativos Internos da BBTS?",
            "Olá, como a BBTS pode te ajudar seguindo as Normas Internas??",
            "Oi, humano! Posso te ajudar em alguma coisaa conforme os Normativos Internos da BBTS?",
            "Você precisa de ajuda com algo que envolva as Normas Internas da BBTS?",
            "Como posso assisti-lo hoje, conforme os Normativos Internos da BBTS?",
            "Olá, posso ajudar em algo de acordo com as Normas Internas da BBTS??",
            "Precisa de ajuda com alguma coisa referente aos Normativos Internos da BBTS?",
            "Oi, como posso te auxiliar hoje de acordo com as Normas Internas da BBTS?",
            "Oi, humano! Há algo que eu possa fazer seguindo os Normativos Internos da BBTS?",
            "Olá, como a BBTS pode te ajudar com base nas Normas Internas?",
            "Precisa de suporte relacionado aos Normativos Internos da BBTS?",
            "Como posso te ajudar hoje, seguindo as Normas Internas da BBTS?",
            "Oi, humano! Posso te ajudar com alguma coisa conforme os Normativos Internos da BBTS?",
            "Olá, como a BBTS pode assisti-lo respeitando as Normas Internas?",
            "Oi, humano! Há algo que eu possa fazer de acordo com os Normativos Internos da BBTS?",
            "Você precisa de ajuda com alguma questão das Normas Internas da BBTS?",
            "Como posso assisti-lo hoje com base nos Normativos Internos da BBTS?",
            "Olá, posso ajudar em algo relacionado às Normas Internas da BBTS?",
            "Precisa de assistência com os Normativos Internos da BBTS?",
            "Oi, como posso ajudar hoje, conforme as Normas Internas da BBTS?",
            "Oi, humano! Posso te ajudar com alguma coisaa conforme os Normativos Internos da BBTS?",
            "Você precisa de ajuda com alguma coisa que envolva as Normas Internas da BBTS?",
            "Como posso assisti-lo hoje, de acordo com os Normativos Internos da BBTS?",
            "Olá, posso ajudar com algo baseado nas Normas Internas da BBTS?",
            "Precisa de ajuda com os Normativos Internos da BBTS?",
            "Oi, como posso te auxiliar hoje seguindo as Normas Internas da BBTS?",
            "Oi, humano! Há algo que eu possa fazer com base nos Normativos Internos da BBTS?",
            "Olá, como a BBTS pode te ajudar hoje conforme as Normas Internas?",
            "Precisa de suporte relacionado às Normas Internas da BBTS?"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.15)

# st.title("Chat simples")
st.markdown("<h3>Chatbot para Normativos Internos.</h3>", unsafe_allow_html=True)

# Inicializar histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens de chat do histórico ao recarregar o app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceitar entrada do usuário
if prompt := st.chat_input("Em que posso ajudar?"):
    # Adicionar mensagem do usuário ao histórico de chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Exibir mensagem do usuário no contêiner de mensagens de chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Exibir resposta do assistente no contêiner de mensagens de chat
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Adicionar resposta do assistente ao histórico de chat
    st.session_state.messages.append({"role": "assistant", "content": response})