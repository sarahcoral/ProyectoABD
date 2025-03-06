# CONCLUSIONES


## Análisis Descriptivo


### 🚀 ¿Qué hacemos con el código?


#### **1. Estructura del Notebook**

- Se importan librerías esenciales (`pandas`, `numpy`, `matplotlib`, `seaborn`, `sqlite3`).
- Se carga una base de datos SQLite (`linkedindatabase.db`).
- Se extraen varias tablas de la base de datos:
    - `clean_numerical_postings` (datos numéricos limpios sobre ofertas de trabajo).
    - `postings` (ofertas de trabajo).
    - `companies` (empresas).
    - `industries` (industrias).
    - `job_industries` (relación entre empleos e industrias).
    - `skills` (habilidades).
    - `job_skills` (relación entre empleos y habilidades).

#### **2. Cálculo de estadísticas descriptivas**

- Se filtran los datos de salario (`max_salary`, `min_salary`, `normalized_salary`) para eliminar valores extremos.
- Se calculan:
  - **Media, Mediana y Moda** para los tres tipos de salario (`normalizado`, `máximo`, `mínimo`).
  - **Coeficiente de asimetría** para evaluar la distribución de los salarios.

### 💡 Análisis de gráficas:


#### **1. Distribución de salarios promedio (Gráfico de dispersión - Stripplot)**

- **Análisis**
    - La distribución de los salarios no es uniforme: algunas categorías tienen valores más concentrados, mientras que otras presentan una dispersión mucho mayor.  
    - Hay una acumulación notable en salarios bajos y una menor cantidad de valores en los extremos altos.  
    - Algunas industrias parecen pagar significativamente más que otras, lo que sugiere desigualdad salarial según el sector.  

- **Conclusión avanzada**  
    El mercado laboral tiene una segmentación fuerte en términos de salarios. Existen sectores donde los salarios están muy concentrados en ciertos rangos, mientras que otros muestran una gran variabilidad. La presencia de valores atípicos altos sugiere que ciertos puestos especializados pueden recibir compensaciones significativamente mayores.

#### **2. Histograma y diagrama de caja de los salarios**

- **Análisis**  
    - La distribución de los salarios tiene un **sesgo a la derecha**, lo que indica que la mayoría de los empleados gana menos que el promedio.  
    - La mediana es considerablemente menor que la media, lo que confirma la existencia de valores atípicos altos.  
    - El primer cuartil (Q1) y el tercer cuartil (Q3) están bastante separados, lo que implica alta dispersión en los datos.  

- **Conclusión avanzada**  
    El salario promedio puede ser engañoso al evaluar oportunidades laborales, ya que unos pocos valores altos elevan la media. Para una persona buscando empleo, **el salario mediano es una mejor referencia**. Además, la alta dispersión sugiere que negociar el salario puede ser clave, pues las diferencias dentro de la misma industria pueden ser significativas. 

#### **3. Distribución de vistas y aplicaciones (Gráfico de dispersión - Logarítmico)**  

- **Análisis**  
    - Se observa que la relación entre vistas y aplicaciones no es lineal: muchas publicaciones con muchas vistas no necesariamente tienen más aplicaciones.  
    - Algunas ofertas reciben una cantidad masiva de visitas pero pocas aplicaciones, lo que indica que los candidatos pueden estar descartándolas por requisitos poco atractivos o salarios bajos.  
    - La escala logarítmica muestra que la mayoría de las publicaciones tienen menos de 1,000 vistas, mientras que solo unas pocas superan las 10,000.

- **Conclusión avanzada**  
    El hecho de que muchas ofertas sean vistas pero no aplicadas indica problemas en los requisitos, la compensación o la percepción del empleo. Esto sugiere que los reclutadores deberían analizar mejor cómo presentan sus ofertas y ajustar detalles como salario y beneficios para hacerlas más atractivas.

#### **4. Distribución de visitas a ofertas de empleo (Gráfico de dispersión - Logarítmico)**

