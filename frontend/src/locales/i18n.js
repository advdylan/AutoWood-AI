import { createI18n } from 'vue-i18n';
import pl from '@/locales/pl.json' ;
import en from '@/locales/en.json' ;

 

const instance = createI18n({
    locale: 'pl',
    fallbackLocale: 'en',
    messages: {pl, en}
})
export default instance;

export const i18n = instance.global
