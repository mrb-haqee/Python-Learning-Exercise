def studyRecommendation(mathScore: int, physicsScore: int, englishScore: int) -> str:
    result = "Rekomendasi jurusan yang bisa dipilih: "

    if mathScore >= 85 and physicsScore >= 85 and englishScore >= 85:
        result += "Teknik Informatika;"
    if mathScore >= 80 and physicsScore >= 75:
        result += "Teknik;"
    if mathScore >= 80 and englishScore >= 70:
        result += "Ekonomi;"
    if englishScore >= 70:
        result += "Sastra Inggris;"
    if mathScore >= 80:
        result += "Matematika;"
    if physicsScore >= 75:
        result += "Fisika;"
    if mathScore < 80 and physicsScore < 75 and englishScore < 70:
        return "Maaf, tidak ada rekomendasi yang dapat kami berikan."
    return result  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    # expected Output => Maaf, tidak ada rekomendasi yang dapat kami berikan.
    print(studyRecommendation(0, 0, 0))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Ekonomi;Sastra Inggris;Matematika;
    print(studyRecommendation(80, 70, 70))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Teknik;Matematika;Fisika;
    print(studyRecommendation(80, 75, 60))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;Fisika;
    print(studyRecommendation(60, 85, 85))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Teknik;Ekonomi;Sastra Inggris;Matematika;Fisika;
    print(studyRecommendation(80, 85, 70))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Ekonomi;Sastra Inggris;Matematika;
    print(studyRecommendation(85, 70, 70))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;Fisika;
    print(studyRecommendation(64, 90, 85))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Fisika;
    print(studyRecommendation(40, 85, 60))
    # expected Output => Rekomendasi jurusan yang bisa dipilih: Teknik Informatika;Teknik;Ekonomi;Sastra Inggris;Matematika;Fisika;
    print(studyRecommendation(85, 85, 85))
