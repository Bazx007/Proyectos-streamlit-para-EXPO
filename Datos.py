import streamlit as st

from datasets import configurar


# Configuración y estilo general de la aplicación
configurar("🗺️")


# Encabezado
st.title("🗺️ Argentina a través de los datos v.2")
st.subheader("EEST N°9 La Plata")
st.write("7°to 2°da Grupo B")
st.caption("""
                   Arturo Moreno
                 """)
st.caption("versiones anteriores: ")
st.caption("""
                 V.1 - Juan cruz salgado https://github.com/juancruzsalado88-wq/stremlit_zzz
                 """)




st.caption(
    "Una exposición de proyectos realizados con Streamlit"
)

st.write(
    "Explorá distintos aspectos de nuestro país a través de "
    "datos, gráficos y mapas interactivos. Cada proyecto aborda "
    "un tema diferente y presenta información de manera sencilla."
)
st.write(
    "En esta página reunimos los trabajos de todos. Usá el menú de la izquierda para elegir un dataset: cada página explica de qué trata y muestra, en su propia celda, las aplicaciones que hizo cada compañero."
)

st.divider()

st.subheader("Elegí un tema para explorar")

st.write(
    "Seleccioná **Ver información del proyecto** para conocer "
    "qué propone cada aplicación y acceder a los enlaces "
    "cuando estén disponibles."
)


# Información que se mostrará en las tarjetas
proyectos = [
    {
        "titulo": "Avistamientos de felinos",
        "emoji": "🐾",
        "descripcion": (
            "Descubrí dónde se registraron felinos silvestres "
            "en Argentina y explorá las especies presentes "
            "en los datos."
        ),
        "destacados": "Especies · Provincias · Mapas",
        "pagina": "pages/1_Felinos.py",
    },
    {
        "titulo": "Aeropuertos",
        "emoji": "✈️",
        "descripcion": (
            "Conocé la ubicación y las características de los "
            "aeropuertos argentinos a través de datos y gráficos."
        ),
        "destacados": "Ubicación · Categorías · Provincias",
        "pagina": "pages/2_Aeropuertos.py",
    },
    {
        "titulo": "Conectividad a Internet",
        "emoji": "🌐",
        "descripcion": (
            "Explorá las tecnologías de conexión disponibles "
            "en distintas provincias y localidades del país."
        ),
        "destacados": "Tecnologías · Provincias · Localidades",
        "pagina": "pages/3_Conectividad.py",
    },
    {
        "titulo": "Áreas protegidas",
        "emoji": "🌳",
        "descripcion": (
            "Conocé la distribución, los tipos y las superficies "
            "de las áreas protegidas de Argentina."
        ),
        "destacados": "Conservación · Superficies · Ubicación",
        "pagina": "pages/4_Areas_protegidas.py",
    },
]


# Muestra dos tarjetas por fila
for inicio in range(0, len(proyectos), 2):
    columnas = st.columns(2)

    for columna, proyecto in zip(
        columnas,
        proyectos[inicio:inicio + 2],
    ):
        with columna:
            with st.container(border=True):
                st.subheader(
                    f"{proyecto['emoji']} {proyecto['titulo']}"
                )

                st.write(proyecto["descripcion"])

                st.caption(proyecto["destacados"])

                st.page_link(
                    proyecto["pagina"],
                    label="Ver información del proyecto",
                )


st.divider()

st.caption(
    "Proyecto colectivo · Exploración de datos de Argentina"
)