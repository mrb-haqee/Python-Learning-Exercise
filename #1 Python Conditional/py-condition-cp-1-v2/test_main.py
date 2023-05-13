from main import GraduateStudent
class TestGraduateStudent:
    def test_score_more_than_equal_70_and_absent_less_than_5(self):
        assert GraduateStudent(70, 4) == "lulus"
        assert GraduateStudent(80, 1) == "lulus"
        assert GraduateStudent(70, 1) == "lulus"
        
    def test_score_more_than_90_and_absent_0(self):
        assert GraduateStudent(90, 0) == "lulus"
        assert GraduateStudent(95, 0) == "lulus"
        assert GraduateStudent(100, 0) == "lulus"
        
    def test_score_less_than_70(self):
        assert GraduateStudent(69, 4) == "tidak lulus"
        assert GraduateStudent(40, 1) == "tidak lulus"
        assert GraduateStudent(69, 6) == "tidak lulus"
        
    def test_absent_more_than_equal_5(self):
        assert GraduateStudent(70, 10) == "tidak lulus"
        assert GraduateStudent(100, 5) == "tidak lulus"
        assert GraduateStudent(80, 6) == "tidak lulus"
        
    def test_score_0_and_absent_0(self):
        assert GraduateStudent(0, 0) == "tidak lulus"
        
    def test_score_0_and_absent_more_than_5(self):
        assert GraduateStudent(0, 6) == "tidak lulus"
        assert GraduateStudent(0, 7) == "tidak lulus"
        assert GraduateStudent(0, 8) == "tidak lulus"
