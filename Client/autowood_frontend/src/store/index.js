import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    projects : [],
    category: [],
    worktimetype: [],
    accesorytype: [],
    wood: [],
    collection: [],
    paints: [],
    elements: {
      name: '',
      dimX: '',
      dimY: '',
      dimZ: '',
      wood_type: '',
      quantity: '',
    }

  },
  getters: {
  },
  mutations: {
    setData(state,data) {
      state.category = data.category
      state.worktimetype = data.worktimetype
      state.accesorytype = data.accesorytype
      state.wood = data.wood
      state.collection = data.collection
      state.paints = data.paints
      state.elements = data.elements
    },

    addElement(state, element) {
      state.elements.push(element)
    }
    
  }, 
  actions: {
    async loadData({commit}) {
      await axios
      .get(`/api/v1/project/`)
      .then(response =>{
        console.log(JSON.stringify(response.data))
        commit('setData', response.data)    
      })
      .catch(error =>{
        console.log(error)
      })
    },
  },
  modules: {
  }
})
