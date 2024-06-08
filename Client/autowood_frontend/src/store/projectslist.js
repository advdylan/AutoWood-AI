import {defineStore} from 'pinia'
import axios from 'axios'



export const useProjectsListStore = defineStore('projectslist', {
    state: () => ({
        projectlist: null,

    }),
    getters: {
        data() {
            return this.projectlist ? this.projectlist.map(item => ({
                name: item.name,
                category: item.category.name,
                collection: item.collection.name,
                wood: item.wood.name,
                paints: item.paints.name
            })) : [];
        },

        columns() {
            let columns = [
                { 
                field: 'name', 
                label: 'Name',
                searchable: true
                },
                { 
                field: 'category', 
                label: 'Category',
                searchable: true 
                },
                { 
                field: 'collection', 
                label: 'Collection',
                searchable: true
                },
                { 
                field: 'wood', 
                label: 'Wood',
                searchable: true 
                },
                { 
                field: 'paints',
                label: 'Paints',
                searchable: true 
                }
            ]
            return columns
        }
    },

    actions: {

        setProjects(data) {
            this.projectlist = data

        },

        async loadProjects() {
            await axios
            .get(`/api/v1/newproject`)
            .then(response => {
                this.setProjects(response.data)
            })
            .catch(error =>{
                console.log(error)     
            })
        }
    },
    
})