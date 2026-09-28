import streamlit as st

# =====================================================
# CONFIGURAÇÃO
# =====================================================

st.set_page_config(
    page_title="Calculadora Check HPLC",
    page_icon="🧪",
    layout="centered"
)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image(
        "logo_merck.jpg",
        width=350
    )
# =====================================================
# SESSION STATE
# =====================================================

campos = [
    "padrao1",
    "padrao2",
    "padrao3",
    "padrao4",
    "padrao5",
    "check1",
    "check2",
    "massa_padrao",
    "massa_check"
]

for campo in campos:
    if campo not in st.session_state:
        st.session_state[campo] = ""

# =====================================================
# ESTILO MERCK
# =====================================================

st.markdown("""
<style>

.titulo {
    background: #702082;
    color: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

.subtitulo {
    text-align: center;
    color: #4B286D;
    font-size: 16px;
    margin-bottom: 10px;
}

.card {
    border: 1px solid #E0E0E0;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 10px;
    background-color: white;
}

.resultado {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# CABEÇALHO
# =====================================================

st.markdown(
    '<div class="titulo">CALCULADORA CHECK HPLC</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Desenvolvimento Análitico(Guilherme Hayne) </div>',
    unsafe_allow_html=True
)

st.write("")

# =====================================================
# CONVERSÃO
# =====================================================

def converter(valor):
    try:
        return float(valor.replace(",", "."))
    except:
        return None

# =====================================================
# ÁREA DO PADRÃO
# =====================================================

with st.container():

    st.subheader("Área do Padrão")

    st.markdown("**P1**")

    c1, c2, c3, c4, c5 = st.columns(5)

    ap1 = c1.text_input(
        "",
        key="padrao1",
        label_visibility="collapsed"
    )

    ap2 = c2.text_input(
        "",
        key="padrao2",
        label_visibility="collapsed"
    )

    ap3 = c3.text_input(
        "",
        key="padrao3",
        label_visibility="collapsed"
    )

    ap4 = c4.text_input(
        "",
        key="padrao4",
        label_visibility="collapsed"
    )

    ap5 = c5.text_input(
        "",
        key="padrao5",
        label_visibility="collapsed"
    )

# =====================================================
# MÉDIA PADRÃO
# =====================================================

valores_padrao = [
    converter(ap1),
    converter(ap2),
    converter(ap3),
    converter(ap4),
    converter(ap5)
]

media_padrao = None

if all(v is not None for v in valores_padrao):

    media_padrao = sum(valores_padrao) / 5

    st.metric(
        "Média Área do Padrão",
        f"{media_padrao:.2f}"
    )

# =====================================================
# CHECK
# =====================================================

st.divider()

st.subheader("Área do Check")

c1, c2 = st.columns(2)

ac1 = c1.text_input(
    "Check 1",
    key="check1"
)

ac2 = c2.text_input(
    "Check 2",
    key="check2"
)

valores_check = [
    converter(ac1),
    converter(ac2)
]

media_check = None

if all(v is not None for v in valores_check):

    media_check = sum(valores_check) / 2

    st.metric(
        "Média Área do Check",
        f"{media_check:.2f}"
    )

# =====================================================
# MASSAS
# =====================================================

st.divider()

st.subheader("Massas")

massa_padrao = st.text_input(
    "Massa do Padrão",
    key="massa_padrao"
)

massa_check = st.text_input(
    "Massa do Check",
    key="massa_check"
)

massa_p = converter(massa_padrao)
massa_c = converter(massa_check)

# =====================================================
# RESULTADO AUTOMÁTICO
# =====================================================

if (
    media_padrao is not None
    and media_check is not None
    and massa_p is not None
    and massa_c is not None
    and massa_c != 0
):

    resultado = (
        (media_check / media_padrao)
        * (massa_p / massa_c)
    ) * 100

    st.divider()

    st.markdown(
        f"""
        <div class='resultado'>
        {resultado:.2f}%
        </div>
        """,
        unsafe_allow_html=True
    )

    if 98 <= resultado <= 102:

        st.success("✅ CONFORME")

    else:

        st.error("❌ FORA DE ESPECIFICAÇÃO")

# =====================================================
# LIMPAR
# =====================================================

if st.button("🗑️ Limpar Campos"):

    for campo in [
        "padrao1",
        "padrao2",
        "padrao3",
        "padrao4",
        "padrao5",
        "check1",
        "check2",
        "massa_padrao",
        "massa_check"
    ]:

        if campo in st.session_state:
            del st.session_state[campo]

    st.rerun()