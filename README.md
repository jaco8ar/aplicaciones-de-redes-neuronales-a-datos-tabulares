# Trabajo 2: aplicaciones-de-redes-neuronales-a-datos-tabulares

----------------------
Docente: Juan David Ospina Arango

Estudiantes: - Hailer Serna Hernández - Juan Jose Correa Hurtado - Jacobo Ochoa Ramirez

----------------------
Este proyecto tiene como objetivo crear un modelo basado en redes neuronales artificiales para predecir la probabilidad de incumplimiento de pago de un crédito, a partir del análisis de datos financieros y personales de individuos.

### Reto
Crear y validar un modelo de probabilidad de incumplimiento basado en redes neuronales artificiales (ANN). Se debe optimizar su arquitectura.

Representar el modelo con una scorecard (tarjeta de puntuación).

Analizar las variables que hacen más riesgoso a un individuo.

Crear una aplicación web que permita a las personas conocer su scorecard en función de sus características y compararse con la población.

### Dataset
El dataset se encuentra disponible en Kaggle:
Credit Risk Dataset – Kaggle:  https://www.kaggle.com/datasets/ranadeep/credit-risk-dataset/data

La variable objetivo es loan_status, que indica el estado del crédito.

### Codificación de la Variable Objetivo
Se debe crear una variable binaria que indique si un individuo incumplió con el pago:

| Estado Original                                        | Codificación | Justificación                        |
| ------------------------------------------------------ | ------------ | ------------------------------------ |
| `Fully Paid`                                           | 0            | Buen pagador confirmado              |
| `Charged Off`                                          | 1            | Incobrable: mal pagador              |
| `Late (31-120 days)`                                   | 1            | Atraso grave: mal pagador            |
| `Default`                                              | 1            | Impago confirmado                    |
| `Does not meet the credit policy. Status: Fully Paid`  | 0            | Buen pagador confirmado              |
| `Does not meet the credit policy. Status: Charged Off` | 1            | Mal pagador confirmado               |
| `Current`                                              | NA           | No se conoce el comportamiento final |
| `Issued`                                               | NA           | Sin información de pago              |
| `In Grace Period`                                      | NA           | Aún no se requiere pago              |
| `Late (16-30 days)`                                    | NA           | Atraso leve: no concluyente          |


**Importante**: Las observaciones con valor NA deben ser eliminadas del conjunto de entrenamiento.

### Entregables
Reporte técnico publicado como entrada de blog.

Aplicación web donde el usuario puede visualizar su scorecard.

Video promocional de la aplicación.

## Evaluación
### Reporte técnico
Problema bien planteado con metodología clara.

Análisis descriptivo y generación de hipótesis.

Comparación entre modelos (incluyendo uno de baja complejidad como referencia).

Aprendizajes extraídos del modelado.

Caso de uso realista para el modelo.

Formato APA o formato de revista científica.

Gráficas y tablas debidamente citadas y rotuladas.

Bibliografía relevante correctamente citada.

### Aplicación Web
Intuitiva y fácil de usar.

Resuelve el problema planteado mediante el modelo.

Contiene enlaces al reporte técnico y material promocional.

### Video Promocional
Presenta la app como solución al problema.

Genera entusiasmo por su uso.

Cada miembro menciona su contribución individual, por ejemplo:

+ Juan Pérez: programación del componente A, elaboración del reporte
+ Maria Pérez: formato del reporte, elaboración de la animación X
+ Diego Posada: selección de bibliografía, desarrollo de los componentes C y D, elaboración del reporte
  
## Consideraciones Finales
El modelo debe estimar la probabilidad de que un cliente sea “malo” (valor 1).

El enfoque debe reflejar el sentido del negocio, centrado en la prevención del riesgo.

La scorecard puede usar variables continuas, no es obligatorio categorizar todo.
