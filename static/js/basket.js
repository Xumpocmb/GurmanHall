$(document).ready(function () {
    $('.big-card__form').submit(function(event) {
        event.preventDefault();
        let form = $(this);
        let url = form.attr('action');
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'form': form.serialize(),
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            dataType: 'json',
            success: function (data) {
                console.log('Success:', data);
            },
            error: function(xhr, errmsg, err) {
            alert('Произошла ошибка: ' + xhr.status + ': ' + xhr.responseText);
            },
        });
    });
});