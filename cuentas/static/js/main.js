function handleLogout() {
    localStorage.removeItem("authToken");
    window.location.href = "/home";
  }
  