/**
 * POKER CHIP CALCULATOR - FRONTEND JAVASCRIPT
 * Handles user interactions and API communication
 */

// ============================================================================
// STATE MANAGEMENT
// ============================================================================

const API_BASE_URL = '';  // Empty means same origin (Flask serves this)

// Check if user has premium access
function isPremium() {
    return localStorage.getItem('isPremium') === 'true';
}

// ============================================================================
// SCREEN NAVIGATION
// ============================================================================

function showScreen(screenId) {
    // Hide all screens
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });

    // Show requested screen
    const screen = document.getElementById(screenId);
    if (screen) {
        screen.classList.add('active');
        window.scrollTo(0, 0);
    }
}

function selectMode(mode) {
    if (mode === 'auto') {
        showScreen('auto-screen');
    } else if (mode === 'custom') {
        // Check premium status first
        if (!isPremium()) {
            showScreen('custom-screen');
            document.getElementById('premium-lock').style.display = 'block';
            document.getElementById('custom-form').style.display = 'none';
            return;
        }

        // Premium user - check if they have chipsets
        const chipsets = getChipsets();
        if (chipsets.length === 0) {
            // First time premium user - go directly to create chipset
            showChipsetCreate();
        } else {
            // Has chipsets - show selection screen
            showChipsetSelect();
        }
    }
}

function backToModeSelection() {
    showScreen('mode-selection');
    // Clear any previous results
    document.getElementById('results-content').style.display = 'none';
    document.getElementById('error').style.display = 'none';
}

// ============================================================================
// CHIPSET MANAGEMENT
// ============================================================================

let currentChipsetId = null;  // Track currently selected/editing chipset

// Get all chipsets from localStorage
function getChipsets() {
    const data = localStorage.getItem('chipsets');
    return data ? JSON.parse(data) : [];
}

// Save chipsets to localStorage
function saveChipsets(chipsets) {
    localStorage.setItem('chipsets', JSON.stringify(chipsets));
}

// Get chipset by ID
function getChipsetById(id) {
    const chipsets = getChipsets();
    return chipsets.find(cs => cs.id === id);
}

// Show chipset selection screen
function showChipsetSelect() {
    showScreen('chipset-select-screen');
    renderChipsetList();
}

// Show chipset create screen
function showChipsetCreate(chipsetId = null) {
    showScreen('chipset-create-screen');
    currentChipsetId = chipsetId;

    if (chipsetId) {
        // Edit mode
        document.getElementById('chipset-create-title').textContent = 'Edit Chip Set';
        const chipset = getChipsetById(chipsetId);
        if (chipset) {
            document.getElementById('chipset-name').value = chipset.name;
            document.getElementById('set-default-chipset').checked = chipset.isDefault || false;
            renderDenominations(chipset.chips);
        }
    } else {
        // Create mode
        document.getElementById('chipset-create-title').textContent = 'Create Chip Set';
        document.getElementById('chipset-name').value = '';
        document.getElementById('set-default-chipset').checked = false;
        renderDenominations();
    }
}

// Back to chipset selection
function backToChipsetSelect() {
    const chipsets = getChipsets();
    if (chipsets.length === 0) {
        backToModeSelection();
    } else {
        showChipsetSelect();
    }
}

// Render chipset list
function renderChipsetList() {
    const chipsets = getChipsets();
    const container = document.getElementById('chipset-list');
    const useBtn = document.getElementById('use-chipset-btn');

    if (chipsets.length === 0) {
        container.innerHTML = '<p class="helper-text">No chip sets saved yet. Create your first one!</p>';
        useBtn.disabled = true;
        return;
    }

    let html = '<div class="chipset-cards">';
    chipsets.forEach(chipset => {
        const totalChips = Object.values(chipset.chips).reduce((sum, count) => sum + count, 0);
        const totalValue = Object.entries(chipset.chips)
            .reduce((sum, [denom, count]) => sum + (parseInt(denom) * count), 0);

        html += `
            <div class="chipset-card" data-chipset-id="${chipset.id}">
                <input type="radio" name="selected-chipset" value="${chipset.id}"
                       id="chipset-${chipset.id}" onchange="onChipsetSelected()">
                <label for="chipset-${chipset.id}">
                    <div class="chipset-header">
                        <strong>${chipset.name}</strong>
                        ${chipset.isDefault ? '<span class="badge-default">Default</span>' : ''}
                    </div>
                    <div class="chipset-details">
                        <span>${Object.keys(chipset.chips).length} denominations</span>
                        <span>${totalChips} chips</span>
                        <span>$${totalValue.toLocaleString()} total</span>
                    </div>
                    <div class="chipset-actions">
                        <button type="button" class="btn-small" onclick="event.stopPropagation(); showChipsetCreate('${chipset.id}')">
                            Edit
                        </button>
                        <button type="button" class="btn-small btn-danger" onclick="event.stopPropagation(); deleteChipset('${chipset.id}')">
                            Delete
                        </button>
                    </div>
                </label>
            </div>
        `;
    });
    html += '</div>';

    container.innerHTML = html;

    // Auto-select default chipset
    const defaultChipset = chipsets.find(cs => cs.isDefault);
    if (defaultChipset) {
        document.getElementById(`chipset-${defaultChipset.id}`).checked = true;
        useBtn.disabled = false;
    }
}

