import {defineStore} from 'pinia'
import axios from 'axios'
import { useLink } from 'vue-router';
import { i18n } from '@/locales/i18n';





export const useProjectsListStore = defineStore('projectslist', {
    state: () => ({
        projectlist: null,
        detail_project: null,
        catalog_product: null,
        isLoading: true
       
        
    }),
    getters: {

        data() {
            return this.projectlist ? this.projectlist.map(item => ({
                id: item.id,
                name: item.name,
                category: item.category.name,
                collection: item.collection.name,
                wood: item.wood.name,
                paints: item.paints.name,
                elements: item.elements,
                nawigacja: 'nawigacja'
            })) : [];
        },

        catalog_product_data() {
            return this.catalog_product ? this.catalog_product.map(item => ({
                id: item.id,
                name: item.name,
                
                category: item.category.name,
                collection: item.collection.name,
                wood: item.wood.name,
                paints: item.paints.name,
                elements: item.elements,
                production_stages: item.production_stages,
                nawigacja: 'nawigacja'
            })) : [];

        },


        
        columns() {         
            let columns = [
                { 
                field: 'name', 
                label: i18n.t('name'),
                searchable: true,
                width: '250',
                },
                { 
                field: 'category', 
                label: i18n.t('category'),
                searchable: true,
   
                },
                { 
                field: 'collection', 
                label: i18n.t('collection'),
                searchable: true,
              
                },
                { 
                field: 'wood', 
                label: i18n.t('wood_type'),
                searchable: true,
                width: '130',

              
                },
                { 
                field: 'paints',
                label: i18n.t('paints'),
                searchable: true,
                
               
                },
                {
                field: 'nawigacja',
                label: i18n.t('Nav'),
            
                }
            ]
            return columns
        }
    },

/*     linkFiles(){
        for (let img of this.detail_project.image){
            return 0
        } */

    

    actions: {

        

        setProjects(data) {
            this.projectlist = data

        },

        setDetaiLProject(data) {
            this.detail_project = data
        },

        

        async loadProjects() {
            await axios
            .get(`/api/v1/newproject`)
            .then(response => {       
                this.setProjects(response.data)
                this.isLoading = false;
            })
            .catch(error =>{
                console.log(error)     
            })
        },

        async loadCatalog() {
            await axios
            .get(`/api/v1/production/catalog-product`)
            .then(response => {
                console.log(response.data)       
                this.catalog_product = response.data
                this.isLoading = false;
            })
            .catch(error =>{
                console.log(error)     
            })
        },

        async loadDetailProject(id) {
        
            await axios
            .get(`/api/v1/newproject/${id}/`)
            .then(response => {
                this.setDetaiLProject(response.data)
                console.log(`Project DETAIL ID:${id} \n`, response.data)
            })

        },

        async loadCatalogProductDetail(id) {
            await axios
            .get(`/api/v1/production/catalog-product/${id}/`)
            .then(response => {
                this.setDetaiLProject(response.data)
                console.log(`catalogProduct ID:${id} \n`, response.data)
            })

        },
        async updateProject(id, editedData) {
            try {
                const response = await axios.patch(`/api/v1/newproject/${id}/`, editedData, {
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
                url: `/api/v1/newproject/elements-production/${id}`,
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
                url: `/api/v1/newproject/pricing-report/${id}`,
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

        async addNewProjectToProduction(data) {

            console.log(data)

            await axios
            .post(`/api/v1/production/add-newproject-to-production/`, data , {
                headers: {
                  'Content-Type': 'application/json'
                }
              }) 
            .then((response) => {
                console.log(`Response : ${response}`)
            })
            .catch(error => {
                console.log(error)
            })
        },

        async addCatalogProductToProduction(data) {

            await axios
            .post(`/api/v1/production/add-catalogproduct-to-production/`, data , {
                headers: {
                  'Content-Type': 'application/json'
                }
              }) 
            .then((response) => {
                console.log(`Response : ${response}`)
            })
            .catch(error => {
                console.log(error)
            })

        },

        addElement(element) {
            this.detail_project.elements.push({
              element: {
                name: element.element.name,
                dimX: element.element.dimX,
                dimY: element.element.dimY,
                dimZ: element.element.dimZ,
                wood_type: element.element.wood_type
              },
              quantity: element.quantity
            });
            console.log(this.element)
          },

        addAccesoryDetailProject(accesory) {
                
                const newAccesory = {
                    id: accesory.id,
                    project: this.detail_project.id,
                    quantity: accesory.quantity,
                    type: {
                        description: accesory.description,
                        id: accesory.id,
                        name: accesory.name,
                        price: accesory.price,
                        type: accesory.type,
                        weight: accesory.weight
                    }
                }
                this.detail_project.accessories.push(newAccesory)
            },
        
        setLoading() {
            this.isLoading = true;
        }
    },
})