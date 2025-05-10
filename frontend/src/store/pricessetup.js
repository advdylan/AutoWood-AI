import { defineStore } from 'pinia'
import { setTransitionHooks } from 'vue'
import axios from 'axios'

export const usePricesSetup = defineStore('pricessetup', {
    state: () => ({

      newWorktimeCost: []
      
    }),
    actions: {

      updateLocalWorktimetypes(value) {
        this.newWorktimeCost = value
      },
      async updateWorktimetypes(editedData) {
        await axios
        .post(`/api/v1/newproject/update-worktimetypes/`, editedData, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => {
          console.log(JSON.stringify(response.data))   
          return true   
        })
        .catch(error => {
          //console.log(JSON.stringify(response.data))  
          console.log(error)
          return false
        })
      },
      
    },
  })

