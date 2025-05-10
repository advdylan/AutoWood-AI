import {defineStore} from 'pinia'
import axios from 'axios'

export const productionStore = defineStore('productionStore', {
  state: () => ({

    productionList: []

    
  }),

  getters: {
  }, 
  actions: {

    async getProductionList() {

      await axios
      .get(`/api/v1/production/production-list`)
      .then(response =>{
        console.log(response)
        this.productionList = response.data
      })
      .catch(error => {console.log(error)})

    }
  }
})