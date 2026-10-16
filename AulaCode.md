# AulaCode
## Plataforma inteligente, multilenguaje y adaptable para la enseñanza de programación en el aula

**Concurso objetivo:** INNOVATECNM  
**Tipo de proyecto:** Desarrollo de software educativo  
**Modalidad propuesta:** Plataforma web con funcionamiento en línea y en red local  
**Público objetivo:** Estudiantes y docentes de programación, especialmente de nivel medio superior y superior.

> **Estado del documento:** Propuesta inicial. Los supuestos sobre el problema, la innovación, los objetivos y las metas deberán validarse mediante investigación con usuarios y pruebas del prototipo. Los requisitos de participación deberán confirmarse con la convocatoria oficial vigente.

---

## 1. Descripción general

AulaCode es una propuesta de plataforma educativa diseñada para facilitar la enseñanza y el aprendizaje de programación dentro de clases reales. Busca integrar en un mismo entorno digital las herramientas que necesitan los docentes para impartir clases y las que requieren los estudiantes para practicar, ejecutar código, recibir retroalimentación y desarrollar habilidades de programación.

La plataforma pretende complementar las metodologías educativas actuales y, posteriormente, ofrecer un entorno integral para impartir y evaluar clases de programación.

A diferencia de una plataforma dedicada únicamente a ofrecer cursos o ejercicios, AulaCode propone incorporar diagnóstico del aprendizaje, seguimiento grupal, evaluación automática y funcionamiento con conectividad limitada.

El proyecto se desarrollará con un enfoque de innovación educativa, accesibilidad tecnológica y validación en un entorno académico real.

## 2. Planteamiento del problema

La enseñanza de programación presenta desafíos, especialmente para quienes comienzan a desarrollar habilidades de pensamiento lógico y resolución de problemas.

Entre las posibles dificultades se encuentran:

- Interpretar errores de código y comprender cómo corregirlos.
- Comprender conceptos fundamentales de programación.
- Recibir retroalimentación oportuna.
- Permitir que el docente identifique las necesidades individuales de un grupo durante una clase.
- Coordinar herramientas para explicar conceptos, escribir código, evaluar ejercicios y registrar avances.
- Utilizar plataformas educativas en aulas con conexión a internet inestable o inexistente.

Estas situaciones son **hipótesis de trabajo que deben comprobarse** mediante entrevistas, encuestas y observaciones en grupos reales. No deben presentarse como resultados de investigación hasta contar con evidencia.

### Pregunta de investigación

¿Una plataforma educativa que integre ejecución de código, retroalimentación formativa, diagnóstico grupal y funcionamiento sin conexión a internet puede mejorar el aprendizaje de los fundamentos de programación y facilitar el trabajo docente?

## 3. Objetivo general

Desarrollar una plataforma educativa multilenguaje que facilite la enseñanza y el aprendizaje de programación en clases reales mediante herramientas de práctica interactiva, evaluación automática, diagnóstico de errores y seguimiento del progreso académico, con capacidad de funcionamiento tanto en línea como en una red local sin acceso a internet.

## 4. Objetivos específicos

1. Diseñar una interfaz que permita a docentes y estudiantes interactuar en un entorno educativo común.
2. Implementar herramientas para crear clases, administrar grupos y asignar actividades de programación.
3. Integrar un editor de código que permita trabajar inicialmente con Python, Java y C++.
4. Desarrollar un sistema de evaluación automática basado en instrucciones y casos de prueba definidos por el docente.
5. Implementar mecanismos para identificar errores frecuentes y ofrecer pistas que ayuden a los estudiantes a corregirlos.
6. Crear un panel de seguimiento que permita al docente consultar entregas, resultados y dificultades de aprendizaje.
7. Diseñar un modo de funcionamiento local que permita desarrollar clases sin depender de internet.
8. Validar la utilidad, usabilidad y efectividad educativa de la plataforma mediante pruebas en un grupo real.
9. Documentar la viabilidad técnica, económica y operativa del proyecto para su presentación en INNOVATECNM.

## 5. Usuarios beneficiarios

### Estudiantes

Podrán resolver ejercicios, escribir y ejecutar programas, consultar sus resultados, recibir pistas para corregir errores y dar seguimiento a su progreso.

### Docentes

Podrán organizar clases, preparar actividades, revisar entregas, identificar dificultades comunes y tomar decisiones pedagógicas con base en los resultados obtenidos.

