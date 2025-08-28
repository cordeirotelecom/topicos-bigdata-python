// Main JavaScript file for DataScience Pro website
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initNavigation();
    initSmoothScrolling();
    initTooltips();
    initAnimations();
    
    console.log('DataScience Pro website initialized successfully!');
});

// Navigation functionality
function initNavigation() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Mobile menu toggle
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });
    }
    
    // Tab switching
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetTab = this.getAttribute('data-tab');
            if (targetTab) {
                switchTab(targetTab);
                
                // Update active nav link
                navLinks.forEach(l => l.classList.remove('active'));
                this.classList.add('active');
                
                // Close mobile menu if open
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            }
        });
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        }
    });
}

// Tab switching functionality
function switchTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
        content.classList.remove('active');
    });
    
    // Show target tab
    const targetTab = document.getElementById(tabName);
    if (targetTab) {
        targetTab.classList.add('active');
        
        // Scroll to top of page
        window.scrollTo({ top: 0, behavior: 'smooth' });
        
        // Initialize tab-specific functionality
        if (tabName === 'ferramenta') {
            initAnalysisTool();
        }
    }
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Skip if it's a tab link (handled by navigation)
            if (this.hasAttribute('data-tab')) {
                return;
            }
            
            const targetElement = document.querySelector(href);
            if (targetElement) {
                e.preventDefault();
                
                const offsetTop = targetElement.offsetTop - 100; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Initialize tooltips
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            showTooltip(this, this.getAttribute('data-tooltip'));
        });
        
        element.addEventListener('mouseleave', function() {
            hideTooltip();
        });
    });
}

// Show tooltip
function showTooltip(element, text) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = text;
    tooltip.id = 'custom-tooltip';
    
    document.body.appendChild(tooltip);
    
    const rect = element.getBoundingClientRect();
    tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
    tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
    
    setTimeout(() => {
        tooltip.classList.add('show');
    }, 10);
}

// Hide tooltip
function hideTooltip() {
    const tooltip = document.getElementById('custom-tooltip');
    if (tooltip) {
        tooltip.remove();
    }
}

// Initialize animations
function initAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.content-section, .concept-card, .step-card, .technique-card, .model-card');
    animateElements.forEach(el => {
        observer.observe(el);
    });
}

// Initialize analysis tool (called when switching to ferramenta tab)
function initAnalysisTool() {
    if (typeof window.analysisToolInitialized === 'undefined') {
        // This will be implemented in analysis-tool.js
        if (typeof initializeAnalysisTool === 'function') {
            initializeAnalysisTool();
            window.analysisToolInitialized = true;
        }
    }
}

