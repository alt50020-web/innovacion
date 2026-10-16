# Especificaciones Técnicas y de Diseño: Tutor de Programación Adaptativo con IA

Este documento detalla la arquitectura, metodología y funcionalidades de la plataforma **Tutor de Programación Adaptativo con IA**, un sistema diseñado bajo un modelo híbrido que equilibra el rigor pedagógico (método socrático) con la capacidad de co-crear programas complejos y completos.

---

## 🌟 1. Propuesta de Valor y Factor Innovador

A diferencia de las herramientas de asistencia tradicionales (como ChatGPT o GitHub Copilot) que entregan soluciones directas de código —fomentando la dependencia y destruyendo el proceso cognitivo del aprendizaje—, esta plataforma actúa como un **mentor pedagógico**.

* **Ocultación Estratégica de Soluciones:** El sistema retiene el código corregido. En su lugar, analiza los errores sintácticos y lógicos para guiar al usuario mediante preguntas orientadoras.
* **Personalización Basada en Frustración:** Modifica de manera dinámica el tipo de asistencia según el "historial de frustración" y desempeño del estudiante en tiempo real.
* **Modelo Híbrido Avanzado:** Permite pasar fluidamente de resolver retos puntuales de lógica a la arquitectura y co-creación guiada de aplicaciones de software completas.

---

## 📋 2. Arquitectura del Sistema y Módulos Core

El ecosistema de la plataforma se compone de cuatro pilares técnicos fundamentales interconectados:

```
┌────────────────────────────────────────────────────────┐
│               Interfaz de Usuario (IDE Web)            │
│       (Monaco Editor + Workspace Multi-archivo)        │
└───────────────┬────────────────────────┬───────────────┘
                │                        │
                ▼                        ▼
┌────────────────────────┐      ┌────────────────────────┐
│   Módulo de Sandbox    │      │    Motor Adaptativo    │
│  (Evaluación / Tests)  │      │      (El Cerebro)      │
└────────────────────────┘      └────────┬───────────────┘
                                         │
                                         ▼
                                ┌────────────────────────┐
                                │Orquestador de Pistas/IA│
                                │   (LLM + Contexto)     │
                                └────────────────────────┘
```

### A. Interfaz de Usuario (IDE Web con Workspace Multi-archivo)
* **Qué hace:** Proporciona un entorno de desarrollo integrado (IDE) directamente en el navegador, capaz de gestionar múltiples archivos de forma simultánea a través de un árbol de directorios lateral.
* **Tecnología recomendada:** *Monaco Editor* (el motor que impulsa Visual Studio Code) o *CodeMirror*, complementado con componentes de gestión de árboles de archivos virtuales en React o Vue.js.

### B. Módulo de Evaluación de Código (Sandbox Seguro)
* **Qué hace:** Recibe el código escrito por el estudiante y lo ejecuta de manera completamente aislada para validar si cumple con las especificaciones técnicas y las pruebas unitarias (*unit tests*).
* **Tecnología recomendada:** *Judge0*, *Piston API*, o microservicios basados en contenedores efímeros de *Docker* con restricciones estrictas de red, memoria y tiempo de ejecución.

### C. Motor Adaptativo (El Cerebro Analítico)
* **Qué hace:** Monitorea y recopila variables métricas cuantitativas del comportamiento del alumno: tiempo empleado, frecuencia de compilación, patrones de errores sintácticos reincidentes y nivel de experiencia del perfil. Clasifica instantáneamente el estado del alumno en tres niveles: *Fluido*, *Estancado Ligero* o *Frustrado Crítico*.
* **Tecnología recomendada:** Algoritmos de Machine Learning tradicionales para clasificación (como Árboles de Decisión o KNN) implementados en Python mediante *Scikit-Learn*.

### D. Orquestador de Pistas y Contexto (IA Generativa)
* **Qué hace:** Administra los prompts dirigidos al Modelo de Lenguaje (LLM). Utiliza el estado psicopedagógico del estudiante y el mapa de archivos del proyecto actual para generar respuestas guiadas sin entregar código explícito, a menos que el flujo de co-creación lo requiera.
* **Tecnología recomendada:** *OpenAI API (GPT-4o-mini / GPT-4o)*, *Anthropic Claude*, o modelos de despliegue local para privacidad total (*Llama 3* o *Gemma* gestionados vía *Ollama*).

---

## 🛠️ 3. El Sistema de Doble Modo (UI Dual)

La plataforma cuenta con dos pestañas de interacción principales que cambian las reglas de comportamiento del tutor:

