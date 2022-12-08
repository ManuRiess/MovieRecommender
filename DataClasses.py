class Movie:
    def __init__(self, id, title, r_date, v_date, url, g_list):
        self.id = id
        self.title = title
        self.release_date = r_date
        self.video_release = v_date
        self.url = url
        self.genre_list = g_list

    def get_genres(self):
        genres = []
        genre = ["unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
        for i in range(len(self.genre_list)):
            if  int(self.genre_list[i]):
                genres.append(genre[i])
        return genres

class User:
    def __init__(self, id, age, gender, occ, zip):
        self.id = id
        self.age = age
        self.gender = gender
        self.occupation = occ
        self.postal_code = zip

def importAsDataClasses():
    with open(r'ml-100k\u.data') as ml_100_data:  # ml-100k\u.data
        data_csv = csv.reader(ml_100_data, delimiter='\t')
        ratings = list(data_csv)

    movies = list()
    with open(r'ml-100k\u.item') as movies_data:  # ml-100k\u.data
        movies_csv = csv.reader(movies_data, delimiter='|')
        for row in movies_csv:
            movies.append(
                Movie(id=row[0], title=row[1], r_date=row[2], v_date=row[3], url=str(row[4]), g_list=row[5:24]))
    print(f"Sanity check:\nThe movie {movies[0].title} contains the genres: {movies[0].get_genres()}")

    users = list()
    with open(r'ml-100k\u.user') as users_data:  # ml-100k\u.data
        users_csv = csv.reader(users_data, delimiter='|')
        for row in users_csv:
            users.append(User(id=row[0], age=row[1], gender=row[2], occ=row[3], zip=row[4]))
    print(
        f"Sanity check:\nThe user 111 ({users[110].gender} {users[110].age}) works as {users[110].occupation} - ID: {users[110].id}")