window.onload = function () {
  var messages = document.querySelectorAll("#messages .message");
  messages.forEach(function (messageElement) {
    showToast(messageElement.textContent);
  });
};

function showToast(message) {
  var toast = document.getElementById("toast");
  var toastMessage = document.getElementById("toastMessage");

  toastMessage.textContent = message;
  toast.classList.remove("hidden");

  setTimeout(function () {
    toast.classList.add("hidden");
  }, 3000);
}
document
  .getElementById("toggleFormButton")
  .addEventListener("click", function () {
    var form = document.getElementById("addTaskForm");
    form.style.display = form.style.display === "none" ? "flex" : "none";
  });

window.addEventListener("click", function (event) {
  var form = document.getElementById("addTaskForm");
  if (event.target == form) {
    form.style.display = "none";
  }
});