| Característica | Modo Reto (Pedagogía Pura) | Modo Proyecto (Co-creación Completa) |
| :--- | :--- | :--- |
| **Objetivo** | Resolver acertijos algorítmicos y afianzar sintaxis. | Construir aplicaciones de software funcionales desde cero. |
| **Nivel de Ayuda** | Preguntas conceptuales y de lógica (Método Socrático). | Entrega de arquitectura, diagramas y código estructurado básico (*boilerplate*). |
| **Estructura** | Archivo único de código expuesto al alumno. | Árbol de archivos completo (*Workspace Multi-archivo*). |
| **Evaluación** | Pruebas unitarias predefinidas por el sistema. | Pruebas unitarias autogeneradas por la IA para verificar la lógica del alumno. |

---

## 🚀 4. Metodología de Co-Creación de Programas Completos

Cuando el usuario activa el **Modo Proyecto**, el Tutor de IA se transforma en un **Arquitecto de Software y Programador en Pareja (*Pair Programmer*)**. El proceso se divide en un flujo guiado de tres fases:

1. **Fase de Diseño y Arquitectura (Prompt a Diagrama):** El alumno redacta la idea general del software en lenguaje natural. La IA procesa la solicitud y modela la arquitectura técnica del sistema mediante un diagrama visual interactivo (ej. diagramas de clases o flujos de datos estructurados con *Mermaid.js* o *D3.js*).
2. **Fase de Modularización (Roadmap Dinámico):** La IA fragmenta el proyecto completo en subtareas atómicas e independientes y genera una lista de verificación (*Checklist*) interactiva en la interfaz. (Ej. *Paso 1: Configurar variables de entorno y base de datos; Paso 2: Crear el modelo de usuarios*).
3. **Fase de Co-programación Asistida:** A medida que el alumno selecciona una tarea del roadmap, la IA habilita tres niveles de ayuda bajo demanda:
   * **Nivel 1 (Conceptual):** Explicación teórica de cómo abordar la tarea y qué librerías son las idóneas.
   * **Nivel 2 (Plantillas / Boilerplate):** Generación del esqueleto del archivo o función (declaración de funciones, importaciones necesarias y firmas), dejando el cuerpo algorítmico vacío para que el estudiante programe la lógica central.
   * **Nivel 3 (Código Complejo con Auditoría):** Si el estudiante solicita la codificación de un algoritmo abstracto o complejo, la IA lo genera pero adjunta de manera obligatoria explicaciones paso a paso en forma de comentarios exhaustivos sobre las decisiones de diseño arquitectónico tomadas.

---

## 🎯 5. Características Avanzadas (Factores "Wow")

Para maximizar el impacto ante jurados o usuarios avanzados, la plataforma implementa las siguientes tecnologías adicionales:

* **Visualizador Dinámico de Flujo de Datos:** Muestra de forma gráfica y animada cómo cambian los estados de las variables en memoria línea por línea durante la ejecución de un código fallido, permitiendo al estudiante "ver" su error conceptual.
* **Modo "Explicación Inversa":** Invierte los roles de enseñanza. La plataforma presenta un bloque de código avanzado y el alumno debe redactar una explicación textual de su funcionamiento. El LLM evalúa la comprensión semántica profunda del alumno más allá de la sintaxis.
* **Módulo de TDD Automatizado (Test-Driven Development):** La IA escribe de manera autónoma las pruebas unitarias para las funciones que el estudiante va diseñando en su proyecto completo. El alumno aprende a programar guiado por pruebas de software del estándar de la industria.
* **Dashboard Analítico para Profesores:** Un panel integral con mapas de calor de competencia que le indica a los educadores qué conceptos específicos de ciencias de la computación (ej. recursividad, gestión de memoria, programación orientada a objetos) presentan la mayor tasa de estancamiento en el grupo de alumnos.

---

## 🧰 6. Stack Tecnológico General Sugerido

* **Capa de Presentación (Frontend):** *React.js*, *Next.js* o *Vue.js*, asegurando una interfaz Single Page Application (SPA) responsiva y reactiva de alta velocidad.
* **Capa de Lógica (Backend):** *Python* sustentado sobre *FastAPI* o *Django*, ideal por su ecosistema nativo de Machine Learning, su compatibilidad con librerías de IA y velocidad en el manejo de peticiones asíncronas.
* **Capa de Persistencia (Base de Datos):** *PostgreSQL* para la gestión estructurada de los perfiles de usuario, analíticas y roadmaps, y una base de datos vectorial ligera o almacenamiento de sesiones en *Redis* para mantener el contexto extendido del código multi-archivo en el LLM.
