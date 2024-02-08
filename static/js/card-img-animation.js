//изменение кнопки "в корзину"
// document.querySelectorAll(".btn.btn-success.cards__btn").forEach((button) => {
//   button.addEventListener("click", (event) => {
//     event.preventDefault();
//     const basketTitle = event.target.parentElement.querySelector(
//       ".cards__basket-title"
//     );
//     const basketText = basketTitle.textContent;
//
//     basketTitle.textContent = "супер!";
//
//     setTimeout(() => {
//       basketTitle.textContent = basketText;
//     }, 1000);
//   });
// });

//счетчик
// const incrementButton = document.querySelector(
//   ".big-card__green.big-card__max"
// );
// const decrementButton = document.querySelector(".big-card__dark.big-card__max");
// const counterDisplay = document.querySelector(".big-card__number");
//
// let counterValue = parseInt(counterDisplay.value, 10);
//
// function incrementCounter() {
//   if (counterValue < 25) {
//     counterValue++;
//     counterDisplay.value = counterValue;
//   }
// }
//
// function decrementCounter() {
//   if (counterValue > 1) {
//     counterValue--;
//     counterDisplay.value = counterValue;
//   }
// }
//
// incrementButton.addEventListener("click", incrementCounter);
// decrementButton.addEventListener("click", decrementCounter);

document.querySelectorAll(".big-card__card-block").forEach(function (card) {
  card.addEventListener("mousemove", function (e) {
    let rect = card.getBoundingClientRect();
    let x = e.clientX - rect.left;
    let y = e.clientY - rect.top;
    card.querySelector(
      ".big-card__img"
    ).style.transformOrigin = `${x}px ${y}px`;
  });
});

    var docWidth = document.documentElement.offsetWidth;
    [].forEach.call(document.querySelectorAll("*"), function (el) {
      if (el.offsetWidth > docWidth) {
        console.log(el);
      }
    });