- **Análisis**  
    - Se confirma que hay una gran desigualdad en la visibilidad de las ofertas de trabajo.  
    - Algunas ofertas acumulan una cantidad desproporcionada de visitas, mientras que la mayoría apenas recibe tráfico.  
    - La visualización logarítmica permite ver que muchas publicaciones tienen menos de 100 visitas, lo que sugiere que dependen de la estrategia de marketing o visibilidad en la plataforma.  

- **Conclusión avanzada**  
    La distribución desigual de visitas implica que no todas las ofertas tienen las mismas oportunidades de atraer candidatos. Esto puede deberse a la popularidad de la empresa, el atractivo del cargo o la optimización de la publicación. **Las empresas con pocas visitas deberían revisar sus estrategias de difusión y asegurarse de que sus ofertas sean fácilmente encontradas.**

#### **5. Histograma de visitas**

- **Análisis**  
    - Se confirma que la mayoría de las publicaciones tienen un número de visitas bajo.  
    - Solo un pequeño porcentaje de publicaciones recibe tráfico masivo, lo que sugiere que ciertos empleadores dominan la atención en la plataforma.  
    - Al aplicar la escala logarítmica, se observa una caída exponencial en la cantidad de ofertas conforme el número de visitas aumenta.  

- **Conclusión avanzada**  
    El mercado laboral online está dominado por pocas publicaciones que reciben la mayor parte de la atención. Esto implica que **la competencia por visibilidad es alta** y que los empleadores deben optimizar sus estrategias de marketing laboral. **Para los candidatos, esto significa que las oportunidades más visibles pueden no ser las mejores, ya que muchas excelentes ofertas podrían estar ocultas en publicaciones con menos tráfico.**

#### **Conclusiones generales**

- **El salario promedio no refleja la realidad del mercado** debido a la existencia de valores atípicos. La mediana y los cuartiles son mejores indicadores.  
- **Muchas ofertas reciben visitas pero pocas aplicaciones**, lo que indica que los candidatos son selectivos o que los requisitos no son atractivos.  
- **Un pequeño número de ofertas concentra la mayoría del tráfico**, lo que sugiere una competencia desigual por la visibilidad.  
- **Los empleadores deben mejorar sus estrategias para atraer talento**, mientras que los candidatos deben explorar más allá de las ofertas más vistas para encontrar buenas oportunidades.


## Análisis Exploratorio

### 🚀 ¿Qué hacemos con el código?

#### 1. **Carga de librerías:**

- Se importan bibliotecas clave para análisis de datos como `pandas`, `numpy`, `matplotlib`, y `seaborn`.
- También se usa `sqlite3` para interactuar con una base de datos SQL.

#### 2. **Configuración del proyecto:**

- Se configuran rutas para módulos y scripts adicionales.

#### 3. **Carga de la base de datos:**

- Se establece conexión con un archivo SQLite llamado `linkedindatabase.db`.
- Se cargan varias tablas en `DataFrames` de `pandas`, incluyendo:
    - `clean_numerical_postings`: Contiene datos salariales filtrados.
    - `postings`, `companies`, `industries`, `job_industries`, `skills`, `job_skills`, `company_industries`: Tablas con información sobre ofertas de trabajo, compañías e industrias.


#### 4. **Limpieza de datos:**

- Se eliminan valores extremos en las columnas `max_salary`, `min_salary` y `normalized_salary` para descartar datos irreales.
- Se calcula la duración de las ofertas de trabajo (`duration`), restando `closed_time` de `listed_time`.



### 💡 Análisis de gráficas:

#### **1. Matriz de Correlación: Salario, Duración, Aplicaciones y Vistas**

- **Correlaciones clave:**  
    - Si el `normalized_salary` tiene una correlación positiva con `applies` y `views`, significa que los trabajos con salarios más altos atraen más atención y postulaciones.  
    - Si la `duration` tiene correlaciones negativas con `applies` y `views`, sugiere que las ofertas populares tienden a cerrarse más rápido.  
    - Una baja correlación entre `salary` y `duration` podría indicar que la duración de una oferta no depende directamente del salario.  

