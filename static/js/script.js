document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const productName = document.getElementById('productName').value.trim();
    const searchBtn = document.getElementById('searchBtn');
    const searchBtnText = document.getElementById('searchBtnText');
    const searchBtnSpinner = document.getElementById('searchBtnSpinner');
    const resultsSection = document.getElementById('resultsSection');
    const errorSection = document.getElementById('errorSection');
    const bestDealSection = document.getElementById('bestDealSection');
    
    searchBtn.disabled = true;
    searchBtnText.classList.add('d-none');
    searchBtnSpinner.classList.remove('d-none');
    resultsSection.classList.add('d-none');
    errorSection.classList.add('d-none');
    bestDealSection.classList.add('d-none');
    
    try {
        const response = await fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ product_name: productName })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Search failed');
        }
        
        const data = await response.json();
        displayResults(data);
        
    } catch (error) {
        document.getElementById('errorText').textContent = error.message;
        errorSection.classList.remove('d-none');
    } finally {
        searchBtn.disabled = false;
        searchBtnText.classList.remove('d-none');
        searchBtnSpinner.classList.add('d-none');
    }
});

function displayResults(data) {
    const queryText = document.getElementById('queryText');
    const resultsTableBody = document.getElementById('resultsTableBody');
    const resultsSection = document.getElementById('resultsSection');
    const bestDealSection = document.getElementById('bestDealSection');
    const bestDealText = document.getElementById('bestDealText');
    
    queryText.textContent = data.query;
    resultsTableBody.innerHTML = '';
    
    const platformBadges = {
        'Zepto': 'badge-zepto',
        'Blinkit': 'badge-blinkit',
        'BigBasket': 'badge-bigbasket',
        'JioMart': 'badge-jiomart',
        'Swiggy Instamart': 'badge-swiggy'
    };
    
    let bestDealPlatform = null;
    
    data.platforms.forEach(platform => {
        const row = document.createElement('tr');
        
        if (platform.is_best_deal && platform.available) {
            row.classList.add('best-deal-row');
            bestDealPlatform = platform;
        }
        
        const platformBadgeClass = platformBadges[platform.platform] || 'bg-secondary';
        
        row.innerHTML = `
            <td>
                <span class="platform-badge ${platformBadgeClass}">${platform.platform}</span>
                ${platform.is_best_deal && platform.available ? '<br><span class="best-deal-badge mt-1">BEST DEAL</span>' : ''}
            </td>
            <td>${platform.product_name}</td>
            <td class="fw-bold">${platform.price}</td>
            <td>
                ${platform.available 
                    ? '<span class="available">✓ Available</span>' 
                    : `<span class="not-available">✗ ${platform.error || 'Not Available'}</span>`
                }
            </td>
            <td>
                ${platform.url && platform.available 
                    ? `<a href="${platform.url}" target="_blank" class="btn btn-sm btn-outline-primary">View</a>` 
                    : '-'
                }
            </td>
        `;
        
        resultsTableBody.appendChild(row);
    });
    
    if (bestDealPlatform) {
        bestDealText.textContent = `${bestDealPlatform.platform} offers the best price at ${bestDealPlatform.price}!`;
        bestDealSection.classList.remove('d-none');
    }
    
    resultsSection.classList.remove('d-none');
}
