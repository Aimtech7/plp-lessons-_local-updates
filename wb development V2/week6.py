import os, zipfile

# Project folder name
project_name = "interactive_web_assignment"
os.makedirs(project_name, exist_ok=True)

# Files and contents
files = {
    "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Web Assignment</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>🌟 Welcome to My Interactive Page!</h1>

  <!-- 🎮 Part 1: Event Handling -->
  <button id="messageBtn">Click Me!</button>
  <p id="message"></p>

  <!-- 🎮 Part 2: Interactive Elements -->
  <section>
    <h2>Light/Dark Mode Toggle</h2>
    <button id="toggleTheme">Toggle Theme</button>
  </section>

  <section>
    <h2>Counter Game</h2>
    <button id="increase">+ Increase</button>
    <button id="decrease">- Decrease</button>
    <p>Counter: <span id="counterValue">0</span></p>
  </section>

  <section>
    <h2>FAQ (Collapsible)</h2>
    <div class="faq-item">
      <h3 class="faq-question">What is JavaScript?</h3>
      <p class="faq-answer">JavaScript is the language that makes websites interactive!</p>
    </div>
    <div class="faq-item">
      <h3 class="faq-question">Why learn it?</h3>
      <p class="faq-answer">Because it’s fun, powerful, and everywhere on the web. 🚀</p>
    </div>
  </section>

  <!-- 📋 Part 3: Form Validation -->
  <section>
    <h2>Signup Form</h2>
    <form id="signupForm">
      <label>Name: <input type="text" id="name"></label><br>
      <small class="error" id="nameError"></small><br>

      <label>Email: <input type="text" id="email"></label><br>
      <small class="error" id="emailError"></small><br>

      <label>Password: <input type="password" id="password"></label><br>
      <small class="error" id="passwordError"></small><br>

      <button type="submit">Submit</button>
    </form>
    <p id="formSuccess"></p>
  </section>

  <script src="script.js"></script>
</body>
</html>
""",
    "style.css": """body {
  font-family: Arial, sans-serif;
  padding: 20px;
  transition: background 0.3s, color 0.3s;
}

.dark-mode {
  background: #121212;
  color: #f1f1f1;
}

button {
  margin: 5px;
  padding: 10px;
  cursor: pointer;
}

.faq-answer {
  display: none;
  margin: 5px 0;
}

.error {
  color: red;
  font-size: 12px;
}
""",
    "script.js": """// 🎉 Part 1: Event Handling
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
  const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
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
"""
}

# Write files
for filename, content in files.items():
    with open(os.path.join(project_name, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Zip them
zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for filename in files:
        zipf.write(os.path.join(project_name, filename), filename)

print(f"ZIP file created: {zip_filename}")