### Instituciones educativas

Podrán disponer de una herramienta adaptable a diferentes grupos y asignaturas, con posibilidades de instalación local y generación de evidencia sobre el aprendizaje.

## 6. Propuesta de innovación

La innovación propuesta para AulaCode consiste en integrar la enseñanza de programación, la evaluación automática y el diagnóstico del aprendizaje dentro de una plataforma que pueda utilizarse durante clases presenciales y operar con conectividad limitada.

Se plantean cuatro diferenciadores principales:

### 6.1. Diagnóstico pedagógico basado en errores

La plataforma analizará los resultados de ejecución y las pruebas de los ejercicios para identificar patrones de dificultad. Podrá distinguir entre categorías de errores, como problemas de sintaxis, fallos en condiciones lógicas o resultados incorrectos.

Con esta información, el sistema mostrará al docente cuáles son las dificultades más frecuentes del grupo y ofrecerá sugerencias de refuerzo.

### 6.2. Funcionamiento en red local

AulaCode podrá instalarse en una computadora que funcione como servidor dentro del aula. Los estudiantes accederán desde sus equipos a través de una red local, permitiendo realizar actividades aunque no exista conexión a internet.

### 6.3. Entorno multilenguaje

La plataforma integrará un entorno común para trabajar inicialmente con Python, Java y C++. Esto permitirá utilizar la misma herramienta en distintas asignaturas de programación y mantener una estructura común para gestionar clases, actividades y resultados.

### 6.4. Seguimiento individual y grupal

El sistema permitirá visualizar el avance de cada estudiante y detectar tendencias del grupo sin exponer públicamente las dificultades individuales.

> Estos elementos son diferenciadores propuestos, no una novedad demostrada todavía. Antes de afirmar que AulaCode es única, se realizará un análisis del estado del arte y una comparación con plataformas existentes para identificar y validar su aporte.

## 7. Funcionamiento de la plataforma

AulaCode contará con dos entornos principales conectados entre sí.

### 7.1. Panel del docente

Permitirá:

- Crear clases y grupos.
- Generar códigos de acceso para estudiantes.
- Diseñar y publicar actividades.
- Definir instrucciones y casos de prueba.
- Consultar entregas y resultados.
- Visualizar errores frecuentes.
- Identificar estudiantes que requieren apoyo.
- Revisar estadísticas de progreso.

### 7.2. Espacio del estudiante

Permitirá:

- Ingresar a una clase mediante un código.
- Consultar instrucciones y ejemplos.
- Escribir código en un editor integrado.
- Seleccionar el lenguaje de programación.
- Ejecutar programas y consultar resultados.
- Recibir retroalimentación sobre errores.
- Entregar ejercicios.
- Consultar su propio progreso.

### 7.3. Ejemplo de uso en una clase real

En una clase sobre estructuras repetitivas, el docente explica los ciclos y publica un ejercicio en AulaCode. Los estudiantes desarrollan una solución en el editor y ejecutan su código.

La plataforma evalúa los resultados y registra los errores encontrados. Si varios estudiantes presentan dificultades similares, el panel docente identifica ese patrón y facilita la preparación de una actividad de refuerzo.

Finalmente, el profesor aplica un ejercicio adicional para comprobar si los estudiantes comprendieron el concepto.

## 8. Arquitectura tecnológica propuesta

La plataforma se desarrollará mediante una arquitectura web modular que permita separar la interfaz, la lógica del sistema, la base de datos y el motor de ejecución de programas.

### Tecnologías propuestas

| Componente | Tecnología | Propósito |
|---|---|---|
| Frontend | React + TypeScript | Interfaz y componentes reutilizables |
| Diseño de interfaz | Tailwind CSS | Diseño adaptable |
| Editor de código | Monaco Editor | Edición con resaltado de sintaxis |
| Backend | Python + FastAPI | API y lógica de negocio |
| Base de datos local | SQLite | Instalación sencilla para pruebas de aula |
| Base de datos central | PostgreSQL | Gestión de múltiples usuarios y grupos |
| Ejecución aislada | Docker con configuración reforzada | Separación de procesos que ejecutan código |
| Despliegue | Docker Compose | Facilitar la instalación |
| Pruebas | Pytest y Playwright | Pruebas del backend y de flujos de usuario |

Estas tecnologías constituyen una propuesta inicial y podrán ajustarse según las capacidades del equipo.

### Arquitectura general

