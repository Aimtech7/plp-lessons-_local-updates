// 🎉 Part 1: Event Handling
document.getElementById("messageBtn").addEventListener("click", function() {
  document.getElementById("message").textContent = "You clicked the button! 🎉";
});

// 🎮 Part 2: Interactive Elements
// 1. Light/Dark mode toggle
const toggleBtn = document.getElementById("toggleTheme");
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

// 2. Counter game
let counter = 0;
document.getElementById("increase").addEventListener("click", () => {
  counter++;
  document.getElementById("counterValue").textContent = counter;
});
document.getElementById("decrease").addEventListener("click", () => {
  counter--;
  document.getElementById("counterValue").textContent = counter;
});

// 3. Collapsible FAQ
const faqQuestions = document.querySelectorAll(".faq-question");
faqQuestions.forEach((question) => {
  question.addEventListener("click", () => {
    const answer = question.nextElementSibling;
    answer.style.display = (answer.style.display === "block") ? "none" : "block";
  });
});

// 📋 Part 3: Form Validation
document.getElementById("signupForm").addEventListener("submit", function(e) {
  e.preventDefault(); // stop form from submitting
  let valid = true;

  // Name validation
  const name = document.getElementById("name").value.trim();
  if (name.length < 3) {
    document.getElementById("nameError").textContent = "Name must be at least 3 characters.";
    valid = false;
  } else {
    document.getElementById("nameError").textContent = "";
  }

  // Email validation (basic regex)
  const email = document.getElementById("email").value.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    document.getElementById("emailError").textContent = "Enter a valid email address.";
    valid = false;
  } else {
    document.getElementById("emailError").textContent = "";
  }

  // Password validation (min 6 chars)
  const password = document.getElementById("password").value;
  if (password.length < 6) {
    document.getElementById("passwordError").textContent = "Password must be at least 6 characters.";
    valid = false;
  } else {
    document.getElementById("passwordError").textContent = "";
  }

  // Success message
  if (valid) {
    document.getElementById("formSuccess").textContent = "🎉 Signup successful!";
    this.reset(); // clear form
  } else {
    document.getElementById("formSuccess").textContent = "";
  }
});
