document.addEventListener("DOMContentLoaded", function () {
  const bodyElement = document.querySelector("body");
  if (bodyElement.getAttribute("data-bs-theme") === "auto") {
    function updateTheme() {
      document
        .querySelector("html")
        .setAttribute(
          "data-bs-theme",
          window.matchMedia("(prefers-color-scheme: dark)").matches
            ? "dark"
            : "light"
        );
    }

    window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", updateTheme);

    updateTheme();
  }
});
