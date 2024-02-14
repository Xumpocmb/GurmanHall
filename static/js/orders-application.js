let socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/orders/'
);

socket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    let orderId = data.order_id;
    let status = data.order_status;
    let statusText = data.order_status_text;
    let createdAt = new Date(data.created_at);
    let totalSum = data.total_sum;
    let order_tr = document.getElementById("order-" + data.order_id);
    if (statusText === "Создан") {
        order_tr.className = "table-info";
    } else if (statusText === "Подтвержден") {
        order_tr.className = "table-primary";
    } else if (statusText === "В обработке") {
        order_tr.className = "table-warning";
    }
    if (statusText === "Готов") {
        order_tr.className = "table-success";
    } else if (statusText === "В пути") {
        order_tr.className = "table-secondary";
    } else if (statusText === "Выдан") {
        order_tr.className = "table-dark";
    } else if (statusText === "Отменен") {
        order_tr.className = "table-danger";
    }
    let formattedDate = `${createdAt.getDate()} ${getMonthName(createdAt.getMonth())} ${createdAt.getFullYear()} г. ${createdAt.getHours()}:${padZero(createdAt.getMinutes())}`;
    order_tr.innerHTML = `
            <th scope="row">${orderId}</th>
            <td>${statusText}</td>
            <td>${formattedDate}</td>
            <td>${totalSum} руб.</td>
            <td><a href="/orders/order/${orderId}/" target="_blank">Детали</a></td>
            `;

    // Функция для получения названия месяца по его номеру
    function getMonthName(monthIndex) {
        const months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
        return months[monthIndex];
    }

    // Функция для добавления ведущего нуля к однозначному числу
    function padZero(number) {
        return number < 10 ? '0' + number : number;
    }
};

socket.onopen = function (e) {
    console.log('Connection established');
};

socket.onclose = function (e) {
    console.error('WebSocket closed unexpectedly', e);
};