- **Conclusión avanzada:**  
    - Si los trabajos con mayor salario no tienen muchas aplicaciones en comparación con los de menor salario, podría deberse a requisitos más altos o a que los postulantes consideran estos puestos inaccesibles.  
    - Una correlación negativa fuerte entre `duration` y `views` podría sugerir que los trabajos con más visibilidad tienden a cerrarse rápido, lo que puede influir en estrategias de publicación para empresas.

#### **2. Empresas con Mayor Salario Promedio**

- **Patrones de mercado:**  
    - Si las empresas con salarios más altos pertenecen a un sector específico (ejemplo: tecnología o finanzas), indica que ciertas industrias están impulsando el crecimiento salarial.  
    - La dispersión de los salarios podría mostrar si los sueldos altos son exclusivos de unas pocas empresas o si hay una tendencia general en varias compañías.  

- **Conclusión avanzada:**  
    - Si pocas empresas ofrecen salarios muy altos, es posible que haya monopolización del talento, donde solo unas cuantas organizaciones pueden competir por los mejores candidatos.  
    - Si hay un rango salarial amplio dentro de las empresas del top 10, indica que los salarios pueden depender del puesto más que de la empresa en sí.

#### **3. Empresas con Más Ofertas de Trabajo**

- **Tendencias de contratación:**  
    - Si hay una superposición entre las empresas con más ofertas y las de mayores salarios, significa que algunas compañías están dominando tanto en cantidad como en calidad de contratación.  
    - Si la empresa con más ofertas no está en el top de salarios, podría indicar una estrategia de contratación masiva con salarios moderados.  

- **Conclusión avanzada:**  
    - Empresas con muchas ofertas pero salarios bajos pueden estar contratando para posiciones temporales o de alta rotación.  
    - Un alto número de ofertas en pocas empresas puede indicar una concentración del mercado, reduciendo la diversidad de oportunidades para los postulantes.

#### **4. Industrias con Más Empresas**

- **Dominio de sectores específicos:**  
    - Si las industrias más grandes coinciden con las de mayor salario, indica que el crecimiento económico en ciertos sectores está atrayendo más inversión.  
    - Si hay una industria con muchas empresas pero no está en el top de salarios, significa que tiene alta competencia y posiblemente márgenes de ganancia ajustados.  

- **Conclusión avanzada:**  
    - Si la industria con más empresas también lidera en ofertas de empleo, significa que está en expansión activa.  
    - Una industria con muchas empresas pero sin dominar los salarios podría estar fragmentada, sin empresas grandes que impongan sueldos altos.

#### **5. Habilidades Más Solicitadas**

- **Evolución del mercado laboral:**  
    - Si hay muchas habilidades técnicas en el top (ej. programación, análisis de datos), significa que la demanda de talento está orientada hacia tecnología.  
    - Si hay un equilibrio entre habilidades blandas y técnicas, indica que las empresas buscan un perfil más versátil en los candidatos.  

- **Conclusión avanzada:**  
    - Habilidades con alta demanda pero bajos salarios podrían significar que muchas personas las poseen, reduciendo su exclusividad.  
    - Si algunas habilidades aparecen tanto en el top de demanda como en el top de salarios, significa que la oferta de talento en esa área es menor que la demanda.

#### **6. Salario Promedio por Habilidad**

- **Competencia y exclusividad de habilidades:**  
    - Habilidades con salarios altos pero baja demanda pueden ser altamente especializadas y difíciles de encontrar en el mercado.  
    - Si las habilidades más demandadas no son las mejor pagadas, indica que la oferta de candidatos en esa área es alta y las empresas pueden pagar menos.  

- **Conclusión avanzada:**  
    - Si las habilidades más demandadas y mejor pagadas coinciden, significa que las empresas están en una carrera activa por captar talento en esas áreas.  
    - Si una habilidad bien pagada no está entre las más solicitadas, podría ser un nicho lucrativo con pocas vacantes pero sueldos altos. 

#### **Conclusiones generales**

1. **El salario no siempre es el principal factor en la duración de las ofertas.**  
    - Un salario alto puede atraer más aplicaciones, pero si el puesto requiere habilidades muy especializadas, la vacante puede permanecer abierta más tiempo.  

