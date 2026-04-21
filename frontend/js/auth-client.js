/**
 * @file auth-client.js
 * @description 認證服務前端 SDK，處理 JWT 儲存、API 請求封裝與認證狀態管理。
 */

/**
 * @typedef {Object} AuthOptions
 * @property {string} [baseURL=''] - API 的基礎路徑
 * @property {string} [tokenKey='auth_service_token'] - 儲存在 localStorage 的 Token 鍵名
 * @property {string} [usernameKey='auth_service_username'] - 儲存在 localStorage 的用戶名鍵名
 * @property {string} [loginPage='login.html'] - 登入頁面的路徑
 */

/**
 * 認證服務客戶端類別
 */
export class AuthClient {
    /**
     * 初始化 AuthClient
     * @param {AuthOptions} options - 配置選項
     */
    constructor(options = {}) {
        this.baseURL = options.baseURL || '';
        this.tokenKey = options.tokenKey || 'auth_service_token';
        this.usernameKey = options.usernameKey || 'auth_service_username';
        this.loginPage = options.loginPage || 'login.html';
    }

    /**
     * 儲存認證資訊到 localStorage
     * @param {string} token - JWT 存取權杖
     * @param {string} username - 用戶名稱
     */
    saveToken(token, username) {
        localStorage.setItem(this.tokenKey, token);
        localStorage.setItem(this.usernameKey, username);
    }

    /**
     * 獲取當前的 JWT 權杖
     * @returns {string|null}
     */
    getToken() {
        return localStorage.getItem(this.tokenKey);
    }

    /**
     * 獲取當前登入的用戶名
     * @returns {string|null}
     */
    getUsername() {
        return localStorage.getItem(this.usernameKey);
    }

    /**
     * 登出並清除本地認證資訊
     */
    logout() {
        localStorage.removeItem(this.tokenKey);
        localStorage.removeItem(this.usernameKey);
        window.location.href = this.loginPage;
    }

    /**
     * 檢查當前是否已認證
     * @returns {boolean}
     */
    isAuthenticated() {
        return !!this.getToken();
    }

    /**
     * 認證守衛：若未登入則導向登入頁
     */
    checkAuth() {
        if (!this.isAuthenticated() && !window.location.pathname.endsWith(this.loginPage)) {
            window.location.href = this.loginPage;
        }
    }

    /**
     * 具備認證功能的 fetch 封裝
     * @param {string} url - 請求路徑
     * @param {RequestInit} [options={}] - fetch 配置選項
     * @returns {Promise<Response>}
     * @throws {Error} 當認證失效 (401) 時會自動登出並拋出異常
     */
    async fetchWithAuth(url, options = {}) {
        const token = this.getToken();
        const headers = {
            ...options.headers,
        };

        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        const fullURL = url.startsWith('http') ? url : `${this.baseURL}${url}`;
        const response = await fetch(fullURL, { ...options, headers });

        if (response.status === 401) {
            console.warn('Authentication expired, redirecting to login');
            this.logout();
            throw new Error('Unauthorized');
        }

        return response;
    }

    /**
     * 執行登入請求
     * @param {string} username 
     * @param {string} password 
     * @returns {Promise<Object>} 包含 access_token 的物件
     */
    async login(username, password) {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        const response = await fetch(`${this.baseURL}/api/auth/login`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Login failed');
        }

        const data = await response.json();
        this.saveToken(data.access_token, data.username);
        return data;
    }

    /**
     * 執行註冊請求
     * @param {string} username 
     * @param {string} password 
     * @returns {Promise<Object>} 伺服器回傳結果
     */
    async register(username, password) {
        const response = await fetch(`${this.baseURL}/api/auth/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Registration failed');
        }

        return await response.json();
    }
}

/** 預設導出的全域 auth 實例 */
export const auth = new AuthClient();
