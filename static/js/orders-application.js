let socket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/orders/'
);

socket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    let eventType = data.event_type;
    console.log(eventType);
    if (eventType === 'order_update') {
        let orderId = data.order_id;
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
        } else if (statusText === "Готов") {
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
    }
    if (eventType === 'order_create') {
        let orderId = data.order_id;
        let statusText = data.order_status_text;
        let createdAt = new Date(data.created_at);
        let totalSum = data.total_sum;
        let parentElement = document.getElementById("ordersBody");
        let formattedDate = `${createdAt.getDate()} ${getMonthName(createdAt.getMonth())} ${createdAt.getFullYear()} г. ${createdAt.getHours()}:${padZero(createdAt.getMinutes())}`;
        let newRow1 = parentElement.insertRow(0);
        newRow1.id = "order-" + orderId;
        if (statusText === "Создан") {
            newRow1.className = "table-info";
        } else if (statusText === "Подтвержден") {
            newRow1.className = "table-primary";
        } else if (statusText === "В обработке") {
            newRow1.className = "table-warning";
        } else if (statusText === "Готов") {
            newRow1.className = "table-success";
        } else if (statusText === "В пути") {
            newRow1.className = "table-secondary";
        } else if (statusText === "Выдан") {
            newRow1.className = "table-dark";
        } else if (statusText === "Отменен") {
            newRow1.className = "table-danger";
        }
        newRow1.innerHTML = `
            <th scope="row">${orderId}</th>
            <td>${statusText}</td>
            <td>${formattedDate}</td>
            <td>${totalSum} руб.</td>
            <td><a href="/orders/order/${orderId}/" target="_blank">Детали</a></td>
        `;
        let newRow2 = document.createElement("tr");
        newRow2.innerHTML = `
            <td>
                <a href="/managements_orders_app/change_status/${orderId}/1/">Подтвердить</a>
                <a href="/managements_orders_app/change_status/${orderId}/6/">Отменить</a>
            </td>
            <td><a href="/managements_orders_app/change_status/${orderId}/2/">В обработке</a></td>
            <td><a href="/managements_orders_app/change_status/${orderId}/3/">Готов</a></td>
            <td><a href="/managements_orders_app/change_status/${orderId}/4/">В пути</a></td>
            <td><a href="/managements_orders_app/change_status/${orderId}/5/">Выдан</a></td>
        `;
        newRow1.insertAdjacentElement("afterend", newRow2);
        // parentElement.insertBefore(newRow2, newRow);
    }

};
// Функция для получения названия месяца по его номеру
function getMonthName(monthIndex) {
    const months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
    return months[monthIndex];
}

// Функция для добавления ведущего нуля к однозначному числу
function padZero(number) {
    return number < 10 ? '0' + number : number;
}


socket.onopen = function (e) {
    console.log('Connection established');
};

socket.onclose = function (e) {
    console.error('WebSocket closed unexpectedly', e);
};