# 📚 DocuTutor: Tu Tutor IA a partir de Documentos Físicos

[![Estado del Backend](https://github.com/<TU_USUARIO>/docututor/actions/workflows/ci-backend.yml/badge.svg)](https://github.com/<TU_USUARIO>/docututor/actions/workflows/ci-backend.yml)
[![Estado del Frontend](https://github.com/<TU_USUARIO>/docututor/actions/workflows/ci-frontend.yml/badge.svg)](https://github.com/<TU_USUARIO>/docututor/actions/workflows/ci-frontend.yml)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Transforma tus apuntes, guías y fotocopias en material de estudio interactivo. **DocuTutor** usa OCR e Inteligencia Artificial para extraer el texto de tus documentos escaneados y generar resúmenes, quizzes y explicaciones al instante.

## 🎯 ¿Qué Problema Resuelve?

Los estudiantes a menudo trabajan con material físico (libros, fotocopias, apuntes) que no puede ser aprovechado por herramientas digitales. DocuTutor cierra esa brecha, permitiendo digitalizar y potenciar ese conocimiento de forma gratuita y accesible.

## ✨ Funcionalidades Principales

*   **🔍 OCR Preciso:** Sube una foto o PDF escaneado y extrae todo el texto.
*   **✍️ Resúmenes Automáticos:** Obtén las ideas clave del documento en segundos.
*   **🧠 Quizzes Interactivos:** Genera preguntas de opción múltiple para autoevaluar tu conocimiento.
*   **👨‍🏫 Modo Tutor IA:** Pide explicaciones más profundas sobre cualquier concepto del texto.
*   **🌍 Open Source y Gratuito:** Construido con tecnologías de código abierto, sin costos de API.

## 🛠️ Stack Tecnológico

| Componente      | Tecnología                                                              |
| --------------- | ----------------------------------------------------------------------- |
| **Backend**     | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) |
| **Frontend**    | ![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black) ![Vite](https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=white) |
| **OCR**         | `pytesseract` (Wrapper de Tesseract)                                    |
| **IA**          | `transformers` de Hugging Face (Modelos T5, GPT-2)                      |
| **Base de Datos** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) (para desarrollo) |
| **CI/CD**       | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white) |

## 📁 Estructura del Proyecto
/
├── backend/ # Lógica del servidor (FastAPI)
├── frontend/ # Interfaz de usuario (React)
├── docs/ # Documentación (Diagramas, Visión del Proyecto)
└── .github/ # Workflows de CI/CD

## 🚀 Empezando

> **Nota:** Las instrucciones detalladas de instalación estarán disponibles pronto.

1.  **Clona el repositorio:**
    ```sh
    git clone https://github.com/<TU_USUARIO>/docututor.git
    cd docututor
    ```
2.  **Configura el backend:**
    ```sh
    cd backend
    # Sigue las instrucciones de su README interno
    ```
3.  **Configura el frontend:**
    ```sh
    cd frontend
    # Sigue las instrucciones de su README interno
    ```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, lee la guía de contribución (próximamente) y sigue nuestro código de conducta.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