La interfaz web permitirá que docentes y estudiantes accedan a sus respectivas funciones. Las solicitudes se procesarán mediante una API que gestionará usuarios, clases, actividades y resultados.

El backend se comunicará con la base de datos y con un servicio independiente encargado de ejecutar el código de los estudiantes en entornos aislados.

Los resultados de las ejecuciones se utilizarán para evaluar los ejercicios y alimentar el módulo de diagnóstico pedagógico.

### Funcionamiento con internet

La plataforma podrá desplegarse en un servidor central accesible mediante internet para gestionar clases, usuarios y actividades.

### Funcionamiento sin internet

Una computadora dentro del aula podrá alojar la aplicación y su base de datos local. Los estudiantes accederán mediante la red local y podrán realizar ejercicios sin depender de servicios externos.

La sincronización automática entre las instalaciones locales y la nube se considerará una funcionalidad posterior, debido a su complejidad técnica.

## 9. Módulos del producto mínimo viable (MVP)

El producto mínimo viable será la primera versión funcional que permitirá demostrar la utilidad de AulaCode en una clase real.

### Módulo 1. Gestión de clases

Administración de grupos, creación de sesiones, acceso mediante códigos y control de roles.

### Módulo 2. Editor y ejecución de código

Editor integrado con soporte inicial para Python, Java y C++, ejecución de programas y visualización de resultados.

### Módulo 3. Actividades y evaluación automática

Creación de ejercicios, publicación de instrucciones, recepción de entregas y evaluación mediante casos de prueba.

### Módulo 4. Panel de seguimiento docente

Visualización de entregas, resultados, dificultades recurrentes y progreso por estudiante o concepto.

### Módulo 5. Tutor de errores basado en reglas

Sistema que interprete determinados patrones de error y ofrezca pistas progresivas sin proporcionar automáticamente toda la solución.

### Módulo 6. Funcionamiento local

Instalación en una computadora del aula, acceso por red local, almacenamiento de actividades y recuperación de resultados sin internet.

### Funcionalidades que se aplazarán

- Generación libre de cursos mediante inteligencia artificial.
- Videollamadas y clases virtuales completas.
- Aplicaciones móviles nativas.
- Sincronización compleja entre instalaciones locales y la nube.
- Soporte para más lenguajes que los tres iniciales.

Estas funciones se considerarán después de validar el MVP.

## 10. Seguridad y protección de datos

Debido a que la plataforma ejecutará código escrito por estudiantes y manejará información académica, la seguridad será una prioridad desde el diseño.

### Seguridad de ejecución

- Ejecutar el código en entornos aislados.
- Limitar tiempo, memoria, CPU y tamaño de salida.
- Restringir el acceso a archivos y recursos del servidor.
- Desactivar el acceso a la red para los programas ejecutados.
- Evitar privilegios administrativos en los procesos de ejecución.
- Utilizar entornos temporales y eliminarlos al terminar.
- No ejecutar código estudiantil directamente dentro del proceso principal de la API.

Docker ayuda a aislar procesos, pero por sí solo no garantiza seguridad absoluta. Se evaluarán configuraciones de aislamiento reforzado, permisos mínimos y actualizaciones periódicas.

### Protección de cuentas e información

- Contraseñas almacenadas con hash seguro y sesiones protegidas.
- Permisos separados para docentes, estudiantes y administradores.
- Recolección mínima de datos personales.
- Acceso restringido a calificaciones y resultados.
- Copias de seguridad y procedimientos de recuperación.
- Registro de acciones administrativas relevantes.
- Procedimientos de conservación, corrección y eliminación de datos.

La implementación deberá considerar la legislación mexicana aplicable en materia de datos personales y las políticas de la institución participante. Para el piloto se recomienda utilizar identificadores seudónimos en los análisis y evitar publicar clasificaciones individuales.

## 11. Plan de validación

La plataforma se evaluará mediante pruebas técnicas y un piloto educativo.

### Fase 1. Investigación del problema — semanas 1 y 2

Entrevistar a docentes, encuestar estudiantes y observar clases de programación.

**Entregable:** informe de necesidades y requisitos priorizados.

### Fase 2. Desarrollo del prototipo — semanas 3 a 7

Construir los módulos principales y realizar pruebas internas.

**Entregable:** MVP funcional y guion de demostración.

### Fase 3. Pruebas técnicas — semanas 8 y 9

