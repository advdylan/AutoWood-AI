import {defineStore} from 'pinia'
import axios from 'axios'



export const useProjectsListStore = defineStore('projectslist', {
    state: () => ({
        projectlist: null
    }),
    actions: {

        setProjects(data) {
            this.projectlist = data
        },

        async loadProjects() {
            await axios
            .get(`/api/v1/newproject`)
            .then(response => {
                this.setProjects(response.data)
                console.log(response.data)
            })
            .catch(error =>{
                console.log(error)     
            })
        }
    },
    
})