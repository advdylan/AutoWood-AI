import {defineStore} from 'pinia'
import {ref, computed} from 'vue'
import axios from 'axios'

export const useNewProjectStore = defineStore('newproject', () => {

    const state = {

    category : ref([]),
    worktimetype : ref([]),
    accesorytype : ref([]),
    wood : ref([]),
    collection : ref([]),
    paints : ref([]),
    elements: ref({})
    }

    const loading = ref(false)


    async function loadData() {
        loading.value = true
       await axios
      .get(`/api/v1/project/`)
      .then(response =>{
        console.log(JSON.stringify(response.data))
        setData(response.data)
        loading.value = false    
      })
      .catch(error =>{
        console.log(error)
        loading.value = false

    })
  }

    function setData(data) {
      state.category.value = data.category
      state.worktimetype.value = data.worktimetype
      state.accesorytype.value = data.accesorytype
      state.wood.value = data.wood
      state.collection.value = data.collection
      state.paints.value = data.paints

  }

    function addElement(element) {
      state.elements.value.push(element)
    }

    return { state, addElement, loadData, setData}
  })



  