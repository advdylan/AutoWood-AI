import { createApp } from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import App from './App.vue'
import router from './router'
import { pinia } from '@/store'
import { createI18n } from 'vue-i18n';
import pl from './locales/pl.json';
import en from './locales/en.json';

import axios from 'axios'



axios.defaults.baseURL = "https://autowood.fly.dev"
//axios.defaults.baseURL = "https://autowood.onrender.com/"
//axios.defaults.baseURL = "http://127.0.0.1:8000"

const i18n = createI18n({
    locale: 'pl',
    fallbackLocale: 'en',
    messages: {pl, en}
})


const app = createApp(App)

app.use(Buefy, {
    defaultIconPack: 'fa'
})
app.use(pinia)
app.use(router)
app.use(i18n)
app.mount('#app')



