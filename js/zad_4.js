function pobieranieDanychSekwencyjne() {
    let url = [
        "http://costam.com/iksdewhat1",
        "http://costam.com/iksdewhat2",
        "http://costam.com/iksdewhat3"
    ]

    $.get(url[0], function(data1) {
        console.log("Pierwsze żądanie", data1);

        $.get(url[1], function(data2) {
            console.log("Drugie żądanie", data2);

            $.get(url[2], function(data3) {
                console.log("Trzecie żądanie", data3);
            });
        });
    });
}

pobieranieDanychSekwencyjne();
