function getResponseFromAPI() {
  return new Promise((resolve) => {
    // Aquí puedes realizar cualquier operación asíncrona, como una solicitud a una API.
    // Por ahora, simplemente resolveremos la promesa después de un pequeño retraso.

    setTimeout(() => {
      resolve('Response from API');
    }, 1000); // Simulamos un retraso de 1 segundo
  });
}

export default getResponseFromAPI;
