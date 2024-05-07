import { ref, reactive, computed } from 'vue'
import axios from 'axios'

export const useStore = () => {
  const state = reactive({
    projects : [],
    category: [],
    worktimetype: [],
    accesorytype: [],
    wood: [],
    collection: [],
    paints: [],
    elements: []
  })
  
  const loadData = async () => {
    await axios
      .get(`/api/v1/project/`)
      .then(response =>{
        //console.log(JSON.stringify(response.data))
        setData(response.data)    
      })
      .catch(error =>{
        console.log(error)
      })
  }

  const setData = (data) => {
    state.category = data.category
    state.worktimetype = data.worktimetype
    state.accesorytype = data.accesorytype
    state.wood = data.wood
    state.collection = data.collection
    state.paints = data.paints
  }

  const addElement = (element) => {
    state.elements.push(element)
  }



  return {
    state,
    loadData,
    setData,
    addElement,
    
  }
}