Evaluar seguridad, rendimiento, permisos, recuperación de datos y funcionamiento sin internet.

**Entregable:** informe de pruebas y lista de defectos corregidos.

### Fase 4. Piloto educativo — semanas 10 y 11

Probar la plataforma en un grupo real, idealmente de 20 a 30 estudiantes si la institución lo permite. Aplicar ejercicios diagnósticos iniciales y finales, observar la dinámica de clase y recopilar opiniones de docentes y estudiantes.

**Entregable:** resultados de aprendizaje, usabilidad y experiencia docente.

### Fase 5. Evaluación y preparación para la competencia — semana 12

Analizar resultados, corregir fallos prioritarios y preparar la memoria técnica, el modelo de negocio y la presentación.

**Entregable:** expediente de evidencias y presentación para el jurado.

### Diseño del experimento

1. Aplicar una prueba diagnóstica de conceptos de programación.
2. Impartir una unidad didáctica con ejercicios equivalentes.
3. Utilizar AulaCode durante las sesiones planificadas.
4. Aplicar una prueba final comparable a la inicial, con problemas diferentes pero de dificultad equivalente.
5. Registrar tiempo de resolución, intentos de ejecución, tipos de error y percepción del docente y del alumnado.

Si es viable, se compararán los resultados con otro grupo que utilice la metodología habitual, procurando mantener equivalentes los contenidos, el tiempo de enseñanza y la dificultad. Si solo se dispone de un grupo, se realizará una comparación antes-después y se reconocerán las limitaciones para atribuir los cambios exclusivamente a la plataforma.

## 12. Indicadores de evaluación

Las siguientes metas son provisionales, no resultados garantizados. Se ajustarán después de establecer la línea base.

| Indicador | Método de medición | Meta inicial |
|---|---|---:|
| Aprendizaje | Diferencia entre puntuación inicial y final | Mejora media de 15 puntos porcentuales |
| Finalización | Actividades completadas / asignadas | Al menos 80% |
| Autonomía | Ejercicios resueltos sin intervención directa | Aumentar frente a la línea base |
| Trabajo docente | Tiempo de revisión y detección de dificultades | Reducir frente a la línea base |
| Usabilidad | Encuesta a docentes y estudiantes | Al menos 80% de valoración favorable |
| Confiabilidad | Ejecuciones completadas sin fallos en pruebas definidas | Al menos 95% |
| Modo local | Sesión realizada sin internet | Completar la sesión prevista |

Los resultados deberán reportarse de forma transparente, incluyendo el tamaño de la muestra, las condiciones del piloto, los resultados iniciales y finales, y las limitaciones.

## 13. Modelo de negocio y sostenibilidad

AulaCode podrá orientarse a instituciones educativas interesadas en mejorar sus prácticas de enseñanza de programación.

### Propuesta de valor

Ofrecer una plataforma integrada para enseñar, practicar y evaluar programación, con seguimiento del aprendizaje y funcionamiento local.

### Clientes potenciales

- Institutos tecnológicos.
- Universidades.
- Instituciones de educación media superior.
- Centros de capacitación tecnológica.

### Estrategia inicial

Realizar una implementación piloto en una institución, capacitar a los docentes y evaluar el uso del sistema antes de plantear una expansión.

### Posibles fuentes de sostenibilidad

Podrá estudiarse una edición comunitaria de código abierto y servicios opcionales de instalación, capacitación, soporte y mantenimiento institucional, siempre que sean viables económica y legalmente.

Antes de definir precios o proyecciones financieras, será necesario estudiar los costos de desarrollo, infraestructura, instalación y soporte, así como la disposición de las instituciones a adoptar la plataforma.

## 14. Alineación con INNOVATECNM

AulaCode se plantea para el Certamen de Proyectos de INNOVATECNM, sujeto a la revisión de la convocatoria vigente y de la categoría correspondiente.

| Elemento | Cómo lo atendería AulaCode |
|---|---|
| Problema identificado | Investigación con estudiantes y docentes de programación |
| Estado del arte | Comparación técnica y pedagógica con plataformas existentes |
| Innovación tecnológica | Diagnóstico de errores, panel de aula y funcionamiento local integrados |
| Prototipo funcional | Demostración de una clase completa con ejecución y evaluación |
| Validación | Pruebas técnicas y piloto educativo con indicadores |
| Impacto social | Acceso a herramientas de programación en aulas con conectividad limitada |
| Escalabilidad | Posibilidad de instalación en otros grupos, asignaturas e instituciones |
| Modelo de negocio | Plan de adopción, soporte, costos y sostenibilidad |
| Propiedad intelectual | Documentación de autoría y revisión de licencias de componentes |

