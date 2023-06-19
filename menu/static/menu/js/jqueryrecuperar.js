const form = document.getElementById("formulario");
const correoInput = document.getElementById("correo");
const telefonoInput = document.getElementById("telefono");

form.addEventListener("submit", function(event) {
  // Prevenir que el formulario se envíe
  event.preventDefault();

  // Validar el correo electrónico
  const correoValue = correoInput.value;
  const correoRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
  if (!correoValue || correoValue.indexOf("@") === -1) {
    document.getElementById("correo-error").textContent = "Ingrese un correo electrónico válido";
    return;
  }

  // Validar el número de teléfono
  const telefonoValue = telefonoInput.value;
  const regexTelefono = /^\d{10}$/;
  if (!telefonoValue || telefonoValue.length !== 10) {
    document.getElementById("telefono-error").textContent = "Ingrese un número de teléfono válido (10 dígitos)";
    return;
  }

  // Si todo está correcto, enviar el formulario
  form.submit();
});
