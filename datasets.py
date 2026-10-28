import streamlit as st
import streamlit.components.v1 as components

TITULO_PESTANA = "Streamlit para expo de datasets"

# ------------------------------------------------------------------
#  AQUÍ SE COMPLETA LA INFORMACIÓN.
#  Cada compañero agrega su app dentro de "apps" del dataset que
#  corresponda:
#    autor : nombre del compañero
#    repo  : link del repositorio de GitHub (donde está su texto)
#    url   : link de la app ya publicada (opcional). Si se completa,
#            la app se muestra dentro de la celda.
# ------------------------------------------------------------------
FELINOS = {
    "nombre": "Felinos",
    "emoji": "🐾",
    "fuente": "GBIF (gbif.org)",
    "resumen": "Avistamientos de felinos silvestres en Argentina.",
    "que_es": (
        "Estas aplicaciones muestran información sobre los avistamientos de felinos "
        "silvestres en Argentina, a partir de una base de datos con **2019 registros "
        "de 9 especies distintas**, como el puma, el yaguareté y el ocelote. "
        "Podemos descubrir cuántas filas y columnas tiene la lista de datos, cuántas "
        "especies hay y en qué provincias se los vio más veces: Misiones es la primera "
        "y Santa Cruz la segunda."
    ),
    "secciones": [
        ("Conociendo nuestros datos", "Filas, columnas, nombres de las columnas y provincias que aparecen en los registros."),
        ("Graficamos", "Gráficos de colores para ver los mismos datos de distintas formas: barras por especie, torta con el porcentaje de cada especie, barras con las provincias con más avistamientos y, en otra versión, los meses del año en que se ven más felinos (líneas, barras y torta)."),
        ("Mostramos en mapas", "Un mapa de la Argentina que se puede mover y acercar. Se elige un felino (puma, yaguareté, etc.) y aparecen los lugares donde lo vieron, con el nombre del animal en cada marca."),
    ],
    "herramientas": ["Python", "Streamlit", "Pandas", "Plotly", "Folium"],
    "objetivo": "Que cualquier persona pueda explorar los datos de forma fácil y visual, y descubrir dónde y cuándo se ven los felinos de nuestro país.",
    "aviso": "",
    "apps": [
        {"autor": "Catalina Fernandez", "repo": "https://github.com/katalon4184-design/tp11-pps", "url": ""},
        {"autor": "Persigo Martín", "repo": "https://github.com/persigoWast12/app_pps", "url": ""},
    ],
}

AEROPUERTOS = {
    "nombre": "Aeropuertos",
    "emoji": "✈️",
    "fuente": "Dataset de aeropuertos de Argentina",
    "resumen": "Cuántos aeropuertos hay, de qué tipo y dónde están.",
    "que_es": (
        "La aplicación permite conocer mejor los aeropuertos de Argentina de una manera "
        "sencilla e interactiva, a partir de un conjunto de datos (dataset)."
    ),
    "secciones": [
        ("Conociendo el dataset", "Cantidad de filas, columnas y tipos de aeropuertos, junto con información general sobre los datos usados."),
        ("Gráficos", "Comparación de la cantidad de aeropuertos por provincia y por categoría."),
        ("Mapa interactivo", "Ubicación geográfica de los aeropuertos del país, con la posibilidad de elegir cuáles ver según su tamaño."),
    ],
    "herramientas": ["Python", "Streamlit", "Pandas", "Plotly", "Folium"],
    "objetivo": "Que cualquier persona, aunque no tenga conocimientos de informática o análisis de datos, pueda explorar la información, comprenderla fácilmente y descubrir datos interesantes sobre nuestro país.",
    "aviso": "",
    "apps": [
        {"autor": "Cristian Lescano", "repo": "https://github.com/Comediasr/PPs/blob/main/texto_expo_pps.odt", "url": ""},
    ],
}

CONECTIVIDAD = {
    "nombre": "Conectividad a Internet",
    "emoji": "🌐",
    "fuente": "Dataset de conectividad de Argentina",
    "resumen": "Qué tecnologías y conexiones de internet hay en el país.",
    "que_es": "Aquí vemos información sobre las redes de internet en la Argentina.",
    "secciones": [
        ("Tecnologías", "Qué tecnologías se usan, por ejemplo fibra óptica, satelital y ADSL."),
        ("Provincias", "Qué tipo de conexiones hay en cada provincia, por ejemplo Buenos Aires, Salta y Santa Fe."),
        ("Localidades", "Información por localidad, por ejemplo Villa Grisolia, Villa María y Mechita."),
    ],
    "herramientas": [],
    "objetivo": "",
    "aviso": "",
    "apps": [
        {"autor": "Santiago Saenz", "repo": "https://github.com/santiagosaenzmadero-ux/texto-de-presentacion/blob/main/Sin%20t%C3%ADtulo%201.odt", "url": ""},
    ],
}