// Utility functions
const Utils = {
    // Format numbers with thousands separator
    formatNumber: function(num) {
        return new Intl.NumberFormat('pt-BR').format(num);
    },
    
    // Format file size
    formatFileSize: function(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    },
    
    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Get file extension
    getFileExtension: function(filename) {
        return filename.slice((filename.lastIndexOf(".") - 1 >>> 0) + 2);
    },
    
    // Check if value is numeric
    isNumeric: function(value) {
        return !isNaN(parseFloat(value)) && isFinite(value);
    },
    
    // Calculate statistics
    calculateStats: function(data) {
        const numericData = data.filter(val => this.isNumeric(val)).map(val => parseFloat(val));
        
        if (numericData.length === 0) {
            return {
                count: data.length,
                numeric_count: 0,
                mean: null,
                median: null,
                std: null,
                min: null,
                max: null,
                missing: data.filter(val => val === null || val === undefined || val === '').length
            };
        }
        
        const sorted = [...numericData].sort((a, b) => a - b);
        const mean = numericData.reduce((sum, val) => sum + val, 0) / numericData.length;
        const median = sorted.length % 2 === 0 
            ? (sorted[sorted.length / 2 - 1] + sorted[sorted.length / 2]) / 2 
            : sorted[Math.floor(sorted.length / 2)];
        
        const variance = numericData.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / numericData.length;
        const std = Math.sqrt(variance);
        
        return {
            count: data.length,
            numeric_count: numericData.length,
            mean: parseFloat(mean.toFixed(4)),
            median: parseFloat(median.toFixed(4)),
            std: parseFloat(std.toFixed(4)),
            min: Math.min(...numericData),
            max: Math.max(...numericData),
            missing: data.filter(val => val === null || val === undefined || val === '').length
        };
    },
    
    // Detect outliers using IQR method
    detectOutliers: function(data) {
        const numericData = data.filter(val => this.isNumeric(val)).map(val => parseFloat(val));
        
        if (numericData.length < 4) return [];
        
        const sorted = [...numericData].sort((a, b) => a - b);
        const q1Index = Math.floor(sorted.length * 0.25);
        const q3Index = Math.floor(sorted.length * 0.75);
        
        const q1 = sorted[q1Index];
        const q3 = sorted[q3Index];
        const iqr = q3 - q1;
        
        const lowerBound = q1 - 1.5 * iqr;
        const upperBound = q3 + 1.5 * iqr;
        
        return numericData.filter(val => val < lowerBound || val > upperBound);
    },
    
    // Calculate correlation between two arrays
    calculateCorrelation: function(x, y) {
        if (x.length !== y.length || x.length === 0) return null;
        
        const xNumeric = x.filter((val, i) => this.isNumeric(val) && this.isNumeric(y[i])).map(val => parseFloat(val));
        const yNumeric = y.filter((val, i) => this.isNumeric(x[i]) && this.isNumeric(val)).map(val => parseFloat(val));
        
        if (xNumeric.length < 2) return null;
        
        const xMean = xNumeric.reduce((sum, val) => sum + val, 0) / xNumeric.length;
        const yMean = yNumeric.reduce((sum, val) => sum + val, 0) / yNumeric.length;
        
        let numerator = 0;
        let xSumSquares = 0;
        let ySumSquares = 0;
        
        for (let i = 0; i < xNumeric.length; i++) {
            const xDiff = xNumeric[i] - xMean;
            const yDiff = yNumeric[i] - yMean;
            
            numerator += xDiff * yDiff;
            xSumSquares += xDiff * xDiff;
            ySumSquares += yDiff * yDiff;
        }
        
        const denominator = Math.sqrt(xSumSquares * ySumSquares);
        
        if (denominator === 0) return null;
        
        return numerator / denominator;
    },
    
    // Generate color palette
    generateColorPalette: function(count) {
        const colors = [
            '#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6',
            '#06b6d4', '#84cc16', '#f97316', '#ec4899', '#6366f1',
            '#14b8a6', '#eab308', '#dc2626', '#9333ea', '#0891b2'
        ];
        
        const palette = [];
        for (let i = 0; i < count; i++) {
            palette.push(colors[i % colors.length]);
        }
        
        return palette;
    },
    
    // Download file
    downloadFile: function(content, filename, contentType = 'text/plain') {
        const blob = new Blob([content], { type: contentType });
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
    },
    
    // Show notification
    showNotification: function(message, type = 'info', duration = 5000) {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span class="notification-message">${message}</span>
                <button class="notification-close">&times;</button>
            </div>
        `;
        
        // Add styles
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#22c55e' : type === 'error' ? '#ef4444' : type === 'warning' ? '#f59e0b' : '#2563eb'};
            color: white;
            padding: 16px 20px;
            border-radius: 8px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            z-index: 10000;
            max-width: 400px;
            animation: slideInRight 0.3s ease-out;
        `;
        
        document.body.appendChild(notification);
        
        // Close button functionality
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notification.remove();
        });
        
        // Auto remove
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.animation = 'slideOutRight 0.3s ease-in';
                setTimeout(() => notification.remove(), 300);
            }
        }, duration);
    }
};

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .notification-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
        padding: 0;
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        transition: background-color 0.2s;
    }
    
    .notification-close:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
    
    .tooltip {
        position: absolute;
        background-color: var(--bg-dark);
        color: white;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 14px;
        z-index: 10000;
        opacity: 0;
        transition: opacity 0.2s;
        pointer-events: none;
        white-space: nowrap;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .tooltip.show {
        opacity: 1;
    }
    
    .tooltip::after {
        content: '';
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        border: 5px solid transparent;
        border-top-color: var(--bg-dark);
    }
    
    .animate-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;

document.head.appendChild(style);

// Export utilities for global use
window.Utils = Utils;
