import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al archivo JSON de credenciales
cred = credentials.Certificate("credentials/amancayahouse-f9bde-firebase-adminsdk-fbsvc-3b7f08b12b.json")

# Inicializar la aplicación de Firebase
firebase_admin.initialize_app(cred)

# Obtener una instancia de Firestore
db = firestore.client()

def add_user(name, age, email):
    doc_ref = db.collection("users").document()
    doc_ref.set({
        "name": name,
        "age": age,
        "email": email
    })
    print(f"Usuario agregado con ID: {doc_ref.id}")

# Función para obtener todos los usuarios
def get_users():
    users_ref = db.collection("users")
    docs = users_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

# Ejemplo de uso
def update_user(user_id, new_data):
    user_ref = db.collection("users").document(user_id)
    user_ref.update(new_data)
    print(f"Usuario {user_id} actualizado")

# Ejemplo de uso
#update_user("1FSzKnTOe6GgoSfiwYWo", {"age": 90})  # Cambia la edad del usuario
def delete_user(user_id):
    db.collection("users").document(user_id).delete()
    print(f"Usuario {user_id} eliminado")

# Ejemplo de uso
#delete_user("jLmH2jstOBde9SW6MaGZ")

