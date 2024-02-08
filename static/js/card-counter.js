$(document).ready(function () {
    let currentValueElement = $("#counter_value");
    let priceElement = $(".big-card__price");
    let currentPrice = parseFloat(priceElement.text().replace(',', '.'));

    // обрабатываю событие клика по кнопкам + и -
    $(document).on("click", ".big-card__green", function (e) {
        e.preventDefault();
        let currentValue = parseInt(currentValueElement.val(), 10);
        if (currentValue < 10) {
            currentValue++;
        }
        currentValueElement.val(currentValue)
        let newPrice = (currentPrice * currentValue).toFixed(2);
        priceElement.html("<ins>" + newPrice.replace('.', ',') + "р." + "</ins>");
    });
    $(document).on("click", ".big-card__dark", function (e) {
        e.preventDefault();
        let currentValue = parseInt(currentValueElement.val(), 10);
        if (currentValue > 1) {
            currentValue--;
        }
        currentValueElement.val(currentValue)
        let newPrice = (currentPrice * currentValue).toFixed(2);
        priceElement.html("<ins>" + newPrice.replace('.', ',') + "р." + "</ins>");
    });
})