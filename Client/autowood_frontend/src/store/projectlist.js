import {defineStore} from 'pinia'
import axios from 'axios'
import { set } from 'core-js/core/dict'


export const useProjectsListStore = defineStore('projectslist', {
    state: () => ({
        projectlist: null
    }),
    actions: {
        async loadProjects() {
            await axios
            .get(`/api/v1/newproject`)
            .then(response => {
                setProjects(response.data)
                console.log(response.data)
            })
            .catch(error =>{
                console.log(error)     
            })
        }
    },
    setProjects(data) {
        this.projectlist = data
    }
})