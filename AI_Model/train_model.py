import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Dataset d'exemple avec des caractéristiques fictives (email_length, num_links, has_attachment)
data = np.array([
    [100, 2, 1, 1],
    [50, 1, 0, 0],
    [200, 5, 1, 1],
    [70, 1, 1, 0],
    [300, 6, 1, 1]
])

# Labels (1 = succès, 0 = échec)
labels = np.array([1, 0, 1, 0, 1])

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Création du modèle de Random Forest
model = RandomForestClassifier(n_estimators=10)
model.fit(X_train, y_train)

# Prédiction et évaluation du modèle
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Sauvegarde du modèle
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)
