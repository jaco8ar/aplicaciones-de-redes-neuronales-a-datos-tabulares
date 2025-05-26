# Trabajo 2: aplicaciones-de-redes-neuronales-a-datos-tabulares
----------------------
Docente: Juan David Ospina Arango

Estudiantes: - Hailer Serna Hernández - Juan Jose Correa Hurtado - Jacobo Ochoa Ramirez
----------------------
El reto en este trabajo es crear un modelo para predecir la probabilidad de que un individuo incumpla con el pago de su crédito.

La variable "loan_status" (incumplimiento de las obligaciones financieras) está dada en el archivo "Credit Risk Dataset" (disponible en https://www.kaggle.com/datasets/ranadeep/credit-risk-dataset/data).


Reto
1. Cree y valide un modelo de probabilidad de incumplimiento basado en redes neuronales artificiales. Optimice la arquitectura del modelo.
2. Represente este modelo con una scorecard
3. Analice qué variables hacen más riesgosa a una persona
4. Cree una app web que le permita saber a las personas, de acuerdo con sus características, cuál es su scorecard y cómo se ve contra la población.

Entregables
Reporte técnico publicado como entrada de blog
Sitio web donde el usuario puede ver cómo se comporta su score en función de sus características
Video promocional de la aplicación web

----------------------

Evaluación
La evaluación se hará siguiendo los Criterios de Evaluación:
Reporte técnico
El problema está bien delimitado y se plantea una metodología para
resolverlo
Se incluye un análisis descriptivo y se generan hipótesis a partir del
mismo
Se plantean modelos y se evalúa su desempeño con diferentes conjuntos
de datos. Se incluye un modelo de baja complejidad como referencia.
Se incluye un listado de aprendizajes sobre el problema generados por el
proceso de modelamiento
Se plantea un caso de uso del modelo
El reporte sigue las normas APA o las de algún formato de revista
científica
Las gráficas y tablas están rotuladas y citadas dentro del texto
El reporte se apoya en bibliografía relevante correctamente citada
Aplicación Web
El aplicativo es intuitivo y fácil de usar para nuevos usuarios
La aplicación resuelve un problema a través de un modelo
La aplicación contiene los enlaces al reporte técnico y el material
publicitario
Video publicitario
El video presenta la aplicación web como la solución a un problema
El video genera entusiasmo por utilizar la aplicación

Reporte de contribución individual
Al final del video publicitario cada integrante debe aparecer mencionando su "contribución individual", es decir, sus aportes específicos de cada integrante del grupo. Por ejemplo:

+ Juan Pérez: programación del componente A, elaboración del reporte
+ Maria Pérez: formato del reporte, elaboración de la animación X
+ Diego Posada: selección de bibliografía, desarrollo de los componentes C y D, elaboración del reporte

----------------------

Otras consideraciones
Definición de la variable objetivo
Un elemento crítico para el éxito del modelo es la correcta definición de la variable objetivo. Para este proyecto, debemos modelar la probabilidad de que un cliente sea "malo" (que incumpla con el pago de su crédito).
Codificación binaria de la variable objetivo
Se recomienda crear una variable binaria donde:
 (aquel que pagó su crédito completamente)
 (aquel que no pagó su crédito)
Clasificación de categorías en la variable original

Se recomienda tener en cuenta lo siguiente para transformar las categorías originales en la nueva variable binaria:
"Current": Clientes que están al día. Codificación: NA. Justificación: No hay certeza sobre su comportamiento final de pago.
"Fully paid": Créditos completamente pagados. Codificación: 0. Justificación: Son buenos pagadores confirmados.
"Charged off": Créditos reconocidos como incobrables. Codificación: 1. Justificación: Son definitivamente malos pagadores.
"Late (31-120)": Atrasos entre 31 y 120 días. Codificación: 1. Justificación: Se considerarán como malos pagadores.
"Issued": Crédito aprobado pero sin historia. Codificación: NA. Justificación: No hay información sobre comportamiento de pago.
"In Grace Period": En periodo de gracia. Codificación: NA. Justificación: Aún no están obligados a pagar.
"Late (16-30 days)": Atrasos entre 16 y 30 días. Codificación: NA. Justificación: No hay certeza sobre su comportamiento final.
"Does not meet the credit policy. Status:Fully Paid": No cumple requisitos pero pagó. Codificación: 0. Justificación: Son buenos pagadores confirmados.
"Default": Impago confirmado. Codificación: 1. Justificación: Son definitivamente malos pagadores.
"Does not meet the credit policy. Status:Charged Off": No cumple requisitos y no pagó. Codificación: 1. Justificación: Son definitivamente malos pagadores.
Último pero no menos importante:
Los modelos de riesgo de crédito usualmente se centran en estimar la probabilidad de que un cliente sea "malo" (valor 1), no de que sea bueno.
La codificación binaria debe reflejar el sentido del negocio y el objetivo específico del score crediticio.
Los casos marcados como NA no deben incluirse en el entrenamiento del modelo, pues no tenemos certeza sobre su clasificación final.
