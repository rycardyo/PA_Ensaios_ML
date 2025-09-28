## Ensaios de Machine Learning.

### 1.0 - Problema de negócio

Descrição:

Um entendimento mais aprofundado dos algorimos de Machine learning, é essencial para sua correta aplicação aos mais diversos cenários possíveis, axiliando tanto na escolha de um determinado algoritmo para a solução de algum problema, como para o melhor ajuste destes, elevando a qualidade e confiança de soluções de aprendizado de máquina. 

Objetivo:

O objetivo desse projeto será realizar ensaios com algoritmos de Classificação, Regressão e
Clusterização, para estudar a mudança do comportamento da performance, a medida que os
valores dos principais parâmetros de controle de overfitting e underfitting mudam.

### 2. Planejamento da Solução

- 2.1 - Produto Final
    
    O produto final serão tabelas exibindo a perfomance dos algoritmos, avaliados sob diversas métricas, para 3 conjuntos de dados diferentes: treino , teste e validação. 
    
- 2.2 - Algoritmos Ensaiados:
    
    **Classificação**
    
    **Algoritmos:** Regressão logistica, Árvores de decisão, Florestas aleatórias (randomforest), K-vizinhos mais proximos (KNeighbors/KNN)
    
    **Métricas:** Acurácia, F1 Score,  Precision,  Recall
    
    **Regressão:**
    
    **Algortimos:** Decision Tree, Random Forest, Linear Regression, Knn Regression, Lr lasso, Lr ridge, Lr Elastic Net, Polinomial Regression
    
    **Métricas:** RMSE, MAE, MAPE
    
    **Clusterização:**
    
    **Algoritmos:** KMeans, Affinity Propagation (AP)
    **Métricas:** Silhouette Score, Interia (WCSS)
    

### 3. Desenvolvimento

Para a realização dos ensaios, cada problema/experimento (classificação, regressão, clusterização) segue essencialmente os passos a seguir:

1. Ler o dataset
2. Realizar transformações/normalizações necessárias (alguns algoritmos são sensíveis a escala das features , tornando a normalização essencial para que seu treinamento atendam as premissas da solução) 
3. Definir uma lista de possíveis hiperparametors candidatos do modelo 
4. Treinar o modelo para cada conjunto de hiperparametros definido na etapa anterior
5. Computar as métricas de avaliação do algoritmo. 
6. Escolher o hiperparametro, que melhor perfomou no conjunto de teste. 
7. Avaliar o desempenho do algoritmo para dados de validação. 
8. Aceitar o desempenho de validação como despempenho esperado do algoritmo em produção. 
9. Tirar conclusões do processo de treinamento de cada algoritmo, a partir da variação de seus hiperparametros. 

### 4. Top 5 insigths

1. Regressões polinomiais possuem uma clara correlação entre complexidade e overfitting. Quanto maior a complexidade do algoritmo (grau do polinomio) maior a força do overfitting. 
2. Regularizações em regressões, por simplfiicar o modelo, diminuem a força do overfitting (vide regularizações aplicadas a regressões polinomais de alta complexidade, diminuem seu overffiting) 
3. Random Forest são mais robustas ao overfitting, do que árvores de decisão comuns. 
4. Para classificação e regressão, algoritmos baseados em árvores alcaçaram os melhores desempenhos. 
5. Os erros MAPE e RMSE não seguem sempre a mesma direção de variação (um hiperparametro que minimiza MAPE, pode nao levar ao menor RMSE), pois enquanto o MAPE avalia o valor absoluto (cada amostra predita, tem um peso relativamente “igual” para toda a população, INDEPENDENTE SE SEU VALOR FOR K ou 1000k), o RMSE e MAE penalizam mais erros ABSOLUTOS MAIORES (uma amostra com valor 10000K terá muito mais peso para o RMSE/MAE que a amostra com valor K). O que sugere que, para cada problema, uma das métricas pode ser mais adequada. 

### 5. Resultados
- **Classificação:**
    
    
    | Model | f1_score | precision | **recall** | **accuracy** |
    | --- | --- | --- | --- | --- |
    | RandomForest | 0.959004 | 0.972584 | 0.945799 | 0.964508 |
    | DecisionTree | 0.935900 | 0.945737 | 0.926265 | 0.944309 |
    | KNN | 0.913911 | 0.954493 | 0.876639 | 0.927509 |
    | LogisticRegression | 0.851043 | 0.867978 | 0.834756 | 0.871741 |


- **Regressão:**
    
    
    | modelName | mae | rmse | r2 | mape |  |
    | --- | --- | --- | --- | --- | --- |
    | randomForest | 13.034.856 | 17.720.416 | 0.355078 | 6.543.768 |  |
    | Ridge Polynomial Regression | 16.624.089 | 20.907.118 | 0.102266 | 8.154.727 |  |
    | DecisionTree | 17.009.887 | 21.253.742 | 0.072252 | 7.833.723 |  |
    | Linear Regression | 17.129.965 | 21.480.869 | 0.052317 | 8.521.859 |  |
    | Ridge Linear Regression | 17.130.024 | 21.480.929 | 0.052312 | 8.521.827 |  |
    | Elastic Net Linear Regression | 17.150.640 | 21.512.493 | 0.049525 | 8.533.096 |  |
    | Lasso Linear Regression | 17.213.783 | 21.607.620 | 0.041100 | 8.553.253 |  |


- **Clusterização**
    
    
    | Model Name | Silhouette Score |
    | --- | --- |
    | Affinity Propagation | 0.3 |
    | KMeans | 0.3 |