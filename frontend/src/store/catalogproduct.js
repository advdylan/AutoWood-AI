import {defineStore} from 'pinia'
import axios from 'axios'
import { useLink } from 'vue-router';
import { i18n } from '@/locales/i18n';





export const useCatalogProductStore = defineStore('catalogproduct', {
    state: () => ({
               
    }),
    getters: {

        

       


        
    },

    actions: {

        async updateProject(id, editedData) {
            try {
                const response = await axios.patch(`/api/v1/production/catalog-product/${id}/`, editedData, {
                    headers: {
                        'Content-Type': 'application/json',                    
                    },
                });
                //console.log('Server response:', response);
                //console.log('Project updated successfully:', response.data);
            } catch (error) {
                console.error('Error updating the project:', error);
            }
        },
        async downloadElementsTable(id) {
            axios({
                url: `/api/v1/production/elements-production/${id}`,
                method: 'GET',
                responseType: 'blob',
            })
            .then((response) => {
                console.log(response)
                const href = URL.createObjectURL(response.data)

                const link = document.createElement('a')
                link.href = href
                link.setAttribute('download', `rozpiska_produkcja_${id}.pdf`)
                document.body.appendChild(link)
                link.click()

                document.body.removeChild(link)
                URL.revokeObjectURL(href)
                
            })
            .catch(error => {
                console.log("There was an error downloading the file", error)
            }) 
        },
        async downloadPriceReport(id) {
            axios({
                url: `/api/v1/production/pricing-report/${id}`,
                method: 'GET',
                responseType: 'blob',
            })
            .then((response) => {
                console.log(response)
                const href = URL.createObjectURL(response.data)

                const link = document.createElement('a')
                link.href = href
                link.setAttribute('download', `raport_wycena_${id}.pdf`)
                document.body.appendChild(link)
                link.click()

                document.body.removeChild(link)
                URL.revokeObjectURL(href)
                
            })
            .catch(error => {
                console.log("There was an error downloading the file", error)
            }) 
        },


        

        
    },
})