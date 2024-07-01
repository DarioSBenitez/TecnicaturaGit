document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Formulario enviado!');
        // Aquí puedes agregar funcionalidad adicional para manejar el envío del formulario
    });
});