// When user selects a chipset
function onChipsetSelected() {
    document.getElementById('use-chipset-btn').disabled = false;
}

// Use selected chipset (proceed to custom form)
function useSelectedChipset() {
    const selected = document.querySelector('input[name="selected-chipset"]:checked');
    if (!selected) {
        alert('Please select a chip set');
        return;
    }

    currentChipsetId = selected.value;
    showScreen('custom-screen');
    document.getElementById('premium-lock').style.display = 'none';
    document.getElementById('custom-form').style.display = 'block';
}

// Render denomination inputs
function renderDenominations(chips = null) {
    const container = document.getElementById('chip-denominations');

    if (!chips) {
        // Default starting denominations
        chips = { '1': 300, '5': 200, '25': 200, '100': 200, '500': 50, '1000': 50 };
    }

    let html = '';
    Object.entries(chips).forEach(([denom, count]) => {
        html += createDenominationRow(denom, count);
    });

    container.innerHTML = html;
}

// Create single denomination row HTML
function createDenominationRow(denom = '', count = 0) {
    const id = Math.random().toString(36).substr(2, 9);
    return `
        <div class="denomination-row" data-row-id="${id}">
            <input type="number" class="denom-value" placeholder="Denomination"
                   value="${denom}" min="1" required>
            <input type="number" class="denom-count" placeholder="Quantity"
                   value="${count}" min="0" required>
            <button type="button" class="btn-small btn-danger" onclick="removeDenomination('${id}')">
                Remove
            </button>
        </div>
    `;
}

// Add new denomination row
function addDenomination() {
    const container = document.getElementById('chip-denominations');
    container.insertAdjacentHTML('beforeend', createDenominationRow());
}

// Remove denomination row
function removeDenomination(rowId) {
    const row = document.querySelector(`[data-row-id="${rowId}"]`);
    if (row) {
        row.remove();
    }
}

// Delete chipset
function deleteChipset(chipsetId) {
    if (!confirm('Are you sure you want to delete this chip set?')) {
        return;
    }

    let chipsets = getChipsets();
    chipsets = chipsets.filter(cs => cs.id !== chipsetId);
    saveChipsets(chipsets);

    if (chipsets.length === 0) {
        backToModeSelection();
    } else {
        renderChipsetList();
    }
}

// ============================================================================
// PREMIUM/LICENSE MANAGEMENT
// ============================================================================

function showUnlockDialog() {
    document.getElementById('unlock-dialog').classList.add('active');
}

function closeUnlockDialog() {
    document.getElementById('unlock-dialog').classList.remove('active');
}

