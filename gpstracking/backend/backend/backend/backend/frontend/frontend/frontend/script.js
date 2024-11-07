async function fetchLocations() {
    try {
        const response = await fetch('http://localhost:5000/api/locations');
        const data = await response.json();
        console.log(data); // Placeholder for map integration
    } catch (error) {
        console.error('Error fetching GPS locations:', error);
    }
}
