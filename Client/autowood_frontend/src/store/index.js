import { defineStore } from 'pinia'
import axios from 'axios'

export const useStore = defineStore('new-project', {
  state: () => ({
    projects : [],
    category: [],
    worktimetype: [],
    accesorytype: [],
    wood: [],
    collection: [],
    paints: [],
    elements: []
  }),
  actions: {
    async loadData() {
      await axios
      .get(`/api/v1/project/`)
      .then(response =>{
        console.log(JSON.stringify(response.data))
        this.setData(response.data)    
      })
      .catch(error =>{
        console.log(error)
      })
    },

    setData(data) {
      this.$state.category = data.category
      this.$state.worktimetype = data.worktimetype
      this.$state.accesorytype = data.accesorytype
      this.$state.wood = data.wood
      this.$state.collection = data.collection
      this.$state.paints = data.paints
    },

    addElement(element) {
      this.elements.push(element)
    }
  }
})