async function activateLicense() {
    const licenseKey = document.getElementById('license-key-input').value.trim();

    if (!licenseKey) {
        alert('Please enter a license key');
        return;
    }

    // Show loading
    const button = event.target;
    button.disabled = true;
    button.textContent = 'Verifying...';

    try {
        // Try to verify as Entry Tier first
        const response = await fetch(`${API_BASE_URL}/api/verify-license`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                license_key: licenseKey,
                product_id: 'entry'
            })
        });

        const data = await response.json();

        if (data.success && data.valid) {
            // License is valid!
            localStorage.setItem('isPremium', 'true');
            localStorage.setItem('licenseKey', licenseKey);
            localStorage.setItem('productTier', data.product_tier);
            localStorage.setItem('purchaseEmail', data.purchase_email || '');

            // Show success message
            alert(`✅ License activated successfully!\n\nProduct: ${data.product_name || 'Entry Tier'}\nEmail: ${data.purchase_email || 'N/A'}`);

            // Close dialog
            closeUnlockDialog();

            // Refresh premium status
            checkPremiumStatus();
        } else {
            // Try Premium tier
            const premiumResponse = await fetch(`${API_BASE_URL}/api/verify-license`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    license_key: licenseKey,
                    product_id: 'premium'
                })
            });

            const premiumData = await premiumResponse.json();

            if (premiumData.success && premiumData.valid) {
                // Premium license is valid!
                localStorage.setItem('isPremium', 'true');
                localStorage.setItem('licenseKey', licenseKey);
                localStorage.setItem('productTier', premiumData.product_tier);
                localStorage.setItem('purchaseEmail', premiumData.purchase_email || '');

                // Show success message
                alert(`✅ Premium license activated successfully!\n\nProduct: ${premiumData.product_name || 'Premium Upgrade'}\nEmail: ${premiumData.purchase_email || 'N/A'}`);

                // Close dialog
                closeUnlockDialog();

                // Refresh premium status
                checkPremiumStatus();
            } else {
                // Invalid license for both tiers
                alert(`❌ Invalid license key\n\n${data.error || premiumData.error || 'Please check your key and try again.'}`);
            }
        }
    } catch (error) {
        alert(`❌ Error verifying license\n\n${error.message}\n\nPlease check your internet connection and try again.`);
    } finally {
        button.disabled = false;
        button.textContent = 'Activate';
    }
}

// ============================================================================
// API CALLS
// ============================================================================