2. **Las empresas con más ofertas no siempre ofrecen los mejores salarios.**  
    - Puede haber estrategias de contratación masiva con sueldos moderados, mientras que empresas con menos ofertas pueden estar apuntando a talento más exclusivo con mejores salarios.  

3. **Las industrias con más empresas no necesariamente lideran en salarios.**  
    - Algunos sectores tienen muchas compañías, pero los mejores sueldos pueden concentrarse en industrias más específicas.  

4. **Las habilidades más solicitadas no siempre son las mejor pagadas.**  
    - Si una habilidad es muy demandada pero tiene un salario bajo, puede indicar que hay mucha oferta de candidatos en esa área.  

5. **El mercado laboral está guiado por la competencia entre oferta y demanda de talento.**  
    - Las habilidades con alta demanda y salarios altos son las más valiosas, mientras que las de baja demanda y bajos salarios podrían estar en riesgo de automatización o saturación.

## Análisis Predictivo

### 💡 Análisis de gráficas:

#### **1. Variación en la publicación de ofertas de empleo** 

- **Análisis**
    - Los datos muestran que la cantidad de publicaciones de empleo **no es constante**, sino que sigue un patrón fluctuante.  
    - Hay días en los que se concentran más ofertas, lo que sugiere que ciertos períodos tienen **mayor actividad de contratación**.  
    - Esto puede indicar que las empresas tienden a publicar ofertas en momentos estratégicos, posiblemente alineados con ciclos de presupuesto, fin de mes o días laborales clave.  

- **Conclusión avanzada**
    El número de publicaciones no es constante y parece tener **patrones estacionales**. Esto puede deberse a estrategias de contratación en ciertas épocas del mes o la semana. Si se identifican picos de publicación, los candidatos pueden elegir mejor cuándo aplicar para maximizar sus oportunidades.

#### **2. Predicción de salario promedio para Mayo 2024 (Regresión lineal)**

- **Análisis**
    - Basándose en los datos históricos, se estimó el salario promedio para **el 1 de mayo de 2024**.  
    - El valor obtenido indica que los salarios en ese mes seguirán una trayectoria esperada dentro de los valores previamente registrados.  
    - No se observan cambios bruscos que sugieran una alteración significativa del mercado, lo que implica **cierta estabilidad en la oferta y la demanda de empleo en este período**.  

- **Conclusión avanzada**

    El modelo sugiere que **el salario promedio tendrá una tendencia predecible basada en datos pasados**. Sin embargo, la regresión lineal supone que la tendencia se mantiene estable, lo que puede no ser cierto si hay eventos económicos o cambios en el mercado laboral. **Validar el modelo con datos futuros será clave para mejorar su precisión**. Es decir, La evolución de los salarios en el tiempo sugiere un mercado estable sin cambios extremos en la compensación.

#### **3. Tendencia de salarios en función del tiempo**

- **Análisis**
    - La relación entre la fecha de publicación y el salario muestra que **los salarios varían con el tiempo, pero mantienen una dirección clara**.  
    - Se observa que en ciertos períodos los salarios son más altos o más bajos, lo que puede estar relacionado con la demanda de talento en distintos momentos.  
    - La tendencia general sugiere un **comportamiento predecible** del salario promedio en función de la fecha de publicación de las ofertas.  

- **Conclusión avanzada**
    Los salarios de las ofertas no son aleatorios, sino que siguen una tendencia específica en el tiempo, influenciada por factores del mercado laboral.

#### **Conclusión general**

- El volumen de publicaciones de empleo **no es uniforme** y presenta períodos de alta actividad.  
- Los salarios varían en función del tiempo, pero siguen **un patrón predecible**.  
- La proyección para mayo de 2024 indica **estabilidad en los salarios**, sin cambios abruptos en la tendencia.  

Este análisis proporciona información clave para entender **cómo y cuándo se publican ofertas, cómo varían los salarios en el tiempo y qué se espera en el corto plazo**. 🚀