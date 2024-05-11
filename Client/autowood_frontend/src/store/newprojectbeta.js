import {defineStore} from 'pinia'
import {ref, computed} from 'vue'
import axios from 'axios'


export const useNewProjectStoreBeta = defineStore('newproject', {
  state: () => ({

    category: [],
    worktimetype: [],
    accesorytype: [],
    wood: [],
    collection: [],
    paints: [],
    elements: [
    ]

  }),
  actions: {

    setData(data){
      this.category = data.category,
      this.worktimetype = data.worktimetype,
      this.accesorytype = data.accesorytype,
      this.wood = data.wood,
      this.collection = data.collection,
      this.paints = data.paints

    },


    async loadData(){
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


    addElement(element) { 
      console.log(element)
        this.elements.push({
        
          id: Math.floor(Math.random()* 10000000),
          name: element.name,
          dimX: element.dimX,
          dimY: element.dimY,
          dimZ: element.dimZ,
          quantity: element.quantity,
          wood_type: element.wood_type
        })
        
        
        

        
         
       
    
    }
  }
})