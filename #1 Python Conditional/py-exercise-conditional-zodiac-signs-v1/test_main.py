from main import zodiacSign

class TestzodiacSign:
    def test_not_null(self):
        assert zodiacSign(1, 'Januari') is not None
        assert zodiacSign(1, 'Februari') is not None
        assert zodiacSign(1, 'Maret') is not None
        assert zodiacSign(1, 'April') is not None
        assert zodiacSign(1, 'Mei') is not None
        assert zodiacSign(1, 'Juni') is not None
        assert zodiacSign(1, 'Juli') is not None
        assert zodiacSign(1, 'Agustus') is not None
        assert zodiacSign(1, 'September') is not None
        assert zodiacSign(1, 'Oktober') is not None
        assert zodiacSign(1, 'November') is not None
        assert zodiacSign(1, 'Desember') is not None


    def test_invalid_date(self):
        assert zodiacSign(0, 'Januari') == 'Input tanggal salah'
        assert zodiacSign(32, 'Januari') == 'Input tanggal salah'
        assert zodiacSign(1, 'Januari') != 'Input tanggal salah'

        assert zodiacSign(0, 'Februari') == 'Input tanggal salah'
        assert zodiacSign(30, 'Februari') == 'Input tanggal salah'
        assert zodiacSign(1, 'Februari') != 'Input tanggal salah'
        assert zodiacSign(29, 'Februari') != 'Input tanggal salah'


    def test_invalid_month(self):
        assert zodiacSign(1, "Januari") != "Nama bulan salah"
        assert zodiacSign(1, "Februari") != "Nama bulan salah"
        assert zodiacSign(1, "Maret") != "Nama bulan salah"
        assert zodiacSign(1, "April") != "Nama bulan salah"
        assert zodiacSign(1, "Mei") != "Nama bulan salah"
        assert zodiacSign(1, "Juni") != "Nama bulan salah"
        assert zodiacSign(1, "Juli") != "Nama bulan salah"
        assert zodiacSign(1, "Agustus") != "Nama bulan salah"
        assert zodiacSign(1, "September") != "Nama bulan salah"
        assert zodiacSign(1, "Oktober") != "Nama bulan salah"
        assert zodiacSign(1, "November") != "Nama bulan salah"
        assert zodiacSign(1, "Desember") != "Nama bulan salah"

        assert zodiacSign(1, "januari") == "Nama bulan salah"
        assert zodiacSign(1, "februari") == "Nama bulan salah"
        assert zodiacSign(1, "maret") == "Nama bulan salah"
        assert zodiacSign(1, "april") == "Nama bulan salah"
        assert zodiacSign(1, "mei") == "Nama bulan salah"
        assert zodiacSign(1, "juni") == "Nama bulan salah"
        assert zodiacSign(1, "juli") == "Nama bulan salah"
        assert zodiacSign(1, "agustus") == "Nama bulan salah"
        assert zodiacSign(1, "september") == "Nama bulan salah"
        assert zodiacSign(1, "oktober") == "Nama bulan salah"
        assert zodiacSign(1, "november") == "Nama bulan salah"
        assert zodiacSign(1, "desember") == "Nama bulan salah"

        assert zodiacSign(1, "Jan") == "Nama bulan salah"
        assert zodiacSign(1, "Feb") == "Nama bulan salah"
        assert zodiacSign(1, "Mar") == "Nama bulan salah"
        assert zodiacSign(1, "Apr") == "Nama bulan salah"
        assert zodiacSign(1, "Mei123") == "Nama bulan salah"
        assert zodiacSign(1, "Jun") == "Nama bulan salah"
        assert zodiacSign(1, "Jul") == "Nama bulan salah"
        assert zodiacSign(1, "Agu") == "Nama bulan salah"
        assert zodiacSign(1, "Sep") == "Nama bulan salah"
        assert zodiacSign(1, "Okt") == "Nama bulan salah"
        assert zodiacSign(1, "Nov") == "Nama bulan salah"
        assert zodiacSign(1, "Des") == "Nama bulan salah"

        assert zodiacSign(1, "Januari123") == "Nama bulan salah"
        assert zodiacSign(1, "Februari123") == "Nama bulan salah"
        assert zodiacSign(1, "Maret123") == "Nama bulan salah"
        assert zodiacSign(1, "April123") == "Nama bulan salah"
        assert zodiacSign(1, "Mei123") == "Nama bulan salah"


    def test_capricorn(self):
        # January 1-19
        assert zodiacSign(1, "Januari") == "Capricorn"
        assert zodiacSign(12, "Januari") == "Capricorn"
        assert zodiacSign(19, "Januari") == "Capricorn"

        # December 22-31
        assert zodiacSign(22, "Desember") == "Capricorn"
        assert zodiacSign(30, "Desember") == "Capricorn"


    def test_aquarius(self):
        # January 20-31
        assert zodiacSign(20, "Januari") == "Aquarius"
        assert zodiacSign(31, "Januari") == "Aquarius"

        # February 1-18
        assert zodiacSign(1, "Februari") == "Aquarius"
        assert zodiacSign(18, "Februari") == "Aquarius"


    def test_pisces(self):
        # February 19-29
        assert zodiacSign(19, "Februari") == "Pisces"
        assert zodiacSign(29, "Februari") == "Pisces"

        # Maret 1-20
        assert zodiacSign(1, "Maret") == "Pisces"
        assert zodiacSign(20, "Maret") == "Pisces"


    def test_aries(self):
        assert zodiacSign(21, "Maret") == "Aries"
        assert zodiacSign(31, "Maret") == "Aries"

        assert zodiacSign(1, "April") == "Aries"
        assert zodiacSign(19, "April") == "Aries"


    def test_taurus(self):
        assert zodiacSign(20, "April") == "Taurus"
        assert zodiacSign(30, "April") == "Taurus"

        assert zodiacSign(1, "Mei") == "Taurus"
        assert zodiacSign(20, "Mei") == "Taurus"


    def test_gemini(self):
        assert zodiacSign(21, "Mei") == "Gemini"
        assert zodiacSign(31, "Mei") == "Gemini"

        assert zodiacSign(1, "Juni") == "Gemini"
        assert zodiacSign(20, "Juni") == "Gemini"


    def test_cancer(self):
        assert zodiacSign(21, "Juni") == "Cancer"
        assert zodiacSign(30, "Juni") == "Cancer"

        assert zodiacSign(1, "Juli") == "Cancer"
        assert zodiacSign(22, "Juli") == "Cancer"


    def test_leo(self):
        assert zodiacSign(23, "Juli") == "Leo"
        assert zodiacSign(31, "Juli") == "Leo"

        assert zodiacSign(1, "Agustus") == "Leo"
        assert zodiacSign(22, "Agustus") == "Leo"


    def test_virgo(self):
        # month is August and date in range 23 - 31
        assert zodiacSign(23, "Agustus") == "Virgo"
        assert zodiacSign(31, "Agustus") == "Virgo"
        # month is September and date in range 1 - 22
        assert zodiacSign(1, "September") == "Virgo"
        assert zodiacSign(22, "September") == "Virgo"

    def test_libra(self):
        # month is September and date in range 23 - 30
        assert zodiacSign(23, "September") == "Libra"
        assert zodiacSign(30, "September") == "Libra"
        # month is October and date in range 1 - 22
        assert zodiacSign(1, "Oktober") == "Libra"
        assert zodiacSign(22, "Oktober") == "Libra"

    def test_scorpio(self):
        # month is October and date in range 23 - 31
        assert zodiacSign(23, "Oktober") == "Scorpio"
        assert zodiacSign(31, "Oktober") == "Scorpio"
        # month is November and date in range 1 - 21
        assert zodiacSign(1, "November") == "Scorpio"
        assert zodiacSign(21, "November") == "Scorpio"

    def test_sagittarius(self):
        # month is November and date in range 22 - 30
        assert zodiacSign(22, "November") == "Sagittarius"
        assert zodiacSign(30, "November") == "Sagittarius"
        # month is December and date in range 1 - 21
        assert zodiacSign(1, "Desember") == "Sagittarius"
        assert zodiacSign(21, "Desember") == "Sagittarius"
