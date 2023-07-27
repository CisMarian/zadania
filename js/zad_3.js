function obslugaBledow() {
    let url = "http://costam.com/iksdewhat"

    $.get(url, function(data) {
        $("body").append("<p>Dane pobrane!</p>")
    })
    .fail(function() {
        $("body").append("<p>Wystąpił błąd podczas pobierania danych</p>")
    });
}

obslugaBledow();