AREAS_PROTEGIDAS = {
    "nombre": "Áreas protegidas",
    "emoji": "🌳",
    "fuente": "Dataset de áreas protegidas de Argentina",
    "resumen": "Distribución, tamaño, tipo y jurisdicción de las áreas protegidas.",
    "que_es": (
        "En esta página web se conocen datos sobre las áreas protegidas de Argentina: "
        "su distribución geográfica, tamaño, tipo y jurisdicción.\n\n"
        "**¿Qué es un área protegida?**"
        " Las áreas protegidas son espacios geográficos destinados a conservar la naturaleza, los ecosistemas, la biodiversidad y otros elementos de valor ambiental, científico o cultural.  "
        "legalmente regulado con el fin de preservar a largo plazo el patrimonio cultural "
        "o un ecosistema.  "
        "Se utilizaran fuentes como el Instituto Geográfico Nacional (IGN), el uso de estos datos facilita conocer dónde se encuentran las áreas protegidas, cómo se clasifican y qué organismos tienen jurisdicción sobre ellas."
    ),
    "secciones": [
        ("conocimientos básicos de nuestro dataset", "se repasan la información básica de nuestro dataset. Muestra columnas y filas, cuantas hay, que información almacenan y cuales áreas aparecen registradas."),
        ("Utilizamos gráficos para áreas protegidas:", "Aquí, se hacen distintos análisis de datos mediante la visualización de los diferentes gráficos que nos otorgan nuestras herramientas (potly). Permitiéndonos identificar y diferenciar porcentajes o cantidades."),
        ("Mostrar mapas de áreas protegidas:", "Se utilizan mapas visuales con los que podemos verificar los diferentes registros de nuestras áreas, marcar cada una de ellas y profundizar las funciones que nos brindan las herramientas según el análisis (folium)."),
    ],
    "herramientas": [],
    "objetivo": "",
    "aviso": "Hoy 16/10/2026 los datos utilizados pueden estar desactualizados y no necesariamente representan la situación actual.",
    "apps": [
        {"autor": "Arturo Moreno", "repo": "https://github.com/Bazx007/Texto-informativo-sobre-app-areas-protegidas", "url": ""},
        {"autor": "Alejandro Moreno", "repo": "https://github.com/AleJndroMoreno/STREAMLIT-/blob/main/documento%20Areas%20protegidas%20dataset%20Expo%20Alejandro%20moreno.docx", "url": ""},
        {"autor": "Rodriguez Alejo", "repo": "https://github.com/AlejoRodriguez57/pps-Armar-un-texto-para-expo-de-la-escuela/blob/main/txt", "url": ""},
    ],
}

TODOS = [FELINOS, AEROPUERTOS, CONECTIVIDAD, AREAS_PROTEGIDAS]

ESTILO = """
<style>
.tarjeta {background:#17402A; border:1px solid #2E8B57; border-radius:16px;
          padding:18px; height:100%; margin-bottom:12px;}
.tarjeta h3 {margin:0 0 6px 0;}
.chip {display:inline-block; background:#2E8B57; color:white; border-radius:12px;
       padding:2px 10px; margin:2px 4px 2px 0; font-size:0.85rem;}
</style>
"""


def configurar(emoji):
    st.set_page_config(page_title=TITULO_PESTANA, page_icon=emoji, layout="wide")
    st.markdown(ESTILO, unsafe_allow_html=True)


def mostrar_dataset(d):
    configurar(d["emoji"])
    st.title(f"{d['emoji']} {d['nombre']}")
    if d["fuente"]:
        st.caption(f"Fuente: {d['fuente']}")

    izq, der = st.columns([3, 2], gap="large")

    with izq:
        st.write(d["que_es"])
        if d["aviso"]:
            st.warning("⚠️ " + d["aviso"])

        st.subheader("Qué vas a encontrar")
        for i, (titulo, desc) in enumerate(d["secciones"], start=1):
            st.markdown(f"**{i}. {titulo}.** {desc}")

        if d["herramientas"]:
            st.subheader("Herramientas que usamos")
            st.markdown(
                "".join(f"<span class='chip'>{h}</span>" for h in d["herramientas"]),
                unsafe_allow_html=True,
            )
        if d["objetivo"]:
            st.subheader("Objetivo")
            st.info(d["objetivo"])

    with der:
        st.subheader("📱 Las aplicaciones")
        for app in d["apps"]:
            with st.container(border=True):
                st.markdown(f"**App de {app['autor']}**")
                if app["repo"]:
                    st.link_button("Ver repositorio y texto", app["repo"])
                else:
                    st.warning("Falta el link del repositorio.")
                if app["url"]:
                    components.iframe(app["url"], height=450, scrolling=True)
                else:
                    st.caption("La app publicada aparecerá acá cuando se agregue su link.")
