import { createApp } from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import App from './App.vue'
import router from './router'
import { pinia } from '@/store'

import axios from 'axios'




axios.defaults.baseURL = "http://127.0.0.1:8000"


const app = createApp(App)

app.use(Buefy, {
    defaultIconPack: 'fa'
})
app.use(pinia)
app.use(router)
app.mount('#app')



