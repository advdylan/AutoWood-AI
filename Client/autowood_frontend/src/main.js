import { createApp } from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import App from './App.vue'
import router from './router'
import { pinia } from '@/store'

import axios from 'axios'




//axios.defaults.baseURL = "https://autowood.onrender.com/"
axios.defaults.baseURL = "http://localhost:8080/"


const app = createApp(App)

app.use(Buefy, {
    defaultIconPack: 'fa'
})
app.use(pinia)
app.use(router)
app.mount('#app')



