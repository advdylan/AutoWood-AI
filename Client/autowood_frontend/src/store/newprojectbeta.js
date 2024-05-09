import {defineStore} from 'pinia'
import {ref, computed} from 'vue'


export const useNewProjectStoreBeta = defineStore('newproject', {
  state: () => ({

    category: [],
    worktimetype: [],
    accesorytype: [],
    wood: [],
    collection: [],
    paints: [],
    elements: [
      {
      name: '',
      dimX: '',
      dimY: '',
      dimZ: '',
      quantity: '',
      wood_type: ''
      }
    ]

  }),
  actions: {
    addElement(element) { 
        this.elements.push(...element)
    }
  }
})