// Language Switcher Module
class LanguageSwitcher {
    constructor() {
        this.currentLanguage = this.getStoredLanguage() || 'es';
        this.init();
    }

    // Get stored language from localStorage
    getStoredLanguage() {
        return localStorage.getItem('preferredLanguage');
    }

    // Save language to localStorage
    saveLanguage(lang) {
        localStorage.setItem('preferredLanguage', lang);
    }

    // Initialize language on page load
    init() {
        this.applyLanguage(this.currentLanguage);
        this.updateLanguageButton();
    }

    // Toggle between Spanish and English
    toggleLanguage() {
        this.currentLanguage = this.currentLanguage === 'es' ? 'en' : 'es';
        this.saveLanguage(this.currentLanguage);
        this.applyLanguage(this.currentLanguage);
        this.updateLanguageButton();
    }

    // Apply language to all elements with data-i18n attribute
    applyLanguage(lang) {
        // Update all elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            if (translations[key] && translations[key][lang]) {
                element.textContent = translations[key][lang];
            }
        });

        // Update placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
            const key = element.getAttribute('data-i18n-placeholder');
            if (translations[key] && translations[key][lang]) {
                element.placeholder = translations[key][lang];
            }
        });

        // Update title attributes
        document.querySelectorAll('[data-i18n-title]').forEach(element => {
            const key = element.getAttribute('data-i18n-title');
            if (translations[key] && translations[key][lang]) {
                element.title = translations[key][lang];
            }
        });

        // Update alt attributes for images
        document.querySelectorAll('[data-i18n-alt]').forEach(element => {
            const key = element.getAttribute('data-i18n-alt');
            if (translations[key] && translations[key][lang]) {
                element.alt = translations[key][lang];
            }
        });

        // Update value attributes (for inputs)
        document.querySelectorAll('[data-i18n-value]').forEach(element => {
            const key = element.getAttribute('data-i18n-value');
            if (translations[key] && translations[key][lang]) {
                element.value = translations[key][lang];
            }
        });

        // Update page title if it exists
        const titleElement = document.querySelector('title[data-i18n]');
        if (titleElement) {
            const key = titleElement.getAttribute('data-i18n');
            if (translations[key] && translations[key][lang]) {
                document.title = translations[key][lang];
            }
        }

        // Update meta description if it exists
        const metaDesc = document.querySelector('meta[name="description"][data-i18n]');
        if (metaDesc) {
            const key = metaDesc.getAttribute('data-i18n');
            if (translations[key] && translations[key][lang]) {
                metaDesc.content = translations[key][lang];
            }
        }

        // Update html lang attribute
        document.documentElement.lang = lang;
    }

    // Update the language button text
    updateLanguageButton() {
        const langButton = document.getElementById('choiceLangBttn');
        if (langButton) {
            langButton.textContent = this.currentLanguage;
        }

        // Also update the language button if it exists as a different element
        const langButtons = document.querySelectorAll('.language-btn, #languageBtn');
        langButtons.forEach(btn => {
            btn.textContent = this.currentLanguage;
        });
    }

    // Get current language
    getCurrentLanguage() {
        return this.currentLanguage;
    }
}

// Initialize language switcher when DOM is ready
let languageSwitcher;

document.addEventListener('DOMContentLoaded', function () {
    // Create language switcher instance
    languageSwitcher = new LanguageSwitcher();

    // Add click event to language button(s)
    const langButton = document.getElementById('choiceLangBttn');
    if (langButton) {
        langButton.style.cursor = 'pointer';
        langButton.addEventListener('click', function (e) {
            e.preventDefault();
            languageSwitcher.toggleLanguage();
        });
    }

    // Support for alternative button selectors
    document.querySelectorAll('.language-btn, #languageBtn').forEach(btn => {
        btn.style.cursor = 'pointer';
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            languageSwitcher.toggleLanguage();
        });
    });

    // Add keyboard accessibility
    if (langButton) {
        langButton.setAttribute('role', 'button');
        langButton.setAttribute('tabindex', '0');
        langButton.addEventListener('keypress', function (e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                languageSwitcher.toggleLanguage();
            }
        });
    }
});
