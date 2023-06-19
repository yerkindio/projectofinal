const form = document.getElementById("formulario");
const nombreInput = document.getElementById("Nombre");
const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirm-password");

form.addEventListener("submit", function(event) {
  // Prevenir que el formulario se envíe
  event.preventDefault();

  // Validar el nombre de usuario
  const nombreValue = nombreInput.value;
  if (!nombreValue || nombreValue.includes(" ")) {
    document.getElementById("Nombre-error").textContent = "El nombre de usuario debe contener caracteres y no puede incluir espacios";
    return;
  }
  // Validar la contraseña
  const passwordValue = passwordInput.value;
	const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%])[0-9a-zA-Z@#$%]{6,}$/;
	if (!passwordValue || passwordValue.length < 6) {
  	document.getElementById("password-error").textContent = "La contraseña debe tener al menos 6 caracteres";
  	return;
	}
	if (!/(?=.*[@#$%])/.test(passwordValue)) {
  	document.getElementById("password-error").textContent = "La contraseña debe tener al menos un carácter especial (@#$%)";
  	return;
	}
	if (!/(?=.*[A-Z])/.test(passwordValue)) {
  	document.getElementById("password-error").textContent = "La contraseña debe tener al menos una letra mayúscula";
  	return;
	}

  // Validar la confirmación de contraseña
  const confirmPasswordValue = confirmPasswordInput.value;
  if (!confirmPasswordValue || confirmPasswordValue !== passwordValue) {
    document.getElementById("confirm-password-error").textContent = "Las contraseñas no coinciden";
    return;
  }

    // Si todo está correcto, enviar el formulario
    form.submit();
});
