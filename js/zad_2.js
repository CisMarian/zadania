function wyswietlanieKomunikatu() {
    let url = "http://costam.com/iksdewhat"

    $.get(url, function(data) {
        $("body").append("<p>Dane pobrane!</p>")
    });
}

wyswietlanieKomunikatu();
