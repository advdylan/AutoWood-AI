import {defineStore} from 'pinia'
import axios from 'axios'


export const useNewProjectStoreBeta = defineStore('newproject', {
  state: () => ({

    category: [],
    worktimetype: [],
    accesorytype: [],
    accesories: [],
    wood: [],
    collection: [],
    paints: [],
    elements: [],
    boxes: []
    


  }),

  getters: {
    accesoriesStore() {
      return this.accesories.map(accesory => ({
        ...accesory,
        sum: accesory.type.price * accesory.quantity 
      }))
    },
    pricedElements() {
      return this.elements.map(element => {
        console.log(element)
        
        let volume = (element.element.dimX / 1000) * (element.element.dimY / 1000) * (element.element.dimZ / 1000)
        let wood_type = this.wood.find(w => w.name === element.element.wood_type.name)
        
        if (!wood_type) {
          console.error(`Nie znaleziono typu drewna: ${element.element.wood_type}`)
          return {
            ...element,
            price: 'Nieznana cena - brak typu drewna'
          }
        }
     
        let price = (volume * wood_type.price) * element.quantity
        
        return {
          ...element,
          price: parseFloat(price).toFixed(2)
        }
          
         
      })
    },
    
    worktimeCost() {
      return this.boxes.map(works => ({
        ...works,
        sum: works.value * works.hours
      })
        
      )
    }

  }, 
  actions: {

    setData(data){
      this.category = data.category,
      this.worktimetype = data.worktimetype,
      this.accesorytype = data.accesorytype,
      this.wood = data.wood,
      this.collection = data.collection,
      this.paints = data.paints
      this.boxes = this.worktimetype.map(item => {
        return { text: item.name, value: item.cost, checked: false, hours: ''}
      })

    },

    $resetBoxes() {
      this.boxes = this.worktimetype.map(item => {
        return { text: item.name, value: item.cost, checked: false, hours: ''}
      })
      

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
      
      this.elements.push({
        element: {
          name: element.element.name,
          dimX: element.element.dimX,
          dimY: element.element.dimY,
          dimZ: element.element.dimZ,
          wood_type: element.element.wood_type
        },
        quantity: element.quantity
      });
      
    },

    deleteElement(element) {
      this.elements.pop(element)
    },
  
    addAccesory(accesory) {
      
      const newAccesory = {
        id: accesory.id,
        project: 0,
        quantity: accesory.quantity,
        type: {
            description: accesory.description,
            id: accesory.id,
            name: accesory.name,
            price: accesory.price,
            type: accesory.type,
            weight: accesory.weight
        }
    }

    //console.log("NewAcc" , newAccesory)
    this.accesories.push(newAccesory)
        

      
    },
    deleteAccesory(accesory) {
      
      this.accesories.pop({
        name: accesory.name,
        price: accesory.price,
        type: accesory.type,
        quantity: accesory.quantity
      })
    },

    setElements(newElements) {
      this.elements = newElements;
    },

    setAccesories(newAccesories) {
      this.accesories = newAccesories
    },

    $reset() {
      this.category = []
      this.worktimetype = []
      this.accesorytype = []
      this.accesories = []
      this.wood = []
      this.collection = []
      this.paints = []
      this.elements = []
      this.boxes = []
    },

   



    



    

    

  }
})