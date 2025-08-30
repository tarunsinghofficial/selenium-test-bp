// show error message
function showError(msg) {
  const err = document.getElementById("error");
  err.textContent = msg;
  err.hidden = false;
}

// clear error message
function clearError() {
  const err = document.getElementById("error");
  err.textContent = "";
  err.hidden = true;
}

// handle login form submission
function handleLogin(e) {
  e.preventDefault();
  clearError();
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  if (username === "admin" && password === "admin123") {
    // fake delay to mimic server response
    setTimeout(() => (window.location.href = "dashboard.html"), 350);
    return false;
  }

  showError("Invalid credentials!");
  return false;
}
