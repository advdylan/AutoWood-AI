import {defineStore} from 'pinia'
import axios from 'axios'


export const useProjectsListStore = defineStore('projectslist', {
    state: () => ({
        projectlist: null
    }),
    actions: {
        async loadProjects() {
            await axios
            .get(`/api/v1/project`)
        }
    }
})