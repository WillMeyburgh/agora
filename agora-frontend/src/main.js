import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia' // Re-add createPinia import
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia()) // Uncomment createPinia
app.use(router) // Uncomment router

app.mount('#app')
