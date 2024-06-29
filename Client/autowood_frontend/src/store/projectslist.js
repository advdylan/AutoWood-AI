import {defineStore} from 'pinia'
import axios from 'axios'



export const useProjectsListStore = defineStore('projectslist', {
    state: () => ({
        projectlist: null,
        detail_project: null,

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
                elements: item.elements.name,
                nawigacja: 'nawigacja'
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
                },
                {
                field: 'nawigacja',
                laber: 'nawigacja'
                }
            ]
            return columns
        }
    },

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
                console.log(response.data)   
                this.setProjects(response.data)
            })
            .catch(error =>{
                console.log(error)     
            })
        },

        async loadDetailProject(id) {
            await axios
            .get(`/api/v1/newproject/${id}/`)
            .then(response => {
                console.log(response.data)
                this.setDetaiLProject(response.data)
            })
            .catch(error => {
                console.log(error)
            })

        }
    },
    
})