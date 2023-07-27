function pobieranieDanychRownolegle() {
    let url = [
        "http://costam.com/iksdewhat1",
        "http://costam.com/iksdewhat2",
        "http://costam.com/iksdewhat3"
    ];

    $.when(
        $.get(url[0]),
        $.get(url[1]),
        $.get(url[2])
    ).done(function(data1, data2, data3) {
        console.log("Pierwsze żądanie", data1[0]);
        console.log("Drugie żądanie", data2[0]);
        console.log("Trzecie żądanie", data3[0]);
    });
}

pobieranieDanychRownolegle();
