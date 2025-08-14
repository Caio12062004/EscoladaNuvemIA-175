from sklearn.datasets import load_breast_cancer # Conjunto de dados de CA de mama
from sklearn.ensemble import RandomForestClassifier # Algoritmo Random Forest

# Métricas para avaliação do modelo
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# Função papra divisão do conjunto de dados
from sklearn.model_selection import train_test_split


# Carregando o dataset de CA de mama
data = load_breast_cancer()

x_train, x_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

#inicializar o conjunto Random Forest com os parâmetros
model = RandomForestClassifier(random_state=42)

# Treinar o modelo com os dados de treino
model.fit(x_train, y_train)

# Fazer as previsões com os dados de teste
y_pred = model.predict(x_test) # Previsões de classe (0 ou 1) (maligno ou benigno)
y_pred_proba = model.predict_proba(x_test)[:,1] # Probabilidade de classe positiva (1) (benigno)

#Calcular as métricas para avaliação:
precision = precision_score(y_test, y_pred) # Precisão = TP / (TP + FP)
recall = recall_score(y_test, y_pred) # Recall = TP / (TP + FN)
f1 = f1_score(y_test, y_pred) # F1-Score = 2 * [(Precisão * Recall) / (Precisão + Recall)]
auc = roc_auc_score(y_test, y_pred_proba) # Área

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"AUC-ROC: {auc:.4f}")