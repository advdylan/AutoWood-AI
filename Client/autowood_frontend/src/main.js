import { createApp } from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'; // Import Buefy first
import './styles/buefy-customs.scss'; // Then your custom styles
import App from './App.vue'
import router from './router'
import { pinia } from '@/store'
import { createI18n } from 'vue-i18n';
import i18nInstance from '@/locales/i18n.js'
import 'animate.css';

import i18n from './locales/i18n' ;

import axios from 'axios'



//axios.defaults.baseURL = "https://autowood.fly.dev"
//axios.defaults.baseURL = "https://autowood.onrender.com/"
axios.defaults.baseURL = "http://127.0.0.1:8000"


const app = createApp(App)

app.use(Buefy, {
    defaultIconPack: 'fa',
    customTheme: true
})
app.use(pinia)
app.use(router)
app.use(i18nInstance)
app.mount('#app')



