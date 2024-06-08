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
                { field: 'name', label: 'Name' },
                { field: 'category', label: 'Category' },
                { field: 'collection', label: 'Collection' },
                { field: 'wood', label: 'Wood' },
                { field: 'paints', label: 'Paints' }
            ];
            return columns;
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