import streamlit as st

# =====================================================
# CONFIGURAÇÃO
# =====================================================

st.set_page_config(
    page_title="Calculadora Check HPLC",
    page_icon="🧪",
    layout="centered"
)

# =====================================================
# LOGO
# =====================================================

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
# ESTILO
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
}

/* RESULTADO */

.resultado {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    color: #4B286D;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* CAMPOS */

.stTextInput div[data-baseweb="input"] {
    border: 2px solid #B08AD6 !important;
    border-radius: 8px !important;
    background-color: white !important;
}

/* TEXTO DOS CAMPOS */

.stTextInput input {
    color: #4B286D !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

/* TÍTULOS */

h1, h2, h3 {
    color: #4B286D !important;
    font-weight: 800 !important;
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
    '<div class="subtitulo">Desenvolvimento Analítico (Guilherme Hayne)</div>',
    unsafe_allow_html=True
)

# =====================================================
# FUNÇÃO CONVERSÃO
# =====================================================

def converter(valor):
    try:
        return float(valor.replace(",", "."))
    except:
        return None

# =====================================================
# ÁREA DO PADRÃO
# =====================================================

st.subheader("Área do Padrão")

st.markdown("**P1**")

c1, c2, c3, c4, c5 = st.columns(5)

ap1 = c1.text_input("", key="padrao1", label_visibility="collapsed")
ap2 = c2.text_input("", key="padrao2", label_visibility="collapsed")
ap3 = c3.text_input("", key="padrao3", label_visibility="collapsed")
ap4 = c4.text_input("", key="padrao4", label_visibility="collapsed")
ap5 = c5.text_input("", key="padrao5", label_visibility="collapsed")

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

    st.markdown(
        f"""
        <div style="
            text-align:center;
            color:#4B286D;
            font-size:22px;
            font-weight:900;">
            Média Área do Padrão
            <br>
            {media_padrao:.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# CHECK
# =====================================================

st.divider()

st.subheader("Área do Check")

c1, c2 = st.columns(2)

ac1 = c1.text_input("Check 1", key="check1")
ac2 = c2.text_input("Check 2", key="check2")

valores_check = [
    converter(ac1),
    converter(ac2)
]

media_check = None

if all(v is not None for v in valores_check):

    media_check = sum(valores_check) / 2

    st.markdown(
        f"""
        <div style="
            text-align:center;
            color:#4B286D;
            font-size:22px;
            font-weight:900;">
            Média Área do Check
            <br>
            {media_check:.2f}
        </div>
        """,
        unsafe_allow_html=True
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
# RESULTADO
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
        <div class="resultado">
            {resultado:.0f}%
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

    for campo in campos:

        if campo in st.session_state:
            del st.session_state[campo]

    st.rerun()