async function calculateAuto(formData) {
    const response = await fetch(`${API_BASE_URL}/api/calculate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num_players: parseInt(formData.players),
            small_blind: parseFloat(formData.small_blind),
            big_blind: parseFloat(formData.big_blind),
            duration_hours: parseFloat(formData.duration),
            minutes_per_level: parseInt(formData.minutes)
        })
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Calculation failed');
    }

    return await response.json();
}

async function calculateCustom(formData) {
    const response = await fetch(`${API_BASE_URL}/api/calculate-custom`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num_players: parseInt(formData.players),
            small_blind: parseFloat(formData.small_blind),
            big_blind: parseFloat(formData.big_blind),
            target_stack: parseFloat(formData.target_stack)
        })
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Calculation failed');
    }

    return await response.json();
}

// ============================================================================
// FORM HANDLERS
// ============================================================================

document.getElementById('auto-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = {
        players: document.getElementById('auto-players').value,
        small_blind: document.getElementById('auto-sb').value,
        big_blind: document.getElementById('auto-bb').value,
        duration: document.getElementById('auto-duration').value,
        minutes: document.getElementById('auto-minutes').value
    };

    // Show results screen with loading
    showScreen('results-screen');
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results-content').style.display = 'none';
    document.getElementById('error').style.display = 'none';

    try {
        // Call API
        const result = await calculateAuto(formData);

        // Hide loading
        document.getElementById('loading').style.display = 'none';

        // Display results
        displayResults(result);

    } catch (error) {
        // Hide loading
        document.getElementById('loading').style.display = 'none';

        // Show error
        const errorBox = document.getElementById('error');
        errorBox.textContent = error.message;
        errorBox.style.display = 'block';
    }
});

document.getElementById('custom-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = {
        players: document.getElementById('custom-players').value,
        small_blind: document.getElementById('custom-sb').value,
        big_blind: document.getElementById('custom-bb').value,
        target_stack: document.getElementById('custom-stack').value
    };

    // Add selected chipset to API call
    if (currentChipsetId) {
        const chipset = getChipsetById(currentChipsetId);
        if (chipset) {
            formData.chip_set = chipset.chips;
        }
    }

    // Show results screen with loading
    showScreen('results-screen');
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results-content').style.display = 'none';
    document.getElementById('error').style.display = 'none';

    try {
        // Call API
        const result = await calculateCustom(formData);

        // Hide loading
        document.getElementById('loading').style.display = 'none';

        // Display results
        displayResults(result);

    } catch (error) {
        // Hide loading
        document.getElementById('loading').style.display = 'none';

        // Show error
        const errorBox = document.getElementById('error');
        errorBox.textContent = error.message;
        errorBox.style.display = 'block';
    }
});

// Chipset form handler
document.getElementById('chipset-form')?.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('chipset-name').value.trim();
    const setDefault = document.getElementById('set-default-chipset').checked;

    if (!name) {
        alert('Please enter a chip set name');
        return;
    }

    // Collect chips from denomination rows
    const chips = {};
    const rows = document.querySelectorAll('.denomination-row');

    for (const row of rows) {
        const denom = parseInt(row.querySelector('.denom-value').value);
        const count = parseInt(row.querySelector('.denom-count').value);

        if (!denom || denom < 1) {
            alert('Please enter valid denomination values (must be at least 1)');
            return;
        }

        if (count < 0) {
            alert('Chip quantities cannot be negative');
            return;
        }

        if (chips[denom]) {
            alert(`Duplicate denomination: $${denom}. Each denomination can only appear once.`);
            return;
        }

        chips[denom] = count;
    }

    if (Object.keys(chips).length === 0) {
        alert('Please add at least one chip denomination');
        return;
    }

    // Get existing chipsets
    let chipsets = getChipsets();

    if (currentChipsetId) {
        // Edit existing chipset
        const index = chipsets.findIndex(cs => cs.id === currentChipsetId);
        if (index !== -1) {
            chipsets[index] = {
                ...chipsets[index],
                name,
                chips,
                isDefault: setDefault
            };
        }
    } else {
        // Create new chipset
        const newChipset = {
            id: `chipset-${Date.now()}`,
            name,
            chips,
            isDefault: setDefault,
            createdAt: new Date().toISOString().split('T')[0]
        };
        chipsets.push(newChipset);
    }

    // If setting as default, unset all others
    if (setDefault) {
        chipsets.forEach(cs => {
            if (cs.id !== currentChipsetId) {
                cs.isDefault = false;
            }
        });
    }

    // Save chipsets
    saveChipsets(chipsets);

    // Navigate back to selection
    alert(`Chip set "${name}" saved successfully!`);
    showChipsetSelect();
});

// ============================================================================
// RESULTS DISPLAY
// ============================================================================

function displayResults(result) {
    // Show results container
    document.getElementById('results-content').style.display = 'block';

    // Display stack summary
    document.getElementById('result-stack').textContent = `$${result.stack_value.toLocaleString()}`;
    document.getElementById('result-bb').textContent = `${result.big_blinds.toFixed(1)} BB`;

    // Show auto-adjust notice if applicable
    const adjustNotice = document.getElementById('adjust-notice');
    if (result.stack_was_adjusted) {
        const maxStack = result.max_stack_per_player;
        adjustNotice.querySelector('#adjust-message').textContent =
            `Stack optimized to fit your chip set (max available: $${Math.floor(maxStack).toLocaleString()} per player)`;
        adjustNotice.style.display = 'block';
    } else {
        adjustNotice.style.display = 'none';
    }

    // Build distribution table
    const table = document.getElementById('distribution-breakdown');
    table.innerHTML = '';

    let totalChips = 0;
    let totalValue = 0;

    // Sort denominations from smallest to largest
    const sortedDenoms = Object.keys(result.distribution)
        .map(d => parseFloat(d))
        .sort((a, b) => a - b);

    sortedDenoms.forEach(denom => {
        const count = result.distribution[denom];
        const value = denom * count;
        totalChips += count;
        totalValue += value;

        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="chip-denom">$${formatDenom(denom)}</td>
            <td class="chip-count">${count} chips</td>
            <td class="chip-value">$${value.toLocaleString()}</td>
        `;
        table.appendChild(row);
    });

    // Add total row
    const totalRow = document.createElement('tr');
    totalRow.innerHTML = `
        <td>TOTAL</td>
        <td class="chip-count">${totalChips} chips</td>
        <td class="chip-value">$${totalValue.toLocaleString()}</td>
    `;
    table.appendChild(totalRow);
}

function formatDenom(denom) {
    // If whole number, display without decimals
    if (denom === Math.floor(denom)) {
        return denom.toString();
    }
    // Otherwise show with decimals
    return denom.toFixed(2).replace(/\.?0+$/, '');
}

// ============================================================================
// INITIALIZATION
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('Poker Chip Calculator loaded');

    // Check if premium is already activated
    if (isPremium()) {
        console.log('Premium features unlocked');
    }

    // Show mode selection screen by default
    showScreen('mode-selection');

    // Register service worker for PWA functionality
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/service-worker.js')
            .then((registration) => {
                console.log('[PWA] Service Worker registered:', registration);
            })
            .catch((error) => {
                console.log('[PWA] Service Worker registration failed:', error);
            });
    }
});

// Close modal when clicking outside
document.getElementById('unlock-dialog')?.addEventListener('click', (e) => {
    if (e.target.id === 'unlock-dialog') {
        closeUnlockDialog();
    }
});
