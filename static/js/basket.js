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
                console.log('Success');
                let successMessage = $("#jq-notification");
                successMessage.html('<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                                    '<strong>Success!</strong> ' + data.message +
                                    '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                                    '<span aria-hidden="true">&times;</span>' +
                                    '</button>' +
                                    '</div>');
            },
            error: function(xhr, errmsg, err) {
            alert('Произошла ошибка: ' + xhr.status + ': ' + xhr.responseText);
            },
        });
    });
});