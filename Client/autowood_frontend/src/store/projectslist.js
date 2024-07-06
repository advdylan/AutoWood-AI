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
                label: 'Nazwa',
                searchable: true
                },
                { 
                field: 'category', 
                label: 'Kategoria',
                searchable: true 
                },
                { 
                field: 'collection', 
                label: 'Kolekcja',
                searchable: true
                },
                { 
                field: 'wood', 
                label: 'Materiał',
                searchable: true 
                },
                { 
                field: 'paints',
                label: 'Malowanie',
                searchable: true 
                },
                {
                field: 'nawigacja',
                label: 'Nawigacja'
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
                this.setDetaiLProject(response.data)
            })
            .catch(error => {
                console.log(error)
            })

        }
    },
    
})