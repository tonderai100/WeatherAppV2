document.addEventListener("DOMContentLoaded", function() {
   document.getElementById("weatherForm").addEventListener("submit", function(event) {
      event.preventDefault();
      const location = document.getElementById("LocationInput").value;

      fetch("/get_weather?location=" + location)
         .then(response => response.json())
         .then(data => {
            displayWeather(data);
         })
         .catch(error => {
            console.error("Error:", error);
         });
   });
});

function displayWeather(weather) {
   const weatherDataElement = document.getElementById("weatherData");
   weatherDataElement.innerHTML = `
      <h2>Current Weather Conditions</h2>
      <p>Temperature: ${weather.temperature}°C</p>
      <p>Humidity: ${weather.humidity}%</p>
      <p>Wind Speed: ${weather.wind_speed} km/h</p>
      <p>Conditions: ${weather.conditions}</p>
   `;
}
