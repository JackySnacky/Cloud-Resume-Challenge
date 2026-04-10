visitorCounterNumber = 0;

async function getVisitorCount() {
    // fetch the API counter using URL
    const response = await fetch("https://9ym09kowqa.execute-api.ca-west-1.amazonaws.com/count");
    // GET method for the data
    const data = await response.json();
    // prints the data to console for debugging
    console.log(data);
    visitorCounterNumber = data;
}

console.log(visitorCounterNumber)

getVisitorCount();