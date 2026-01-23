from app.db import get_db



def create_category(nome: str):
    """Crea una nuova categoria."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO categoria (nome) VALUES (?)", (nome,)
    )
    db.commit()
    return cursor.lastrowid

def get_all_categories():
    """Recupera tutte le categorie."""
    db = get_db()
    categories = db.execute("SELECT * FROM categoria").fetchall()
    return categories