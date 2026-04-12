async function getVisitorCount() {
    // fetch the API counter using URL
    const response = await fetch("https://7j2gfvbtv5.execute-api.ca-west-1.amazonaws.com/count");
    // GET method for the data
    const data = await response.json();
    // Replace the visitor counter with the data
    document.getElementById("visitor_counter").textContent = data.count;
}

getVisitorCount();