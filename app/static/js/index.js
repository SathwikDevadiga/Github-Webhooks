function fetchEvents() {
  fetch('/get_data/events')
    .then(res => res.json())
    .then(data => {
      const div = document.getElementById("events");
      div.innerHTML = "";
      data.forEach(event => {
        div.innerHTML += `<p>${event.message}</p>`;
      });
    })
    .catch(err => console.error("Error loading events:", err));
}

// 🔁 Fetch immediately once
fetchEvents();

// 🔁 Set up interval to fetch events every 15 seconds  
setInterval(fetchEvents, 15000);

