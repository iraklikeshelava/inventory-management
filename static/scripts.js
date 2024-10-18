// Fetch inventory data and update the DOM
function fetchInventory() {
    fetch('/api/inventory')
        .then(response => response.json())
        .then(data => {
            const inventoryList = document.getElementById('inventory-list');
            inventoryList.innerHTML = '';  // Clear existing list
            data.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = `ID: ${item[0]}, Name: ${item[1]}, Quantity: ${item[2]}, Warehouse ID: ${item[3]}`;
                inventoryList.appendChild(listItem);
            });
        });
}

window.onload = fetchInventory;
