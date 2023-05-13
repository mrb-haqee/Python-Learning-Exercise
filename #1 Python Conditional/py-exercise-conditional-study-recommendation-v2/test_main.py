from main import studyRecommendation

class TeststudyRecommendation:
    def test_study_recommendation_not_null(self):
        assert studyRecommendation(0, 0, 0) is not None
        assert studyRecommendation(80, 75, 70) is not None
        assert studyRecommendation(85, 85, 85) is not None
        assert studyRecommendation(80, 75, 85) is not None
        assert studyRecommendation(80, 85, 70) is not None
        assert studyRecommendation(85, 75, 70) is not None
        assert studyRecommendation(85, 85, 70) is not None
        assert studyRecommendation(80, 85, 85) is not None
        assert studyRecommendation(85, 75, 85) is not None
        assert studyRecommendation(85, 85, 85) is not None

    def test_study_recommendation_all_scores_below_min(self):
        assert studyRecommendation(0, 0, 0) == "Maaf, tidak ada rekomendasi yang dapat kami berikan."
        assert studyRecommendation(79, 74, 69) == "Maaf, tidak ada rekomendasi yang dapat kami berikan."
        assert studyRecommendation(79, 74, 50) == "Maaf, tidak ada rekomendasi yang dapat kami berikan."

    def test_study_recommendation_math_scores_above_min(self):
        assert studyRecommendation(80, 75, 70) == "Rekomendasi jurusan yang bisa dipilih: Teknik;Ekonomi;Sastra Inggris;Matematika;Fisika;"
        assert studyRecommendation(80, 75, 50) == "Rekomendasi jurusan yang bisa dipilih: Teknik;Matematika;Fisika;"
        assert studyRecommendation(80, 50, 70) == "Rekomendasi jurusan yang bisa dipilih: Ekonomi;Sastra Inggris;Matematika;"
        assert studyRecommendation(80, 50, 50) == "Rekomendasi jurusan yang bisa dipilih: Matematika;"
        assert studyRecommendation(85, 75, 70) == "Rekomendasi jurusan yang bisa dipilih: Teknik;Ekonomi;Sastra Inggris;Matematika;Fisika;"

    def test_study_recommendation_physic_scores_above_min(self):
        assert studyRecommendation(75, 80, 70) == "Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;Fisika;"
        assert studyRecommendation(75, 80, 50) == "Rekomendasi jurusan yang bisa dipilih: Fisika;"
        assert studyRecommendation(50, 80, 70) == "Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;Fisika;"
        assert studyRecommendation(50, 80, 50) == "Rekomendasi jurusan yang bisa dipilih: Fisika;"

    def test_study_recommendation_english_scores_above_min(self):
        assert studyRecommendation(75, 75, 80) == "Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;Fisika;"
        assert studyRecommendation(75, 50, 80) == "Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;"
        assert studyRecommendation(50, 75, 80) == "Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;Fisika;"
        assert studyRecommendation(50, 50, 80) == "Rekomendasi jurusan yang bisa dipilih: Sastra Inggris;"