La categoría de participación deberá confirmarse con el asesor del proyecto y el responsable institucional de INNOVATECNM. También se deben verificar los requisitos de integración del equipo, documentación, memoria técnica, modelo de negocio y presentación establecidos en la convocatoria aplicable.

Como las bases pueden cambiar entre ediciones, la documentación oficial vigente debe ser la referencia definitiva. Portal oficial: https://innova.tecnm.mx/

## 15. Cronograma de desarrollo

Se propone un plan inicial de 12 semanas, sujeto al tamaño del equipo y al calendario de la competencia.

- **Semanas 1 y 2:** investigación, encuestas, entrevistas y análisis de plataformas existentes.
- **Semana 3:** definición de requisitos y diseño de arquitectura.
- **Semanas 4 a 7:** desarrollo de gestión de clases, editor, ejecución y evaluación.
- **Semanas 8 y 9:** diagnóstico pedagógico, modo local y pruebas técnicas.
- **Semanas 10 y 11:** piloto educativo y recolección de resultados.
- **Semana 12:** análisis de evidencias, correcciones y preparación de la presentación.

El cronograma deberá actualizarse al conocer las fechas oficiales de registro y entrega.

## 16. Riesgos principales y mitigación

| Riesgo | Estrategia de mitigación |
|---|---|
| Complejidad multilenguaje | Validar primero un flujo completo con un lenguaje y después integrar los demás |
| Seguridad de ejecución | Separar el motor del backend y aplicar límites estrictos de recursos y permisos |
| Innovación no demostrada | Realizar análisis del estado del arte y validar diferencias con pruebas |
| Conectividad limitada | Probar la instalación local desde las primeras etapas |
| Baja adopción docente | Involucrar a docentes desde la investigación y hacer pruebas de usabilidad |
| Alcance excesivo | Priorizar el MVP y aplazar funciones avanzadas |
| Protección de datos | Recopilar solo información necesaria y coordinar el piloto con la institución |

## 17. Resultados esperados

Al concluir la primera etapa de desarrollo, se espera disponer de:

1. Un prototipo funcional de AulaCode.
2. Un entorno de clases con roles diferenciados.
3. Un editor de código con soporte inicial para Python, Java y C++.
4. Un sistema de actividades y evaluación automática.
5. Un panel de seguimiento para el docente.
6. Un módulo inicial de diagnóstico de errores.
7. Una instalación funcional en red local.
8. Un informe de pruebas técnicas y educativas.
9. Una memoria técnica y documentación del proyecto.
10. Una propuesta de sostenibilidad y un modelo de negocio preliminar.

Estos resultados permitirán presentar el proyecto con evidencia concreta de desarrollo y funcionamiento.

## 18. Conclusión

AulaCode propone una solución tecnológica para mejorar la enseñanza y el aprendizaje de programación mediante un entorno que integra las necesidades del docente y del estudiante.

Su principal valor potencial radica en combinar la práctica de programación, la evaluación automática, el diagnóstico pedagógico y la posibilidad de utilizar la plataforma sin depender de internet.

El proyecto busca ir más allá de una aplicación de ejercicios: pretende convertirse en una herramienta que ayude a los docentes a tomar decisiones durante la clase y permita a los estudiantes desarrollar autonomía en la resolución de problemas.

Para lograrlo, será fundamental investigar las necesidades reales de los usuarios, demostrar las diferencias frente a las soluciones existentes, construir un prototipo funcional y validar su impacto mediante pruebas transparentes.

La meta es desarrollar una propuesta técnicamente viable, pedagógicamente útil y suficientemente documentada para su evaluación en INNOVATECNM.

---

## Próximos pasos del equipo

- [ ] Validar el problema con docentes y estudiantes.
- [ ] Revisar la convocatoria oficial vigente y confirmar la categoría de participación.
- [ ] Realizar un análisis del estado del arte.
- [ ] Definir los integrantes y las responsabilidades del equipo.
- [ ] Priorizar el alcance del MVP.
- [ ] Diseñar la arquitectura y el modelo de datos.
- [ ] Construir el primer flujo funcional de clase.
- [ ] Planificar las pruebas técnicas y el piloto educativo.
