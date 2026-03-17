# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'Ticket Classification GenAI'
copyright = '2026, Alexandre Bezerra de Lima'
author = 'Alexandre Bezerra de Lima'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon', # Se você usa padrão Google/NumPy
    'sphinx.ext.viewcode', # Opcional: mostra o código fonte no site
    'rst2pdf.pdfbuilder',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

pdf_documents = [('index', 'TicketClassificationDoc', 'Documentação do Projeto: Ticket Classification GenAI', 'Alexandre Bezerra de Lima')]

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # Tamanho do papel e da fonte base
    'papersize': 'a4paper',
    'pointsize': '11pt',

    # Adiciona pacotes LaTeX para customização de cores e fontes
    'preamble': r'''
        \usepackage{titlesec}
        \usepackage{xcolor}
        
        % Define uma cor personalizada (ex: azul-petróleo)
        \definecolor{MyTeal}{HTML}{008080}
        
        % Altera a cor de todos os títulos (H1, H2, H3...)
        \titleformat{\chapter}[display]
          {\normalfont\huge\bfseries\color{MyTeal}}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
        \titleformat{\section}
          {\normalfont\large\bfseries\color{MyTeal}}{\thesection}{1em}{}
        \titleformat{\subsection}
          {\normalfont\normalsize\bfseries\color{MyTeal}}{\thesubsection}{1em}{}

        % Altera a fonte padrão para uma mais moderna (ex: Helvetica/Arial-like)
        \renewcommand{\familydefault}{\sfdefault}
    ''',
    
    # Customiza a página de rosto (capa)
    'maketitle': r'''
        \begin{titlepage}
            \vspace*{4cm}
            \flushright
            {\Huge\bfseries\color{MyTeal} Ticket Classification GenAI} \\
            \vspace{1cm}
            {\large\bfseries Documentação Técnica do Projeto} \\
            \vspace{2cm}
            {\Large Alexandre Bezerra de Lima} \\
            \vfill
            {\large \copyright\ 2026 \ - Gerado em \today}
        \end{titlepage}
    ''',
}

# Garanta que o nome do arquivo e autores estejam corretos
latex_documents = [
    ('index', 'TicketClassificationDoc.tex', 'Ticket Classification GenAI Documentation',
     'Alexandre Bezerra de Lima', 'manual'),
]
