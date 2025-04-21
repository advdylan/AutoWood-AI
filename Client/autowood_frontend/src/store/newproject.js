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
    boxes: [],
    boards: [],
    marginA: 0,
    marginB: 0,
    marginC: 0,
    customer: {
      name: '',
      phone_number: 0,
      street: '',
      code: '',
      city: '',
      email: ''
    },
    files: [],
    projectName: null,
    selectedWood : null,
    selectedCategory : null,
    selectedCollection :null,
    selectedPaint : null,
    selectedFile: null,
    warehouseBoards: [],
    chosenWoodType: null,
    chosenThicknesses: new Set(),
    highlightedRows: new Set(),
    creationMode: '',
    productionSteps: [],
    chosenProductionSteps: [],
    deletedIDs: []
    

  }),

  getters: {
    filteredBoards: (state) => {
      return state.warehouseBoards.filter(
        (wood) => wood.wood_type.name === state.chosenWoodType && state.chosenThicknesses.has(wood.dimZ)
      );
    },
    accesoriesStore() {
      return this.accesories.map(accesory => ({
        ...accesory,
        sum: accesory.type.price * accesory.quantity      
      }))
    },
    pricedElements() {
      return this.elements.map(element => {
       
        
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
        sum: works.value * (works.hours * works.workers)
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
        return { text: item.name, value: item.cost, checked: false, hours: 0, workers: 0}
      })
    },

    chooseWoodType(woodType) {

      console.log("Selected Wood Type:", woodType); // Logs the clicked woodType
      this.chosenWoodType = woodType.name
      console.log("Updated Chosen Wood Type:", this.chosenWoodType); // Logs updated value

    },

    highlightRow(board) {
      console.log(board)
      if (this.highlightedRows.has(board)){
        console.log("It has same row")
        this.highlightedRows.delete(board)
      }
      else {
        this.highlightedRows.add(board)
      }
      
      
    },

    $resetBoxes() {
      this.boxes = this.worktimetype.map(item => {
        return { text: item.name, value: item.cost, checked: false, hours: 0, workers: 0}
      })
    },

    setBoxesViaProps(props) {     
      this.boxes = props.map(item => {
        return { text: item.worktime.name,
            value: item.cost,
            checked: false,
            hours: item.duration,
            workers: item.workers
          }      
      })
    },


    async loadData(){
      await axios
      .get(`/api/v1/project/`)
      .then(response =>{
        //console.log(JSON.stringify(response.data))
        this.setData(response.data)      
      })
      .catch(error =>{
        console.log(error)     
      })
    },

    async loadBoards() {
     await axios
    .get(`/api/v1/warehouse/boards/`)
    .then(response =>{
        //console.log(response)
        this.warehouseBoards = response.data
    })
    .catch(error => {
        //console.log(error)
    })

    },

    async updateAccesories(editedData) {
      await axios
      .post(`/api/v1/newproject/update-accesorytype/`, editedData, {
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

    async getProductionSteps() {
      await axios
      .get(`/api/v1/production/stages/`)
      .then (response => {
        console.log(JSON.stringify(response.data))
        this.productionSteps = response.data
      })
      .catch(error => {
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
    addBoard(board) { 
      console.log(board)  
      this.boards.push({
        board: {
          dimX: board.board.dimX,
          dimY: board.board.dimY,
          dimZ: board.board.dimZ,
          wood_type: board.board.wood_type
        },
        quantity: board.quantity
      });     
    },
    addWarehouseBoard(board) { 
      console.log(board)  
      this.warehouseBoards.push({
        
          dimX: board.board.dimX,
          dimY: board.board.dimY,
          dimZ: board.board.dimZ,
          wood_type: board.board.wood_type,
          quantity: board.quantity
      });     
    },


    deleteElement(element) {
      this.elements.pop(element)
    },
  
    addAccesory(accesory) {    
      //console.log(accesory)  
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
    //console.log("NewAcc:" , newAccesory)
    this.accesories.push(newAccesory)
    },
    addThickness(thickness) {
      if (this.chosenThicknesses.has(thickness)) {
        this.chosenThicknesses.delete(thickness);
      } else {
        this.chosenThicknesses.add(thickness);
    }

    },
    addAccesorytype(accesory) {
      this.accesorytype.push(accesory)
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

    setWorktimes(worktimes) {
      this.boxes = worktimes
    },
    setMode(mode) {
      this.creationMode = mode
    },
    addNewStage(stage) {
      this.chosenProductionSteps.push(stage)
    },
    deleteStage(stage) {
      const stageToDelete = this.chosenProductionSteps.findIndex(item => item.stage_name === stage.stage_name & item.shortcut === stage.shortcut)
      this.chosenProductionSteps.splice(stageToDelete, 1)
    
    },
    deleteNewStage(stage) {
      const stageToDelete = this.productionSteps.findIndex(item => item.stage_name === stage.stage_name & item.shortcut === stage.shortcut)
      this.productionSteps.splice(stageToDelete, 1)
      this.deletedIDs.push(stage.id)

    },

    addProductionStages(stages) {
      for(let stage of stages) {
          this.chosenProductionSteps.push(stage)
          console.log(`Stage: ${stage}`)
      }
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
      this.marginA = 0
      this.marginB = 0
      this.marginC = 0
      this.customer = {
        name: '',
        phone_number: '',
        street: '',
        code: '',
        city: '',
        email: ''
      }
      this.files = []
      
      this.projectName = null
      this.selectedWood = null
      this.selectedCategory = null
      this.selectedCollection = null
      this.selectedPaint = null
      this.selectedFile = null
    },

   



    



    

    

  }
})