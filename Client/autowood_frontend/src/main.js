import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { pinia } from '@/store'

import axios from 'axios'




axios.defaults.baseURL = "http://127.0.0.1:8000"


const app = createApp(App)


app.use(pinia)
app.use(router)
app.mount('#app')



