from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos de películas (simulada)
movies_db = []

# Endpoint para agregar una película
@app.route('/api/new-movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    movie_id = data.get('movieId')
    name = data.get('name')
    genre = data.get('genre')

    if movie_id is None or name is None or genre is None:
        return jsonify({"error": "Campos movieId, name y genre son obligatorios"}), 400

    movie = {
        "movieId": movie_id,
        "name": name,
        "genre": genre
    }
    movies_db.append(movie)

    return jsonify({"message": "Película agregada con éxito"}), 201

# Endpoint para obtener todas las películas por género
@app.route('/api/all-movies-by-genre/<string:genre>', methods=['GET'])
def get_movies_by_genre(genre):
    movies = [movie for movie in movies_db if movie['genre'] == genre]
    return jsonify(movies)

# Endpoint para actualizar una película
@app.route('/api/update-movie', methods=['PUT'])
def update_movie():
    data = request.get_json()
    movie_id = data.get('movieId')
    name = data.get('name')
    genre = data.get('genre')

    if movie_id is None or name is None or genre is None:
        return jsonify({"error": "Campos movieId, name y genre son obligatorios"}), 400

    for movie in movies_db:
        if movie['movieId'] == movie_id:
            movie['name'] = name
            movie['genre'] = genre
            return jsonify({"message": "Película actualizada con éxito"})

    return jsonify({"error": "Película no encontrada"}, 404)

if __name__ == '__main__':
    app.run(debug=True)