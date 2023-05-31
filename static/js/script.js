// Mencari elemen yang ingin Anda hilangkan setelah scroll
var elemenYangAkanDihilangkan = document.querySelector(".navbar");

// Mendapatkan posisi scroll saat ini
var posisiScrollAwal = window.pageYOffset || document.documentElement.scrollTop;

// Menambahkan event listener untuk menghilangkan elemen setelah scroll
window.addEventListener("scroll", function() {
    // Mendapatkan posisi scroll saat ini
    var posisiScrollSaatIni = window.pageYOffset || document.documentElement.scrollTop;
    
    // Menghitung perubahan posisi scroll
    var perubahanPosisiScroll = posisiScrollSaatIni - posisiScrollAwal;
    
    // Jika perubahan posisi scroll lebih besar dari 0, maka elemen akan dihilangkan
    if (perubahanPosisiScroll > 0 || posisiScrollSaatIni > 0) {
        elemenYangAkanDihilangkan.style.display = "none";
    }
    // Jika perubahan posisi scroll kurang dari atau sama dengan 0, maka elemen akan ditampilkan kembali
    else {
        elemenYangAkanDihilangkan.style.display = "flex";
    }
});