def solution(genres, plays):
    answer = []
    total_genres = {}
    genre_songs = {}
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        if g not in total_genres:
            total_genres[g] = 0
        if g not in genre_songs:
            genre_songs[g] = []
            
        total_genres[g] += p
        genre_songs[g].append((p,i))
        
        sorted_genres = sorted(total_genres.items(), key = lambda x:x[1], reverse=True)
        
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key = lambda x:(-x[0],x[1]))
        for play, song_id in sorted_songs[:2]:
            answer.append(song_id)
            
    return answer